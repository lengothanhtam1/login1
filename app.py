from flask import Flask, redirect
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

app = Flask(__name__)

# Cấu hình Selenium WebDriver
def start_browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Chạy không giao diện
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.binary_location = "/usr/bin/google-chrome"  # Đường dẫn Chrome trên môi trường Azure

    # Tự động cài đặt ChromeDriver với webdriver-manager
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

@app.route("/")
def login_to_chatgpt():
    driver = start_browser()
    driver.get("https://chat.openai.com/")  # Mở trang ChatGPT
    
    # Đăng nhập tự động
    time.sleep(2)
    try:
        # Tìm và điền email
        email_box = driver.find_element(By.NAME, "username")
        email_box.send_keys("vutruongnguyen2015@gmail.com")  # Thay bằng email của bạn
        email_box.send_keys(Keys.RETURN)

        time.sleep(2)
        # Tìm và điền mật khẩu
        password_box = driver.find_element(By.NAME, "password")
        password_box.send_keys("Mua_chatgpt_Lien_He_Zalo_0372324770")  # Thay bằng mật khẩu của bạn
        password_box.send_keys(Keys.RETURN)

        time.sleep(5)  # Chờ đăng nhập hoàn tất
    except Exception as e:
        print(f"Lỗi xảy ra: {e}")
    finally:
        # Đóng trình duyệt sau khi hoàn thành
        driver.quit()

    # Trả về thông báo thành công
    return "Đăng nhập tự động hoàn tất!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
