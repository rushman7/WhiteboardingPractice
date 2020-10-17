class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

class Stack {
  constructor(val) {
    this.head = null;
    this.tail = null;
    this.size = 0;
  }

  push(val) {
    let node = new Node(val);
    if (!this.size) this.head = this.tail = node;
    else {
      node.next = this.head;
      this.head = node;
    }

    this.size++
    return this;
  }

  pop() {
    if (!this.size) return null;

    if (this.head == this.tail) this.head = this.tail = null;
    else this.head = this.head.next;

    this.size--
    return this;
  }

  print() { 
    let arr = [];
    let curr = this.head;
    while (curr) {
      arr.push(curr.val)
      curr=curr.next
    }
    console.log(arr)
  }
}


const stack = new Stack();

stack.push(5).push(10).push(15).push(20).push(25).pop()
stack.print()
