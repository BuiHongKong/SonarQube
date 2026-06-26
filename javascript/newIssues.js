// Code MOI co y de demo Quality Gate FAIL tren new code.
// Tat ca gia tri "secret" duoi day la GIA (placeholder), KHONG phai secret that.
// Do not commit real secrets to git.

const crypto = require("crypto");
const { exec } = require("child_process");

// Hardcoded credentials (gia) -> Security Hotspot / Vulnerability MOI
const FAKE_API_KEY = "FAKE_sk_live_0000111122223333_NOT_REAL";
const FAKE_DB_PASSWORD = "FAKE_P@ssw0rd_NOT_REAL";
const FAKE_JWT_SECRET = "FAKE_jwt_signing_key_NOT_REAL";

function login(db, username, password) {
  // SQL Injection MOI
  const query =
    "SELECT * FROM users WHERE name = '" + username + "' AND pwd = '" + password + "'";
  return db.query(query);
}

function runShell(userCmd) {
  // Command Injection MOI
  exec("echo " + userCmd, (err, stdout) => {
    console.log(stdout);
  });
}

function evalExpr(expr) {
  // Code Injection MOI
  return eval(expr);
}

function weakHash(value) {
  // Weak crypto MOI: MD5
  return crypto.createHash("md5").update(value).digest("hex");
}

function makeToken() {
  // Security Hotspot MOI: Math.random cho token
  return Math.random().toString(36).substring(2);
}

function checkEqual(a) {
  // Bug MOI: so sanh === NaN luon false
  if (a === NaN) {
    return "la NaN";
  }
  return "khong phai NaN";
}

module.exports = {
  login,
  runShell,
  evalExpr,
  weakHash,
  makeToken,
  checkEqual,
  FAKE_API_KEY,
  FAKE_DB_PASSWORD,
  FAKE_JWT_SECRET,
};
