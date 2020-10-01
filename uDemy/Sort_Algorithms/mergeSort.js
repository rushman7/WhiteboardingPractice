// Merge sort (merge function modifies passed parameters)
// Merge sort is an O(n * log(n)) algorithm.

function mergeSort(arr) {
  if (arr.length < 2) return arr;
  let mid = Math.floor(arr.length/2);
  let A = mergeSort(arr.slice(0, mid))
  let B = mergeSort(arr.slice(mid))
  let merged = merge(A,B);
  return merged;
}

function merge(A, B) {
  let C = [];
  while (A.length > 0 || B.length > 0) {
    if (A.length === 0) {
      C.push(B[0])
      B.shift()
    } else if (B.length === 0) {
      C.push(A[0])
      A.shift()
    } else if (A[0] <= B[0]) {
      C.push(A[0])
      A.shift()
    } else if (B[0] <= A[0]) {
      C.push(B[0])
      B.shift()
    }
  }
  return C;
}

const nums = [4, 3, 5, 3, 43, 232, 4, 34, 232, 32, 4, 35, 34, 23, 2, 453, 546, 75, 67, 4342, 32];
console.log(mergeSort(nums)); // [2, 3, 3, 4, 4, 4, 5, 23, 32, 32, 34, 34, 35, 43, 67, 75, 232, 232, 453, 546, 4342]
console.log(mergeSort([0, -10, 7, 4, 9, 3])); // [-10, 0, 3, 4, 7, 9, 51]
console.log(mergeSort([0, 2, 34, 22, 10, 19, 17])); // [0, 2, 10, 17, 19, 22, 34]