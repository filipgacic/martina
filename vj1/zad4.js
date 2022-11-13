function fn1(val) {
  return val * 2;
}
function fn2(val) {
  return val + 2;
}
const broj = 5;

function komutativnost(fn1, fn2, broj) {
  if (fn1(fn2(broj)) === fn2(fn1(broj))) return true;
  else return false;
}
console.log(komutativnost(fn1, fn2, broj));
