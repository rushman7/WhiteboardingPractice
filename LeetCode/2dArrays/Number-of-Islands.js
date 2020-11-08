// Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

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
  
  for (r in grid) {
      for (c in grid[0]) {
          if (grid[r][c] == 1) {
              total += 1
              search(grid,Number(r), Number(c))
          }
      }
  }
  return total;
};

function search(grid,r,c) {
  grid[r][c] = 0;
  if (r-1 >= 0 && grid[r-1][c] == 1) search(grid,r-1,c);
  if (r+1 < grid.length && grid[r+1][c] == 1) search(grid,r+1,c);
  if (c-1 >= 0 && grid[r][c-1] == 1) search(grid,r,c-1);
  if (c+1 < grid[0].length && grid[r][c+1] == 1) search(grid,r,c+1);
  return
}