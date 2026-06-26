// Các hàm đã được sửa đúng (đã làm sạch, không còn bug).

function checkStatus(code) {
  if (code === 200 || code === "200") {
    return "OK";
  }
  return "NOT OK";
}

function compute(value) {
  return value * 2;
}

function checkNaN(value) {
  if (Number.isNaN(value)) {
    return "là NaN";
  }
  return "không phải NaN";
}

const config = {
  timeout: 2000,
  retries: 3,
};

function doWork(n) {
  return n + 1;
}

function pickWork(flag) {
  return flag ? doWork(1) : doWork(2);
}

module.exports = { checkStatus, compute, checkNaN, config, doWork, pickWork };
