import os
import httpx
import time
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

if not API_KEY:
    raise ValueError("Groq API key was not found.")


def call_model(user_input):

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    # 1. Prepare the request
    request_data = {
        "model": "openai/gpt-oss-20b",
        "messages": [
            {
                "role": "user",
                "content": user_input
            }
        ]
    }

    try:
        # 2. Start measuring time
        start_time = time.perf_counter()

        # 3. Send request to Groq
        response = httpx.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json=request_data,
            timeout=60.0
        )

        # 4. Check the HTTP response
        response.raise_for_status()

        # 5. Convert response into a Python dictionary
        data = response.json()

        # 6. Stop measuring time
        end_time = time.perf_counter()
        latency = end_time - start_time

        # 7. Extract model information
        output = data["choices"][0]["message"]["content"]

        usage = data["usage"]

        input_tokens = usage["prompt_tokens"]
        output_tokens = usage["completion_tokens"]
        total_tokens = usage["total_tokens"]

        # 8. Create the log record
        log_record = {
            "model": data["model"],
            "input": user_input,
            "output": output,
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "total_tokens": total_tokens,
            "latency_seconds": latency
        }

        # 9. Save the record
        with open("model_calls.jsonl", "a", encoding="utf-8") as file:
            file.write(json.dumps(log_record) + "\n")

        # 10. Return the model's response
        return log_record

    except httpx.ConnectError:
        print("Could not connect to Groq.")

    except httpx.TimeoutException:
        print("The request took too long.")

    except httpx.HTTPStatusError as error:
        print("Groq returned an HTTP error:")
        print("Status:", error.response.status_code)
        print("Details:", error.response.text)

    except (KeyError, IndexError, TypeError, ValueError) as error:
        print("Could not process the model response:", error)

    return None


# Run a test
result = call_model(
    "My account is locked. I cannot log in."
)

if result is not None:
    print("\nMODEL OUTPUT:")
    print(result["output"])

    print("\nINPUT TOKENS:", result["input_tokens"])
    print("OUTPUT TOKENS:", result["output_tokens"])
    print("TOTAL TOKENS:", result["total_tokens"])

    print("\nLATENCY:", result["latency_seconds"], "seconds")
