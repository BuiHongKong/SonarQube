// Test cho javascript/codeSmells.js - cover cac ham thuan de sinh coverage.

const {
  process: proc,
  grade,
  repeatedLiterals,
  unusedVariables,
} = require("../../javascript/codeSmells");

test("grade tra ve A khi diem cao", () => {
  expect(grade(95)).toBe("A");
});

test("grade tra ve B", () => {
  expect(grade(85)).toBe("B");
});

test("grade tra ve C", () => {
  expect(grade(75)).toBe("C");
});

test("grade tra ve D", () => {
  expect(grade(65)).toBe("D");
});

test("grade tra ve F khi diem thap", () => {
  expect(grade(10)).toBe("F");
});

test("repeatedLiterals tra ve connection failed", () => {
  expect(repeatedLiterals()).toBe("connection failed");
});

test("unusedVariables tra ve 42", () => {
  expect(unusedVariables()).toBe(42);
});

test("process mode mac dinh", () => {
  expect(proc([1], "c")).toBe(5);
});

test("process mode b", () => {
  expect(proc([1], "b")).toBe(4);
});
