"""Test cho python/vulnerabilities.py (ban da lam sach) de tang coverage."""

import hashlib
import sqlite3

import python.vulnerabilities as vuln


def test_get_api_key(monkeypatch):
    monkeypatch.setenv("API_KEY", "abc")
    assert vuln.get_api_key() == "abc"


def test_hash_password():
    expected = hashlib.sha256("secret".encode()).hexdigest()
    assert vuln.hash_password("secret") == expected


def test_connect_db(monkeypatch):
    monkeypatch.setenv("DB_PASSWORD", "p")
    monkeypatch.setenv("DB_HOST", "h")
    assert vuln.connect_db() == "postgres://app:p@h:5432/app"


def test_get_user(monkeypatch):
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE users (name TEXT)")
    conn.execute("INSERT INTO users (name) VALUES ('alice')")
    conn.commit()
    monkeypatch.setattr(vuln.sqlite3, "connect", lambda *a, **k: conn)
    assert vuln.get_user("alice") == [("alice",)]


def test_fetch_data(monkeypatch):
    class FakeResp:
        text = "hello"

    monkeypatch.setattr(vuln.requests, "get", lambda *a, **k: FakeResp())
    assert vuln.fetch_data("http://example.com") == "hello"
