// An axis-aligned rectangle is represented as a list [x1, y1, x2, y2], 
// where (x1, y1) is the coordinate of its bottom-left corner, 
// and (x2, y2) is the coordinate of its top-right corner. 
// Its top and bottom edges are parallel to the X-axis, 
// and its left and right edges are parallel to the Y-axis.

// Two rectangles overlap if the area of their intersection is positive. 
// To be clear, two rectangles that only touch at the corner or edges do not overlap.

// Given two axis-aligned rectangles rec1 and rec2, 
// return true if they overlap, otherwise return false.

function rectangleOverlap(rec1, rec2) {

}

// console.log(rectangleOverlap([0,0,2,3], [1,1,3,3])) // true
// console.log(rectangleOverlap([0,0,2,3], [0,0,-2,-2])) // false
// console.log(rectangleOverlap([2,1,4,3], [0,0,2,2])) // true
// console.log(rectangleOverlap([0,0,1,1], [1,0,2,1])) // false
// console.log(rectangleOverlap([0,0,1,1], [2,2,3,3])) // false
// console.log(rectangleOverlap([5,15,8,18], [0,3,7,9])) // false