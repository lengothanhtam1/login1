from flask import Flask, redirect
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager  # Quản lý ChromeDriver tự động
import time

app = Flask(__name__)

# Cấu hình Selenium WebDriver
def start_browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Chạy không giao diện
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    # Sử dụng webdriver_manager để tải xuống ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

@app.route("/")
def login_to_chatgpt():
    driver = start_browser()
    driver.get("https://chat.openai.com/")  # Mở trang ChatGPT
    
    # Đăng nhập tự động
    time.sleep(2)
    try:
        # Điền email
        email_box = driver.find_element(By.NAME, "username")
        email_box.send_keys("vutruongnguyen2015@gmail.com")  # Thay bằng email của bạn
        email_box.send_keys(Keys.RETURN)

        time.sleep(2)
        # Điền mật khẩu
        password_box = driver.find_element(By.NAME, "password")
        password_box.send_keys("Mua_chatgpt_Lien_He_Zalo_0372324770")  # Thay bằng mật khẩu của bạn
        password_box.send_keys(Keys.RETURN)

        time.sleep(5)  # Chờ đăng nhập hoàn tất
    except Exception as e:
        print("Error occurred:", e)

    # Lấy URL đã đăng nhập thành công
    chat_url = driver.current_url
    driver.quit()
    return redirect(chat_url)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
