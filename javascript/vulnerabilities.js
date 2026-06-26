// Demo các lỗi Vulnerability / Security Hotspot mà SonarQube phát hiện.
// Code DEMO có lỗi cố ý, KHÔNG dùng cho production.

const https = require("https");
const { exec } = require("child_process");
const crypto = require("crypto");

// Security Hotspot / Vulnerability: hardcoded credentials
const DB_PASSWORD = "SuperSecret123!";
const API_KEY = "FAKE_DEMO_API_KEY_NOT_REAL";

// Vulnerability: tắt xác thực chứng chỉ TLS toàn cục
process.env.NODE_TLS_REJECT_UNAUTHORIZED = "0";

function getUser(db, username) {
  // SQL Injection: nối trực tiếp input vào query
  const query = "SELECT * FROM users WHERE name = '" + username + "'";
  return db.query(query);
}

function pingHost(host) {
  // Command Injection: exec với input người dùng
  exec("ping -c 1 " + host, (err, stdout) => {
    console.log(stdout);
  });
}

function runCode(userInput) {
  // Code Injection: eval trên dữ liệu đầu vào
  return eval(userInput);
}

function generateToken() {
  // Security Hotspot: Math.random() không an toàn cho token bảo mật
  return Math.random().toString(36).substring(2);
}

function weakHash(password) {
  // Weak crypto: MD5 không an toàn
  return crypto.createHash("md5").update(password).digest("hex");
}

function renderProfile(userInput) {
  // DOM XSS: gán trực tiếp input vào innerHTML
  const el = document.getElementById("profile");
  el.innerHTML = userInput;
}

function fetchInsecure(url) {
  // Insecure: tắt xác thực chứng chỉ
  const agent = new https.Agent({ rejectUnauthorized: false });
  return fetch(url, { agent });
}

module.exports = {
  getUser,
  pingHost,
  runCode,
  generateToken,
  weakHash,
  renderProfile,
  fetchInsecure,
  DB_PASSWORD,
  API_KEY,
};
