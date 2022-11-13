const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];

function unija(arr1, arr2) {
  const newArray = [];
  arr1.reduce((elem) => newArray.push(elem));
  //   arr2.reduce((elem) => newArray.push(elem));
  return newArray;
}

console.log(unija(arr1, arr2));
