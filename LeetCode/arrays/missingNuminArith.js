// In some array arr, the values were in arithmetic progression: the values arr[i+1] - arr[i] are all equal for every 0 <= i < arr.length - 1.

// Then, a value from arr was removed that was not the first or last value in the array.

// Return the removed value.

var missingNumber = function(arr) {
  let val = (arr[arr.length-1]-arr[0])/arr.length;
  for (let i=0;i<arr.length-1;i++) {
      if (arr[i+1] == arr[i]) return arr[i]
      if (arr[i+1] - arr[i] != val) return arr[i] + val
  }
};