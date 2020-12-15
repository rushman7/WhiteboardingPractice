// Given two sparse matrices A and B, return the result of AB.

// You may assume that A's column number is equal to B's row number.

// Example:

// Input:

// A = [
//   [ 1, 0, 0],
//   [-1, 0, 3]
// ]

// B = [
//   [ 7, 0, 0 ],
//   [ 0, 0, 0 ],
//   [ 0, 0, 1 ]
// ]

// Output:

//      |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
// AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
//                   | 0 0 1 |

var multiply = function(A, B) {
  let result = []
  for (i in A) result.push([])

  for (let i=0;i<A.length;i++) {
      let colB = 0;
      while (colB < B[0].length) {
          let sum = 0;
          for (let j=0;j<A[i].length;j++) sum += B[j][colB] * A[i][j];
          result[i][colB] = sum
          colB++;
      }
  }
  
  return result;
};