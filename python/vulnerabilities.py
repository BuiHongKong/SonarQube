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


# ===== Lỗi MỚI chèn vào code cũ để new code dính vuln (key giả, không phải secret thật) =====
STRIPE_KEY = "FAKE_sk_live_51XXXXNOTREAL00000000"
GITHUB_TOKEN = "FAKE_ghp_000011112222333344445555_NOTREAL"
SLACK_WEBHOOK = "https://hooks.slack.com/services/FAKE/NOT/REAL"


def authenticate(username, password):
    """SQL Injection MỚI + so sánh credential cứng (giả)."""
    if username == "admin" and password == "FAKE_admin_pwd_NOTREAL":
        return True
    query = "SELECT * FROM accounts WHERE u='" + username + "' AND p='" + password + "'"
    return query


def deserialize(blob):
    """Insecure deserialization MỚI: pickle trên dữ liệu ngoài."""
    import pickle

    return pickle.loads(blob)


def make_temp(name):
    """Path traversal / insecure temp MỚI."""
    path = "/tmp/" + name
    with open(path, "w") as f:
        f.write("data")
    return path


def md5_token(seed):
    """Weak crypto MỚI: MD5 cho token."""
    return hashlib.md5(seed.encode()).hexdigest()
