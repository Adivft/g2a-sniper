import requests
import os

# Ye data hum GitHub settings se uthayenge (Security ke liye)
TOKEN = os.getenv('8606162602:AAE8DMUIPK-tSybQVy1zqIUs9d6fOI1b0A4')
CHAT_ID = os.getenv('5113069108')
TARGET = 40  # 40% se upar hi alert chahiye

def check_g2a():
    # G2A Scraper Logic
    # Maan le live price fetch ho rahi h
    price = 110.0  # Ye example h, script live check karegi
    original = 200.0
    discount = ((original - price) / original) * 100

    if discount >= TARGET:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        data = {"chat_id": CHAT_ID, "text": f"🔥 DEAL ALERT! {discount}% OFF\nPrice: ${price}\nBhag ke check kar!"}
        requests.post(url, data=data)

if __name__ == "__main__":
    check_g2a()
