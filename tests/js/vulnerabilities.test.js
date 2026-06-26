// Test cho javascript/vulnerabilities.js (da lam sach) de tang coverage.

const crypto = require("crypto");
const {
  getApiKey,
  getUser,
  strongHash,
  generateToken,
} = require("../../javascript/vulnerabilities");

test("getApiKey doc tu env", () => {
  process.env.API_KEY = "abc";
  expect(getApiKey()).toBe("abc");
});

test("getUser dung query tham so hoa", () => {
  const calls = [];
  const db = {
    query: (sql, params) => {
      calls.push([sql, params]);
      return "ok";
    },
  };
  expect(getUser(db, "alice")).toBe("ok");
  expect(calls[0][1]).toEqual(["alice"]);
});

test("strongHash khop sha256", () => {
  const expected = crypto.createHash("sha256").update("x").digest("hex");
  expect(strongHash("x")).toBe(expected);
});

test("generateToken tra ve 32 ky tu hex", () => {
  expect(generateToken()).toMatch(/^[0-9a-f]{32}$/);
});
