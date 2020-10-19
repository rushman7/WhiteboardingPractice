class BinarySearchTree {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }

  insert(value) {
    let node = new BinarySearchTree(value);
    
    if (!this.value) this.value = node;

    if (value > this.value) {
      if (this.right) this.right.insert(value);
      else this.right = node;
    } else if (value < this.value) {
      if (this.left) this.left.insert(value);
      else this.left = node;
    }
  }

  contains(target) {
    if (target == this.value) return true;

    if (target < this.value) {
      if (this.left) return this.left.contains(target);
      else return false;
    }
    if (target > this.value) {
      if (this.right) return this.right.contains(target);
      else return false;
    }
  }

  DFSPrint() {
    let visited = [];
    let curr = this;

    function DFS(node) {
      // visited.push(node.value); // pre order
      if (node.left) DFS(node.left);
      // visited.push(node.value); // in order
      if (node.right) DFS(node.right);
      visited.push(node.value); // post order
    }

    DFS(curr)

    return visited;
  }

  BFSPrint() {
    if (!this.value) return null;
    let queue = [this];
    let visited = [];

    while (queue.length) {
      let curr = queue.shift()
      visited.push(curr.value);
      if (curr.left) queue.push(curr.left);
      if (curr.right) queue.push(curr.right);
    }
    return visited;
  }
}

const BST = new BinarySearchTree(10);

BST.insert(6)
BST.insert(15)
BST.insert(20)
BST.insert(3)
BST.insert(8)
console.log(BST.DFSPrint());
console.log(BST.BFSPrint());
// console.log(BST);

/** 
 *     10
 *   6   15
 * 3  8    20
*/
