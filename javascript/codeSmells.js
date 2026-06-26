// Các hàm đã được làm sạch (không còn code smell).

const CONNECTION_FAILED = "connection failed";
const INCREMENT_BY_MODE = { a: 1, b: 4 };
const DEFAULT_INCREMENT = 5;

function process(data, mode) {
  const increment = INCREMENT_BY_MODE[mode] || DEFAULT_INCREMENT;
  return data.length * increment;
}

function grade(score) {
  if (score > 90) {
    return "A";
  }
  if (score > 80) {
    return "B";
  }
  if (score > 70) {
    return "C";
  }
  if (score > 60) {
    return "D";
  }
  return "F";
}

function repeatedLiterals() {
  return CONNECTION_FAILED;
}

function unusedVariables() {
  return 42;
}

module.exports = { process, grade, repeatedLiterals, unusedVariables };
