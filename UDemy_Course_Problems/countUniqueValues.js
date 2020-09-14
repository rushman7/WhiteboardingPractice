function countUniqueValues(arr) {
  if (arr.length < 2) return arr.length;
  let total = 1;

  for (let ptA =0;ptA<arr.length;ptA++) {
    let ptB = ptA + 1
    if (ptB >= arr.length) break;
    if (arr[ptA] != arr[ptB]) total++;
  }
  return total;
}

console.log(countUniqueValues([1,1,1,1,1,2]))
console.log(countUniqueValues([1,2,3,4,4,4,7,7,12,12,13]))
console.log(countUniqueValues([]))
console.log(countUniqueValues([-2,-1,-1,-0,1]))
