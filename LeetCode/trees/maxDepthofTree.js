// Given the root of a binary tree, return its maximum depth.

// A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

var maxDepth = function(root) {
  if (!root) return 0;
  if (!root.left) return maxDepth(root.right)+1;
  if (!root.right) return maxDepth(root.left)+1;
  
  return Math.max(maxDepth(root.left), maxDepth(root.right))+1
};