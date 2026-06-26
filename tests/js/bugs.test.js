// Test cho javascript/bugs.js (da lam sach) - cover de sinh coverage.

const {
  checkStatus,
  compute,
  checkNaN,
  pickWork,
  config,
} = require("../../javascript/bugs");

test("checkStatus tra ve OK khi code la 200", () => {
  expect(checkStatus("200")).toBe("OK");
});

test("checkStatus tra ve NOT OK voi gia tri khac", () => {
  expect(checkStatus(404)).toBe("NOT OK");
});

test("compute nhan doi gia tri", () => {
  expect(compute(3)).toBe(6);
});

test("checkNaN nhan dien NaN dung", () => {
  expect(checkNaN(NaN)).toBe("là NaN");
});

test("checkNaN voi so binh thuong", () => {
  expect(checkNaN(5)).toBe("không phải NaN");
});

test("pickWork chon nhanh theo flag", () => {
  expect(pickWork(true)).toBe(2);
  expect(pickWork(false)).toBe(3);
});

test("config co timeout 2000", () => {
  expect(config.timeout).toBe(2000);
});
