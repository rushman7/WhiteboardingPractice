// A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

// The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

// Now consider if some obstacles are added to the grids. How many unique paths would there be?



// An obstacle and empty space is marked as 1 and 0 respectively in the grid.

// Note: m and n will be at most 100.

// Example 1:

// Input:
// [
//   [0,0,0],
//   [0,1,0],
//   [0,0,0]
// ]
// Output: 2
// Explanation:
// There is one obstacle in the middle of the 3x3 grid above.
// There are two ways to reach the bottom-right corner:
// 1. Right -> Right -> Down -> Down
// 2. Down -> Down -> Right -> Right

var uniquePathsWithObstacles = function(grid) {
  for (r in grid) {
      for (c in grid[0]) {
          if (r==0 && c==0 && grid[r][c] == 1) return 0;
          else if (r==0 && c==0 && grid[r][c] == 0) grid[r][c] = 1 
          else if (grid[r][c] == 1) grid[r][c] = 0;
          else if (grid[r][c] == 0) {
              if (r-1 < 0) grid[r][c] = 0 + grid[r][c-1];
              else if (c-1 < 0) grid[r][c] = 0 + grid[r-1][c];
              else grid[r][c] = grid[r-1][c] + grid[r][c-1];
          }
      }
  }
  return grid[grid.length-1][grid[0].length-1]
};
