# SonarQube Demo Buggy Project

Repo demo đa ngôn ngữ (Python + JavaScript) chứa **code lỗi cố ý** nhằm minh họa khả năng
phát hiện của SonarQube trên đầy đủ các nhóm issue: **Bugs, Vulnerabilities, Security Hotspots,
Code Smells, Duplications**.

> Cảnh báo: Đây là code DEMO. Không sử dụng cho production.

## Cấu trúc

```
SonarQube/
  sonar-project.properties
  python/
    vulnerabilities.py     # SQLi, command injection, hardcoded secret, eval, MD5, SSL off
    bugs.py                # is-literal, identical operands, unreachable, mutable default
    code_smells.py         # complexity cao, empty except, unused, magic numbers, duplicate literals
    duplicate_a.py         # khối logic trùng lặp
    duplicate_b.py         # khối logic trùng lặp (giống a) -> Duplications
  javascript/
    vulnerabilities.js     # hardcoded creds, eval, innerHTML XSS, Math.random token, TLS off
    bugs.js                # == vs ===, assignment in condition, duplicate keys, unreachable, NaN
    codeSmells.js          # var, nested ternary, complexity cao, unused, duplicate literals
```

## Bảng ánh xạ file -> loại issue dự kiến

| File | Nhóm issue chính | Ví dụ rule SonarQube |
|------|------------------|----------------------|
| `python/vulnerabilities.py` | Vulnerability / Security Hotspot | SQL injection, OS command injection, hardcoded credentials, `eval`, weak hash (MD5), disable SSL verify |
| `python/bugs.py` | Bug | `is` với literal, hai vế toán tử trùng nhau, unreachable code, mutable default arg, điều kiện luôn đúng |
| `python/code_smells.py` | Code Smell | cognitive complexity cao, quá nhiều tham số, empty `except`, unused import/var, magic numbers, duplicate string literal, commented-out code |
| `python/duplicate_a.py` + `duplicate_b.py` | Duplications | khối code gần như giống hệt nhau |
| `javascript/vulnerabilities.js` | Vulnerability / Security Hotspot | SQLi, command injection, hardcoded creds, `eval`, DOM XSS (`innerHTML`), `Math.random()` làm token, `rejectUnauthorized: false` |
| `javascript/bugs.js` | Bug | `==` thay vì `===`, gán trong điều kiện, duplicate object key, unreachable, so sánh `NaN`, nhánh if/else trùng nhau |
| `javascript/codeSmells.js` | Code Smell | `var`, nested ternary, complexity cao, unused var, duplicate string literal, commented-out code |

## Cách chạy scan (tham khảo)

Yêu cầu: có `sonar-scanner` và một SonarQube server.

### Security check (BẮT BUỘC trước khi chạy)
- **Nơi lưu token**: biến môi trường `SONAR_TOKEN`, KHÔNG ghi vào file trong repo.
- **Ai truy cập được**: chỉ máy chạy scan / CI runner có secret.
- **Rotation/revocation**: thu hồi token trên SonarQube nếu lộ; tạo token mới phạm vi tối thiểu (project-level `Analyze`).
- **Đã commit vào git chưa?**: **No** - tuyệt đối không commit token.

### Linux / macOS (bash)

```bash
export SONAR_TOKEN="<YOUR_TOKEN>"   # Do not commit real secrets to git.
sonar-scanner \
  -Dsonar.host.url="https://<your-sonarqube-host>" \
  -Dsonar.token="$SONAR_TOKEN"
```

### Windows (PowerShell)

```powershell
$env:SONAR_TOKEN = "<YOUR_TOKEN>"   # Do not commit real secrets to git.
sonar-scanner `
  -D"sonar.host.url=https://<your-sonarqube-host>" `
  -D"sonar.token=$env:SONAR_TOKEN"
```

Các thông số `projectKey`, `sources`, encoding... được lấy từ `sonar-project.properties`.
