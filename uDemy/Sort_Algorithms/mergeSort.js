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
  let i = j = 0;
  while (A.length > i || B.length > j) {
    if (A.length === i) {
      C.push(B[j]);
      j++;
    } else if (B.length === j) {
      C.push(A[i]);
      i++;
    } else if (A[i] <= B[j]) {
      C.push(A[i]);
      i++;
    } else if (B[j] <= A[i]) {
      C.push(B[j]);
      j++;
    };
  };
  return C;
}

const nums = [4, 3, 5, 3, 43, 232, 4, 34, 232, 32, 4, 35, 34, 23, 2, 453, 546, 75, 67, 4342, 32];
console.log(mergeSort(nums)); // [2, 3, 3, 4, 4, 4, 5, 23, 32, 32, 34, 34, 35, 43, 67, 75, 232, 232, 453, 546, 4342]
console.log(mergeSort([0, -10, 7, 4, 9, 3])); // [-10, 0, 3, 4, 7, 9, 51]
console.log(mergeSort([0, 2, 34, 22, 10, 19, 17])); // [0, 2, 10, 17, 19, 22, 34]