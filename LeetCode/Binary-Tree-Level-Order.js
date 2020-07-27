// Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

// For example:
// Given binary tree [3,9,20,null,null,15,7],
//     3
//    / \
//   9  20
//     /  \
//    15   7
// return its level order traversal as:
// [
//   [3],
//   [9,20],
//   [15,7]
// ]

var levelOrder = function(root) {
  let lists = [];
  add(lists, root, 0)
  
  return lists;
};

function add(lists, node, depth) {
  if (node) {
      if (!lists[depth]) {
          lists[depth] = [];
      }
      
      lists[depth].push(node.val)
      
      add(lists, node.left, depth+1);
      add(lists, node.right, depth+1);
  }
}