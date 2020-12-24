// Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


// In Pascal's triangle, each number is the sum of the two numbers directly above it.

// Example:

// Input: 5
// Output:
// [
//      [1],
//     [1,1],
//    [1,2,1],
//   [1,3,3,1],
//  [1,4,6,4,1]
// ]

var generate = function(numRows) {
  let res = [];
  for (let i=0;i<numRows;i++) res.push([]);
  
  for (let i=0;i<numRows;i++) {
      res[i][0] = 1;
      res[i][i] = 1;
      
      for (j=1;j<res[i].length-1;j++) res[i][j] = res[i-1][j-1] + res[i-1][j]
  }
  
  return res;
};