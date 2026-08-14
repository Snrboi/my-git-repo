# def reverse_string(value):
#     rev = ""
#     for char in value:
#         rev  =  char + rev
#     return rev

aios = {
    "users": [
        {
            "username": "snrboi",
            "profile": {
                "role": "AI Engineer",
                "skills": ["Python", "Git"]
            }
        },
        {
            "username": "admin",
            "profile": {
                "role": "System Administrator",
                "skills": ["Linux", "Security"]
            }
        }
    ]
}

for user in aios["users"]:
    name = user["username"]
    role = user["profile"]["role"]
    print(f"User: {name}")
    print(f"Role: {role}")
    print("Skills:")
    for skill in user["profile"]["skills"]:
        print(f"-{skill}")

