import pyautogui
import time

def execute_trade(signal):
    print(f"🚀 Оролт эхэлж байна: {signal['direction']} @ {signal['entry']}")

    # ⚠️ Энэ хэсэгт MT5 цонхны координатыг тааруулна уу!
    # Жишээ: SELL товчлуурын байршил
    if signal["direction"] == "SELL":
        pyautogui.moveTo(1350, 80)  # ← та өөрөө тохируул
        pyautogui.click()
    elif signal["direction"] == "BUY":
        pyautogui.moveTo(1280, 80)  # ← BUY товч байрлал
        pyautogui.click()
    
    # Delay to simulate human click
    time.sleep(1)

    # Та SL / TP-үүдийг гараар урьдчилан тавьсан шаблоноор тавих эсвэл automation хийж болно
    print(f"✅ {signal['direction']} оролт хийгдлээ — SL: {signal['sl']} TP1: {signal['tp1']}")
