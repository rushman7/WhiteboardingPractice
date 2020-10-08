// Selection Sort
// Selection sort is an O(n^2) algorithm.

function selectionSort(arr) {
  for (let i=0;i<arr.length-1;i++) {
    let min = i;
    for (let j=i;j<arr.length;j++) {
      if (arr[j] < arr[min]) min = j;
    };
    if (i !== min) [arr[i],arr[min]] = [arr[min],arr[i]];
  };
  return arr;
}

const nums = [4, 3, 5, 3, 43, 232, 4, 34, 232, 32, 4, 35, 34, 23, 2, 453, 546, 75, 67, 4342, 32];
console.log(selectionSort(nums)); // [2, 3, 3, 4, 4, 4, 5, 23, 32, 32, 34, 34, 35, 43, 67, 75, 232, 232, 453, 546, 4342]
console.log(selectionSort([0, -10, 7, 4, 9, 3])); // [-10, 0, 3, 4, 7, 9, 51]
console.log(selectionSort([0, 2, 34, 22, 10, 19, 17])); // [0, 2, 10, 17, 19, 22, 34]