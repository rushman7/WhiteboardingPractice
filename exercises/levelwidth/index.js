// --- Directions
// Given the root node of a tree, return
// an array where each element is the width
// of the tree at each level.
// --- Example
// Given:
//     0
//   / |  \
// 1   2   3
// |       |
// 4       5
// Answer: [1, 3, 2]

function levelWidth(root) {
  let counters = [0];
  let arr = [root, 's'];

  while (arr.length > 1) {
    const node = arr.shift();
    arr.push(...node.children);
    counters[counters.length - 1] += 1;

    if (arr[0] === 's' && arr.length > 1) {
      arr.push(arr.shift());
      counters.push(0);
    }
  }

  return counters;
}

module.exports = levelWidth;
