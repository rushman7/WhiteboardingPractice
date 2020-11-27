// Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.

// An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

// Example 1:

// Input: grid = [
//   ["1","1","1","1","0"],
//   ["1","1","0","1","0"],
//   ["1","1","0","0","0"],
//   ["0","0","0","0","0"]
// ]
// Output: 1
// Example 2:

// Input: grid = [
//   ["1","1","0","0","0"],
//   ["1","1","0","0","0"],
//   ["0","0","1","0","0"],
//   ["0","0","0","1","1"]
// ]
// Output: 3

var numIslands = function(grid) {
  let total = 0;
  let cache = {};
  
  for (let i=0;i<grid.length;i++) {
      for (let j=0;j<grid[i].length;j++) {
          if (grid[i][j] == '1') {
              total++;
              search(grid, i, j, cache);
          }
      }
  }
  return total
};

function search(grid, i, j, cache) {
grid[i][j] = '0';
if (j < grid[i].length-1) if (grid[i][j+1] == "1") search(grid, i, j+1); 
if (i < grid.length-1) if (grid[i+1][j] == "1") search(grid, i+1, j); 
if (j > 0) if (grid[i][j-1] == "1") search(grid, i, j-1); 
if (i > 0) if (grid[i-1][j] == "1") search(grid, i-1, j); 
}