# 🧠 AI Scalp Trader (MT5 Automation)

Энэхүү систем нь 1 минутын timeframe-ийн чарт дээр үндэслэн **screenshot авч**, зураг дээр **AI дүн шинжилгээ хийж**, **автоматаар MT5 дээр оролт хийх** бүрэн автомат scalp арилжааны систем юм.

---

## ⚙️ Системийн бүрэлдэхүүн:

| Файл | Үүрэг |
|------|-------|
| `main.py` | Бүх процессыг нэгтгэж ажиллуулдаг гол файл |
| `chart_capture.py` | MT5 чартын screenshot авдаг |
| `decision_maker.py` | Зураг дээр үндэслэн AI шийдвэр гаргана |
| `entry_manager.py` | MT5 дээр BUY/SELL автоматаар дарна |
| `config.json` | Хувийн тохиргоо: risk, lot, cooldown г.м |
| `log_writer.py` | Trade бүрийн лог файл үүсгэнэ |
| `utils.py` | Конфиг унших, лог бичих функц |
| `requirements.txt` | Python шаардлагатай сангууд |

---

## 🛠️ Суулгах заавар

1. Python 3.10+ суулгасан эсэхээ шалгана:
   ```bash
   python --version

