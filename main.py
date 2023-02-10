import psutil
import requests

THRESHOLD = 1024

memory_info = psutil.virtual_memory()
current_usage = memory_info.used / 1024 / 1024
if current_usage > THRESHOLD:
    url = "https://example.com/"
    data = {
        "memory_usage": current_usage,
        "threshold": THRESHOLD
    }
    response = requests.post(url, data=data)

    if response.status_code == 200:
        print("Alarm sent to API.")
    else:
        print("Failed to send alarm to API.")
else:
    print("Memory usage is under the threshold.")
