// --- Directions
// Given an array and chunk size, divide the array into many subarrays
// where each subarray is of length size
// --- Examples
// chunk([1, 2, 3, 4], 2) --> [[ 1, 2], [3, 4]]
// chunk([1, 2, 3, 4, 5], 2) --> [[ 1, 2], [3, 4], [5]]
// chunk([1, 2, 3, 4, 5, 6, 7, 8], 3) --> [[ 1, 2, 3], [4, 5, 6], [7, 8]]
// chunk([1, 2, 3, 4, 5], 4) --> [[ 1, 2, 3, 4], [5]]
// chunk([1, 2, 3, 4, 5], 10) --> [[ 1, 2, 3, 4, 5]]

// function chunk(array, size) {
//   const chunked_arr = [];

//   for (let i = 0; i < array.length; i++) {
//     // setting the last element of array equal to last
//     const last = chunked_arr[chunked_arr.length - 1];
//     // if it doest not exist or if the amount of elements is equal to size:
//     if (!last || last.length === size) {
//     // add the chunked array into the current index of array once it reaches size
//       chunked_arr.push([array[i]]);
//     } else {
//     // if there is no chunks left add last (less than size) to end of array
//       last.push(array[i]);
//     }
//   }
//   return chunked_arr;
// }

function chunk(array, size) {
  const chunked_arr = [];
  let index = 0;

  while (index < array.length) {
    chunked_arr.push(array.slice(index, index + size));
    index += size;
  }

  return chunked_arr;
}


module.exports = chunk;


