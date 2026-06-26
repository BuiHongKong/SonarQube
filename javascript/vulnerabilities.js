// Các thao tác được viết theo chuẩn an toàn (đã làm sạch).
// Không còn hardcoded creds, eval, innerHTML XSS, Math.random cho token, tắt TLS.

const crypto = require("crypto");

function getApiKey() {
  return process.env.API_KEY || "";
}

function getUser(db, username) {
  // Truy vấn tham số hóa, tránh SQL injection
  return db.query("SELECT * FROM users WHERE name = ?", [username]);
}

function strongHash(value) {
  // SHA-256 thay cho MD5
  return crypto.createHash("sha256").update(value).digest("hex");
}

function generateToken() {
  // Sinh token bằng nguồn ngẫu nhiên an toàn về mật mã
  return crypto.randomBytes(16).toString("hex");
}

module.exports = { getApiKey, getUser, strongHash, generateToken };
