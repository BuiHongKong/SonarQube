// Demo các lỗi Code Smell (maintainability) mà SonarQube phát hiện.

function process(data, mode, level, retry, verbose, flag) {
  // Code smell: quá nhiều tham số + cognitive complexity cao
  var result = 0; // Code smell: dùng 'var' thay vì let/const
  for (var i = 0; i < data.length; i++) {
    if (mode === "a") {
      if (level > 1) {
        if (retry) {
          if (verbose) {
            for (var j = 0; j < i; j++) {
              if (flag) {
                result += i * j;
              } else {
                result -= j;
              }
            }
          } else {
            result += 1;
          }
        } else {
          result += 2;
        }
      } else {
        result += 3;
      }
    } else if (mode === "b") {
      result += 4;
    } else {
      result += 5;
    }
  }
  return result;
}

function grade(score) {
  // Code smell: nested ternary khó đọc
  return score > 90 ? "A" : score > 80 ? "B" : score > 70 ? "C" : score > 60 ? "D" : "F";
}

function repeatedLiterals() {
  // Code smell: chuỗi lặp lại nhiều lần (duplicate string literal)
  log("connection failed");
  log("connection failed");
  log("connection failed");
  save("connection failed");
  return "connection failed";
}

function unusedVariables() {
  // Code smell: biến khai báo nhưng không sử dụng
  var total = 100;
  var name = "demo";
  var temp = total + 1;
  return 42;
}

// Code smell: code bị comment lại (commented-out code)
// function oldFunction(x) {
//   return x + 1;
// }

// TODO: refactor module này

function log(message) {
  console.log(message);
}

function save(message) {
  console.log("saved:", message);
}

module.exports = { process, grade, repeatedLiterals, unusedVariables };
