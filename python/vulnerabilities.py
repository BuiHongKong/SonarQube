"""Các thao tác I/O được viết theo chuẩn an toàn (đã làm sạch).

Không còn hardcoded credentials, SQL injection, command injection, eval,
weak crypto hay tắt xác thực SSL.
"""

import hashlib
import os
import sqlite3

import requests

HTTP_TIMEOUT = 10


def get_api_key():
    """Đọc khóa từ biến môi trường thay vì hardcode."""
    return os.environ.get("API_KEY", "")


def get_user(username):
    """Dùng truy vấn tham số hóa để tránh SQL injection."""
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE name = ?", (username,))
    return cursor.fetchall()


def hash_password(password):
    """Dùng SHA-256 thay cho MD5."""
    return hashlib.sha256(password.encode()).hexdigest()


def fetch_data(url):
    """Giữ xác thực chứng chỉ SSL mặc định và đặt timeout."""
    response = requests.get(url, timeout=HTTP_TIMEOUT)
    return response.text


def connect_db():
    """Lấy thông tin kết nối từ biến môi trường."""
    password = os.environ.get("DB_PASSWORD", "")
    host = os.environ.get("DB_HOST", "localhost")
    return f"postgres://app:{password}@{host}:5432/app"
