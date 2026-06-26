// Demo các lỗi Bug (reliability) mà SonarQube phát hiện.

function checkStatus(code) {
  // Bug: dùng == thay vì === (loose equality)
  if (code == "200") {
    return "OK";
  }
  return "NOT OK";
}

function assignInCondition(x) {
  // Bug: gán trong điều kiện thay vì so sánh
  if ((x = 5)) {
    return "luôn đúng";
  }
  return "không bao giờ";
}

const config = {
  // Bug: key trùng lặp trong object literal
  timeout: 1000,
  retries: 3,
  timeout: 2000,
};

function compute(value) {
  // Bug: code không bao giờ chạy sau return (unreachable)
  return value * 2;
  console.log("đã tính xong");
}

function checkNaN(value) {
  // Bug: so sánh trực tiếp với NaN luôn false
  if (value === NaN) {
    return "là NaN";
  }
  return "không phải NaN";
}

function identicalBranches(flag) {
  // Bug: hai nhánh if/else giống hệt nhau
  if (flag) {
    return doWork(1);
  } else {
    return doWork(1);
  }
}

function doWork(n) {
  return n + 1;
}

module.exports = {
  checkStatus,
  assignInCondition,
  config,
  compute,
  checkNaN,
  identicalBranches,
};
