// Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

// Note: You can only move either down or right at any point in time.

 

// Example 1:


// Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
// Output: 7
// Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
// Example 2:

// Input: grid = [[1,2,3],[4,5,6]]
// Output: 12

var minPathSum = function(grid) { 
  for (let i=0;i<grid.length;i++) {
      for (let j=0;j<grid[i].length;j++) {
          if (!(j == 0 && i == 0)) {
              let left = i > 0 ? grid[i-1][j] : Infinity;
              let up = j > 0 ? grid[i][j-1] : Infinity;
              grid[i][j] = Math.min((grid[i][j] + left), (grid[i][j] + up))
          }
      }
  }
  
  return grid[grid.length-1][grid[grid.length-1].length-1]
};