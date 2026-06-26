module.exports = {
  testEnvironment: "node",
  // Chi do coverage cho code trong javascript/
  collectCoverage: true,
  collectCoverageFrom: ["javascript/**/*.js"],
  coverageDirectory: "coverage",
  // lcov de Sonar doc (qua sonar.javascript.lcov.reportPaths), text de xem tren CI log
  coverageReporters: ["lcov", "text"],
  // Test nam trong tests/js de tach khoi source
  testMatch: ["**/tests/js/**/*.test.js"],
};
