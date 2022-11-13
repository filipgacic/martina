function cbf(elem) {
  if (elem > 2) return elem;
}
const array = [1, 2, 3, 4];

function filter(array, cbf) {
  const newArray = [];
  array.forEach((element) => {
    if (cbf(element)) newArray.push(element);
  });
  return newArray;
}

console.log(filter(array, cbf));
