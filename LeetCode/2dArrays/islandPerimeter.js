// You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

// Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

// The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

var islandPerimeter = function(grid) {
  let res = 0;
  let l,r,t,b;
  for (let i=0;i<grid.length;i++) {
      for (let j=0;j<grid[i].length;j++) {
          if (grid[i][j] == 1) {
              if (i == 0) t = 0;
              else t = grid[i-1][j];
              
              if (j == 0) l = 0;
              else l = grid[i][j-1];
              
              if (i == grid.length-1) b = 0;
              else b = grid[i+1][j];
              
              if (j == grid[i].length-1) r = 0;
              else r = grid[i][j+1]

              res += (4 - l - r - t - b)
          }
      }
  }
  
  return res;
};