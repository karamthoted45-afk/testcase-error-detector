
import psutil
import time
import json
from datetime import datetime

def get_metrics():
    return {
        "timestamp": str(datetime.now()),
        "cpu_usage": psutil.cpu_percent(),
        "ram_usage": psutil.virtual_memory().percent,
        "disk_usage": psutil.disk_usage('/').percent
    }

def save_log(data):
    with open("monitor_log.json", "a") as file:
        file.write(json.dumps(data) + "\n")

if __name__ == "__main__":
    try:
        while True:
            metrics = get_metrics()
            print(metrics)
            save_log(metrics)
            time.sleep(3)
    except KeyboardInterrupt:
        print("Stopped.")
