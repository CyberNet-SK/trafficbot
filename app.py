from flask import Flask, request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import threading
import time
import os

app = Flask(__name__)

def visit_website(target_url):
    try:
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)
        driver.get(target_url)
        time.sleep(8)  # অ্যাড লোড হওয়ার জন্য অপেক্ষা
        driver.quit()
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

@app.route('/')
def home():
    return "🚀 Bot is active!"

@app.route('/visit')
def visit():
    target = request.args.get('url', 'https://example.com')
    thread = threading.Thread(target=visit_website, args=(target,))
    thread.start()
    return f"✅ Visiting {target} started!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
