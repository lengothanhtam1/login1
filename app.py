from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Danh sách tài khoản giả lập
users = {"user1": "password1", "user2": "password2"}

@app.route('/')
def home():
    return render_template('login.html')  # Hiển thị trang đăng nhập

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username in users and users[username] == password:
        # Chuyển hướng tới ChatGPT
        return redirect('https://chat.openai.com/')
    else:
        return "Login failed. Please try again."

if __name__ == '__main__':
    app.run(debug=True)
