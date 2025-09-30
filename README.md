# 🎨 AsciiFyer — Text to ASCII Code Converter & Decoder 🔄

<img width="712" height="352" alt="swappy-20250930-225009" src="https://github.com/user-attachments/assets/ab0f90b8-f34c-4863-9a21-eed45230f22b" />

Welcome to **AsciiFyer**, your colorful terminal tool for converting text to ASCII codes (Asciify) and back (De-Asciify)!  
Perfect for encoding sensitive strings like webhooks or just playing around with ASCII art and code.  

---

## 🚀 Features

- 🎭 **Asciify:** Convert any text into a sequence of ASCII codes  
- 🔄 **De-Asciify:** Decode ASCII codes back into readable text   
- 🖥️ Easy-to-use interactive menu with clear options  

---

## 🎯 Why Use AsciiFyer?

- 🔒 Hide sensitive info like webhooks by converting them into ASCII codes  
- 🧩 Quickly encode and decode text for debugging or fun  
- 🔡 **Asciify:** Turn any string into its ASCII code representation
- 🔁 **De-Asciify:** Convert ASCII codes back into normal text
- ✅ Simple, interactive menu      

---

## 📋 Usage

1. Run the script:  
   ```bash
   python AsciiFyer.py
   ```

## ⚙️ Requirements

- Python 3.x

- rich

Install dependencies manually if needed:
   ```bash
   pip install rich pystyle
   ```


# 🔐 Using AsciiFied Webhooks

If you plan to Asciify a Discord webhook and use it in your own script, you'll need a small decoder.

👇 Use this snippet to decode the webhook before using it:
   ```bash
   def ascii_decode(ascii_codes_str):
    return ''.join(chr(int(code)) for code in ascii_codes_str.strip().split())
   ```


Then use:

   ```bash
   ascii_webhook = """Asciifyed Webhook"""
   ```
⚠️ Replace "Asciifyed Webhook" with your actual Asciified webhook (space-separated numbers).
This will return the original webhook URL you can use in requests.


# 📝 License

This project is licensed under the [MIT License](LICENSE).
