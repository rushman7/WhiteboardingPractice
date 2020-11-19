class TreeNode {
  constructor(val, left=null, right=null) {
    this.val = val;
    this.left = left;
    this.right = right;
  }
}

function inOrderBST(node, result=[]) {
  if (node.left) inOrderBST(node.left, result)
  if (node) result.push(node.val)
  if (node.right) inOrderBST(node.right, result)
  return result;
}

function insert(tree, node) {
  if (tree.val > node.val) {
    if (!tree.left) tree.left = node;
    else insert(tree.left, node);
  } else {
    if (!tree.right) tree.right = node;
    else insert(tree.right, node);
  }
}

function sortBST(arr) {
  let mid = Math.floor((arr.length-1)/2);
  let res = [arr[mid]];
  function split(arr1, arr2) {
    if (!arr1.length && !arr2.length) return;
    let mid1 = Math.floor((arr1.length-1)/2);
    let mid2 = Math.floor((arr2.length-1)/2)
    if (arr1.length) res.push(arr1[mid1]);
    if (arr2.length) res.push(arr2[mid2]);

    if (arr1.length > 0) split(arr1.slice(0,mid1), arr1.slice(mid1+1))
    if (arr2.length > 0) split(arr2.slice(0,mid2), arr2.slice(mid2+1))
  }
  split(arr.slice(0,mid), arr.slice(mid+1))

  return res
} 

function balanceBST(root) {
  let arr = inOrderBST(root);
  arr = sortBST(arr).reverse();
  let newTree = new TreeNode(arr.pop());

  while (arr.length > 0) {
    let node = new TreeNode(arr.pop());
    insert(newTree, node)
  }
  
  return newTree;
}

let tree = new TreeNode(14);
tree.left = new TreeNode(9);
tree.left.right = new TreeNode(13);
tree.left.left = new TreeNode(2);
tree.right = new TreeNode(16);

// let tree = new TreeNode(1);
// tree.right = new TreeNode(2);
// tree.right.right = new TreeNode(3);
// tree.right.right.right = new TreeNode(4);


console.log(balanceBST(tree)); 