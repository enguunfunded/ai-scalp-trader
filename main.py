from chart_capture import capture_chart
from decision_maker import analyze_chart
from entry_manager import execute_trade
from log_writer import log_trade
import time

def main_loop():
    while True:
        print("🔄 M1 шинэ лаа шалгаж байна...")
        image_path = capture_chart()
        signal = analyze_chart(image_path)

        if signal:
            print(f"✅ GPT шийдвэрээр оролт хийгдэж байна: {signal}")
            execute_trade(signal)
            log_trade(signal)
        else:
            print("⏭ GPT: Орж болох нөхцөл бүрдээгүй.")

        time.sleep(60)

if __name__ == "__main__":
    main_loop()
