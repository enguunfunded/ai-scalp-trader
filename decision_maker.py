import openai
import base64
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_chart(image_path):
    with open(image_path, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode('utf-8')

    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Та туршлагатай scalp трейдер. Зураг дээр үндэслэн зөвхөн BUY, SELL, эсвэл NO TRADE шийдвэр гаргана уу. Хэрвээ оролт боломжтой бол entry, SL, TP1, TP2, TP3 утгуудыг заавал өгнө үү."},
            {"role": "user", "content": [
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/png;base64,{base64_image}"
                    }
                }
            ]}
        ],
        max_tokens=500
    )

    result = response.choices[0].message.content
    print(f"🤖 GPT шийдвэр:\n{result}")

    if "NO TRADE" in result.upper():
        return None

    try:
        # GPT хариултаас үнэ гаргаж авах (prompt-оос шалтгаална)
        lines = result.strip().splitlines()
        parsed = {}
        for line in lines:
            if ":" in line:
                key, val = line.split(":")
                parsed[key.strip().lower()] = float(val.strip())

        return {
            "direction": "BUY" if "buy" in result.lower() else "SELL",
            "entry": parsed.get("entry"),
            "sl": parsed.get("sl"),
            "tp1": parsed.get("tp1"),
            "tp2": parsed.get("tp2"),
            "tp3": parsed.get("tp3")
        }
    except:
        return None
