// Quick sort
// Quick sort is an O(n * log(n)) algorithm (Worst case - O(n^2).
// Pivot is always the first element

function qHelper(arr, start=0, end=arr.length) {

  let amount = 0;
  for (let i=start+1;i<=end;i++) {
    if (arr[start] >= arr[i]) {
      amount++;
      [arr[i], arr[start+amount]] = [arr[start+amount], arr[i]];
    }
  }
  [arr[start], arr[start+amount]] = [arr[start+amount], arr[start]]
  return start+amount
}

function quickSort(arr, left=0, right=arr.length-1) {
  if (arr.length < 2 || left > right) return arr;

  let pivot = qHelper(arr, left, right)

  quickSort(arr, left, pivot-1, pivot)
  quickSort(arr, pivot+1, right, pivot)

  return arr;
}

const nums = [4, 3, 5, 3, 43, 232, 4, 34, 232, 32, 4, 35, 34, 23, 2, 453, 546, 75, 67, 4342, 32];
console.log(quickSort(nums)); // [2, 3, 3, 4, 4, 4, 5, 23, 32, 32, 34, 34, 35, 43, 67, 75, 232, 232, 453, 546, 4342]
console.log(quickSort([0, -10, 7, 4, 9, 3])); // [-10, 0, 3, 4, 7, 9, 51]
console.log(quickSort([10, 22, 34, 0, 2, 19])); // [0, 2, 10, 17, 19, 22, 34]
