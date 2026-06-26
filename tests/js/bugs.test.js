// Test cho javascript/bugs.js - cover cac ham thuan de sinh coverage.

const {
  checkStatus,
  compute,
  checkNaN,
  identicalBranches,
  config,
} = require("../../javascript/bugs");

test("checkStatus tra ve OK khi == '200'", () => {
  expect(checkStatus("200")).toBe("OK");
});

test("checkStatus tra ve NOT OK voi gia tri khac", () => {
  expect(checkStatus(404)).toBe("NOT OK");
});

test("compute nhan doi gia tri", () => {
  expect(compute(3)).toBe(6);
});

test("checkNaN luon tra ve khong phai NaN (bug so sanh === NaN)", () => {
  expect(checkNaN(NaN)).toBe("không phải NaN");
});

test("identicalBranches luon tra ve 2", () => {
  expect(identicalBranches(true)).toBe(2);
  expect(identicalBranches(false)).toBe(2);
});

test("config giu gia tri key trung cuoi cung (bug duplicate key)", () => {
  expect(config.timeout).toBe(2000);
});
