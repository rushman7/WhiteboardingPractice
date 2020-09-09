// Linear Search
// Write a function called linearSearch which accepts an array and a value,
// and returns the index at which the value exists.
// If the value does not exist in the array, return -1.
// Don't use indexOf to implement this function!

// Time Complexity - O(n)

function linearSearch(arr, val) {
  for (i in arr) {
    if (arr[i] == val) return arr[i]
  }
  return -1
}

console.log(linearSearch(['a',1,'b','c'], '2')) // false
console.log(linearSearch([1,2,3,4], 3)) // true