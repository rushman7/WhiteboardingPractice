// Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

// Note:

// Given target value is a floating point.
// You are guaranteed to have only one unique value in the BST that is closest to the target.
// Example:

// Input: root = [4,2,5,1,3], target = 3.714286

//     4
//    / \
//   2   5
//  / \
// 1   3

// Output: 4

var closestValue = function(root, target) {
  let closest = root.val;
  
  while (root) {
      closest = Math.abs(closest-target) > Math.abs(root.val-target) ? root.val : closest;
      root = root.val > target ? root.left : root.right;
  }
  
  return closest
};