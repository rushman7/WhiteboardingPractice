class Node {
  constructor(data, left=null, right=null) {
    this.data = data;
    this.left = left;
    this.right = right;
  }

  insert(data) {
    let node = new Node(data);

    if (this.data >= node.data) {
      if (!this.left) this.left = node;
      else this.left.insert(node.data)
    } else {
      if (!this.right) this.right = node;
      else this.right.insert(node.data)
    }
  };

  print(node, result=[]) {
    if (node) {
      if (node.left) node.print(node.left, result)
      result.push(node)
      if (node.right) node.print(node.right, result)
    }
    return result
  }

  find(data) {
    if (this.data === data) return this
    else {
      if (this.data > data && this.left) return this.left.find(data)
      else if (this.data < data && this.right) return this.right.find(data)
    }

    return null
  };

  delete(data) {
    let node = this.find(data)
    console.log(node.data)
    if (node) {
      if (node.right) {
        let temp = node.right;
        node.right = node.right.right;
        node.data = temp.data
      }
      else if (node.left) {
        let temp = node.left;
        node.left = node.left.left;
        node.data = temp.data
      }
    } else return 'Node does not exist'
  }

  randomNode(node) {
    if (this.print(node).length > 0) {
      return this.print(node)[Math.floor(Math.random() * Math.floor((this.print(node).length-1)))]
    } 
    return 'No nodes in tree'
  }
};