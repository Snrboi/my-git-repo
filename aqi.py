from datetime import datetime

history = [
    {"city": "ph", "aqi": 2, "timestamp": "2026-08-10T14:32:00" },
    {"city": "abuja", "aqi": 1, "timestamp": "2026-07-12T14:32:00" },
    {"city": "abuja", "aqi": 0, "timestamp": "2026-09-12T14:32:00" }
]

best_aqi_quality = 5

for item in history:
    aqi = item["aqi"]
    date = datetime.fromisoformat(item["timestamp"]).date()
    if aqi < best_aqi_quality:
        best_aqi_quality = aqi
print(best_aqi_quality, date)
