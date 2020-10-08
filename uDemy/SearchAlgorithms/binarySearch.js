// Binary Search
// Write a function called binarySearch which accepts a sorted array and
// a value and returns the index at which the value exists. Otherwise, return -1.

// Time Complexity - O(log n)

function binarySearch(arr, val) {
  let min = 0;
  let max = arr.length-1;

  while (min <= max) {
    let mid = Math.floor((max+min)/2);
    console.log(min,max,mid)
    if (val > arr[mid]) min = mid+1;
    else if (val < arr[mid]) max = mid-1;
    else return val;
  }

  return -1
}

console.log(binarySearch([1,2,3,4,5,6,7], 6)) // 6
console.log(binarySearch([2,4,6,8,10], 3)) // -`