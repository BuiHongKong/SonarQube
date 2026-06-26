"""Code MOI co y de demo Quality Gate FAIL tren new code.

Tat ca gia tri "secret" duoi day la GIA (placeholder), KHONG phai secret that.
Do not commit real secrets to git.
"""

import hashlib
import os
import sqlite3
import subprocess


# Hardcoded credentials (gia) -> Security Hotspot / Vulnerability MOI
FAKE_API_KEY = "FAKE_sk_live_0000111122223333_NOT_REAL"
FAKE_DB_PASSWORD = "FAKE_P@ssw0rd_NOT_REAL"
FAKE_AWS_SECRET = "FAKE_AKIA_EXAMPLE_SECRET_NOT_REAL"
FAKE_JWT_SECRET = "FAKE_jwt_signing_key_NOT_REAL"


def login(username, password):
    """SQL Injection MOI: noi chuoi vao query."""
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE name = '" + username + "' AND pwd = '" + password + "'"
    cursor.execute(query)
    return cursor.fetchall()


def run_shell(user_cmd):
    """Command Injection MOI: shell=True voi input nguoi dung."""
    return subprocess.call("echo " + user_cmd, shell=True)


def eval_expr(expr):
    """Code Injection MOI: eval tren input."""
    return eval(expr)


def weak_hash(value):
    """Weak crypto MOI: MD5."""
    return hashlib.md5(value.encode()).hexdigest()


def build_conn_string():
    """Dung hardcoded credential gia truc tiep."""
    return f"postgres://admin:{FAKE_DB_PASSWORD}@10.0.0.9:5432/prod"


def always_true(x):
    """Bug MOI: dieu kien luon dung (x != 1 or x != 2)."""
    if x != 1 or x != 2:
        return "luon vao day"
    return "khong bao gio"


def get_token():
    """Doi chieu: cach dung la doc tu env."""
    return os.environ.get("API_TOKEN", "")
