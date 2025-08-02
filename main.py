from chart_capture import capture_chart
from decision_maker import analyze_chart
from entry_manager import execute_trade
import time

def main_loop():
    while True:
        print("🔄 M1 шинэ лаа шалгаж байна...")
        image_path = capture_chart()
        signal = analyze_chart(image_path)

        if signal:
            print(f"✅ Шийдвэр гарлаа: {signal}")
            execute_trade(signal)
        else:
            print("⏭ Орж болох нөхцөл бүрдээгүй.")

        time.sleep(60)  # 1 минут тутамд ажиллана

if __name__ == "__main__":
    main_loop()
