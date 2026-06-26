"""Demo các lỗi Vulnerability / Security Hotspot mà SonarQube phát hiện.

Đây là code DEMO có lỗi cố ý, KHÔNG dùng cho production.
"""

import hashlib
import os
import sqlite3
import subprocess

import requests

# Security Hotspot / Vulnerability: hardcoded credentials
DB_PASSWORD = "SuperSecret123!"
API_KEY = "FAKE_DEMO_API_KEY_NOT_REAL"
AWS_SECRET = "FAKE_DEMO_AWS_SECRET_NOT_REAL"


def get_user(username):
    """SQL Injection: nối trực tiếp input vào câu query."""
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchall()


def ping_host(host):
    """Command Injection: shell=True với input người dùng."""
    cmd = "ping -c 1 " + host
    return subprocess.call(cmd, shell=True)


def run_code(user_input):
    """Code Injection: eval trên dữ liệu đầu vào."""
    return eval(user_input)


def hash_password(password):
    """Weak crypto: MD5 không an toàn cho mật khẩu."""
    return hashlib.md5(password.encode()).hexdigest()


def fetch_data(url):
    """Insecure: tắt xác thực chứng chỉ SSL/TLS."""
    response = requests.get(url, verify=False)
    return response.text


def connect_db():
    """Hardcoded credentials sử dụng trực tiếp."""
    return f"postgres://admin:{DB_PASSWORD}@10.0.0.5:5432/prod"


def read_secret_from_env():
    """So sánh: cách làm đúng là đọc từ biến môi trường (để đối chiếu)."""
    return os.environ.get("API_KEY", "")
