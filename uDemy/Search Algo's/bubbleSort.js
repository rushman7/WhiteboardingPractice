// Bubble Sort
// Bubble sort is an O(n^2) algorithm.

function bubbleSort(arr) {
  let noSwaps;
  for (let i=arr.length-1;i>0;i--) {
    noSwaps = true;
    for (let j=0;j<=i-1;j++) {
      if (arr[j] > arr[j+1]) {
        [arr[j],arr[j+1]] = [arr[j+1], arr[j]] 
        noSwaps = false;
      }
    }
    if (noSwaps) break;
  }
  return arr
}

const nums = [4, 3, 5, 3, 43, 232, 4, 34, 232, 32, 4, 35, 34, 23, 2, 453, 546, 75, 67, 4342, 32];
console.log(bubbleSort(nums)); // [2, 3, 3, 4, 4, 4, 5, 23, 32, 32, 34, 34, 35, 43, 67, 75, 232, 232, 453, 546, 4342]
console.log(bubbleSort([0, -10, 7, 4, 9, 51])); // [-10, 0, 4, 7, 9, 51]