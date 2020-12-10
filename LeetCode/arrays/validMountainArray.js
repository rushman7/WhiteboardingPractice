// Given an array of integers arr, return true if and only if it is a valid mountain array.

// Recall that arr is a mountain array if and only if:

// arr.length >= 3
// There exists some i with 0 < i < arr.length - 1 such that:
// arr[0] < arr[1] < ... < arr[i - 1] < A[i]
// arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

var validMountainArray = function(arr) {
  if (arr.length < 3) return false;
  if (arr[0] > arr[1]) return false;
  if (arr[arr.length-1] > arr[arr.length-2]) return false;
  
  let pivot = false;
  
  for (let i=0;i<arr.length-1;i++) {
      if (pivot) {
          if (arr[i] < arr[i+1]) return false;
          if (arr[i] == arr[i+1]) return false;
      } else {
          if (arr[i] > arr[i+1]) pivot = true;
          if (arr[i] == arr[i+1]) return false;
      }
  }

  return pivot ? true : false
};