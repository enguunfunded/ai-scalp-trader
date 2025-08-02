import random

def analyze_chart(image_path):
    # ⛔️ Энд жинхэнэ OpenCV/AI анализ хийгдэх ёстой
    # Туршилтын горим: random шийдвэр гаргана
    decision = random.choice([True, False])
    
    if decision:
        direction = random.choice(["BUY", "SELL"])
        entry_price = round(random.uniform(2280, 2300), 2)
        sl = entry_price - 3 if direction == "BUY" else entry_price + 3
        tp1 = entry_price + 3 if direction == "BUY" else entry_price - 3
        tp2 = entry_price + 5 if direction == "BUY" else entry_price - 5
        tp3 = entry_price + 8 if direction == "BUY" else entry_price - 8

        return {
            "direction": direction,
            "entry": entry_price,
            "sl": round(sl, 2),
            "tp1": round(tp1, 2),
            "tp2": round(tp2, 2),
            "tp3": round(tp3, 2)
        }
    else:
        return None
