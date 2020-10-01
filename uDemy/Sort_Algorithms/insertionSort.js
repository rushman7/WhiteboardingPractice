// Insertion Sort
// Insertion sort is an O(n^2) algorithm.

function insertionSort(arr) {
  for (let i = 1;i<arr.length;i++) {
    let j = i;

    while (arr[j] < arr[j-1]) {
      [arr[j],arr[j-1]] = [arr[j-1], arr[j]] 
      j--
    }
  }
  return arr
}

const nums = [4, 3, 5, 3, 43, 232, 4, 34, 232, 32, 4, 35, 34, 23, 2, 453, 546, 75, 67, 4342, 32];
console.log(insertionSort(nums)); // [2, 3, 3, 4, 4, 4, 5, 23, 32, 32, 34, 34, 35, 43, 67, 75, 232, 232, 453, 546, 4342]
console.log(insertionSort([0, -10, 7, 4, 9, 3])); // [-10, 0, 3, 4, 7, 9, 51]
console.log(insertionSort([0, 2, 34, 22, 10, 19, 17])); // [0, 2, 10, 17, 19, 22, 34]
