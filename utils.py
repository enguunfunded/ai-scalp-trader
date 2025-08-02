import json
import datetime

def load_config(path="config.json"):
    with open(path, "r") as f:
        return json.load(f)

def write_log(message, file="logs.txt"):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file, "a") as f:
        f.write(f"[{now}] {message}\n")
