import json
import datetime
import os

def log_trade(signal, status="EXECUTED", folder="trade_logs"):
    os.makedirs(folder, exist_ok=True)
    now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = os.path.join(folder, f"trade_{now}.json")

    log_data = {
        "timestamp": now,
        "status": status,
        "direction": signal.get("direction"),
        "entry": signal.get("entry"),
        "sl": signal.get("sl"),
        "tp1": signal.get("tp1"),
        "tp2": signal.get("tp2"),
        "tp3": signal.get("tp3")
    }

    with open(filename, "w") as f:
        json.dump(log_data, f, indent=4)

    print(f"📥 Trade лог хадгалсан: {filename}")
