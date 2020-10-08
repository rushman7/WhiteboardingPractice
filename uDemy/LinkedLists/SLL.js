class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

class SinglyLinkedList{
  constructor() {
    this.length = 0;
    this.head = null;
    this.tail = null;
  }

  push(val) {
    let node = new Node(val);

    if (!this.length) this.head = this.tail = node
    else this.tail.next =  this.tail = node;

    this.length++
    return this;
  }

  pop() {
    if (!this.length) return this;

    this.length--
    if (this.head === this.tail) return this.head = this.tail = null;

    let curr = this.head;

    while (curr.next) {
      if (curr.next === this.tail) {
        curr.next = null;
        this.tail = curr;
      } else curr = curr.next;
    }
    
    return this;
  }
}

const SLL = new SinglyLinkedList();

SLL.push(5)
SLL.push(10)
SLL.push(15)
SLL.push(20)
SLL.push(25)
SLL.push(30)
SLL.pop()
SLL.pop()
console.log(SLL, SLL.head.next.next)

// SLL.print(); // [ 5, 10, 15, 20, 25, 30 ]
// SLL.pop();
// SLL.print(); // [ 5, 10, 15, 20, 25 ]
// SLL.unshift(1);
// SLL.print(); // [ 1, 5, 10, 15, 20, 25 ]
// SLL.shift();
// SLL.print(); // [ 5, 10, 15, 20, 25 ]
// console.log(SLL.get(2).data); // 15
// SLL.set(2, 100);
// console.log(SLL.get(2).data); // 100
// SLL.insert(3, 10000);
// SLL.print(); // [ 5, 10, 100, 10000, 20, 25 ]
// SLL.remove(3);
// SLL.print(); // [ 5, 10, 100, 20, 25 ]
// SLL.reverse();
// SLL.print(); // [ 25, 20, 100, 10, 5 ]
// SLL.rotate(-2);
// SLL.print(); // [ 10, 5, 25, 20, 100 ]
// console.log(SLL.find(25, true)); // 2