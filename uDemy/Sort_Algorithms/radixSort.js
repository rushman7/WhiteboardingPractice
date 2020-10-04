// Radix Sort

// Radix Sort Helper function - getDigit
// Implement a function called getDigit which accepts a positive integer and
// a position, and returns the digit in that number at the given position.
// The position reads from right to left, so the 0th position corresponds to the rightmost digit.

// Radix Sort Helper - digitCount
// Implement a function called digitCount which accepts a positive integer and
// returns the number of digits that the integer has.

// Radix Sort Helper - mostDigits
// Implement a function called mostDigits which accepts an array of integers and
// returns a count of the number of digits for the number in the array with the most digits.

// Radix Sort function - radixSort
// Write a function called radixSort which accepts an array of numbers and
// sorts them in ascending order.

function getDigit(num, n) {
  return Math.floor((num / Math.pow(10, n) % 10))
}

function digitCount(num) { 
  if (num === 0) return 1;
  return Math.ceil(Math.log10(Math.abs(num)));
}

function mostDigits(arr) { 
  let max = 0;
  for (i in arr) {
    let temp = digitCount(arr[i]);
    if (max < temp) max = temp;
  }
  return max;
}

function radixSort(arr) {
  let largest = mostDigits(arr);

  for (let k=0;k<largest;k++) {
    let bucket = Array.from({length: 10}, () => []);
    for (let i=0;i<arr.length;i++) {
      let digit = getDigit(arr[i], k)
      bucket[digit].push(arr[i])
    }
    arr = [].concat(...bucket);
  }

  return arr;
}

const nums = [4, 3, 5, 3, 43, 232, 4, 34, 232, 32, 4, 35, 34, 23, 2, 453, 546, 75, 67, 4342, 32];
console.log(radixSort(nums)); // [2, 3, 3, 4, 4, 4, 5, 23, 32, 32, 34, 34, 35, 43, 67, 75, 232, 232, 453, 546, 4342]
console.log(radixSort([130, 10541, 42, 415, 31, 3])); // [0, 3, 4, 7, 9, 51, 10]
console.log(radixSort([10, 22, 34, 0, 2, 19])); // [0, 2, 10, 17, 19, 22, 34]
