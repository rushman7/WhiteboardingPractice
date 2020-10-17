class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

class Queue {
  constructor() {
    this.head = null;
    this.tail = null;
    this.size = 0;
  }

  enqueue(val) {
    let node = new Node(val);
    if (!this.size) this.head = this.tail = node;
    else {
      this.tail.next = node;
      this.tail = node;
    }

    this.size++
    return this;
  }

  dequeue() {
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


const queue = new Queue();

queue.enqueue(5).enqueue(10).enqueue(15).enqueue(20).enqueue(25).dequeue()
queue.print()
