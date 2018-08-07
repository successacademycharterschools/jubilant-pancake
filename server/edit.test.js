const edit = require('./edit');

test('checks edit distance of `matt` and `ozzy`', () => {
  expect(editDistance("matt", "ozzy")).toBe(4);
});

test('checks edit distance of `hello` and `hello`', () => {
  expect(editDistance("hello", "hello")).toBe(0);
});

test('checks edit distance of `Success` and `Academy`', () => {
  expect(editDistance("Success", "Academy")).toBe(6);
});

test('checks edit distance of `matthew` and `MATTHEW`', () => {
  expect(editDistance("matthew", "MATTHEW")).toBe(7);
});
