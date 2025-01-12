#!/bin/bash
# Cài đặt Google Chrome nếu cần thiết (nếu chưa có)
if ! [ -x "$(command -v google-chrome)" ]; then
  echo "Google Chrome chưa được cài đặt, tiến hành cài đặt..."
  apt-get update
  apt-get install -y wget unzip
  wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
  dpkg -i google-chrome-stable_current_amd64.deb || apt-get -f install -y
fi

# Đảm bảo quyền thực thi cho Chrome
chmod +x /usr/bin/google-chrome

# Cài đặt môi trường ảo Python nếu chưa có
if [ ! -d "antenv" ]; then
  python3 -m venv antenv
fi
source antenv/bin/activate

# Cài đặt các thư viện yêu cầu
pip install -r requirements.txt

# Khởi động ứng dụng Flask
gunicorn --bind=0.0.0.0:8000 app:app
