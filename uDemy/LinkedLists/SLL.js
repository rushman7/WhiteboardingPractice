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
    if (!this.length) return `List is Empty`;

    let curr = this.head;

    while (curr.next) {
      if (curr.next === this.tail) {
        curr.next = null;
        this.tail = curr;
      } else curr = curr.next;
    }

    this.length--
    if (!this.length) this.head = this.tail = null;
    return this;
  }

  shift() {
    if (!this.length) return `List is Empty`;

    this.head = this.head.next;

    this.length--
    if (!this.length) this.head = this.tail = null;
    return this;
  }
  unshift(val) {
    let node = new Node(val);
    if (!this.length) this.head = this.tail = node
    else {
      node.next = this.head;
      this.head = node;
    }

    this.length++
    return this;
  }
  get(num) {
    let i = 0;
    let curr = this.head;

    while (i < num && curr) {
      i++
      curr = curr.next
    }

    return curr ? curr : 'Does not exist.';
  }
}

const SLL = new SinglyLinkedList();

SLL.push(5)
SLL.push(10)
SLL.push(15)
SLL.unshift(20)
// SLL.push(20)
// SLL.pop()
// SLL.shift()
console.log(SLL)
console.log(SLL.get(10))
console.log(SLL.get(1))