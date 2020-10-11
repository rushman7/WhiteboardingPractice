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

  get(index) {
    if (index < 0 || index > this.length) return null;
    let i = 0;
    let curr = this.head;

    while (i < index) {
      i++
      curr = curr.next
    }

    return curr;
  }

  set(index, val) {
    if (index < 0 || index > this.length) return null;
    let node = this.get(index);
    node.val = val;
    return node;
  }

  insert(index, val) {
    if (index < 0 || index > this.length) return null;
    if (index === this.length-1) return this.push(val);
    if (index === 0) return this.unshift(val);
    let node = new Node(val);
    let curr = this.get(index-1)
 
    node.next = curr.next;
    curr.next = node;
    this.length++
    return node;
  }

  remove(index) { 
    if (index < 0 || index > this.length) return null;
    if (index === this.length-1) return this.pop();
    if (index === 0) return this.shift();

    let prev = this.get(index-1);
    prev.next = prev.next.next;
    this.length--
    return this;
  }
}

const SLL = new SinglyLinkedList();

SLL.push(5)
SLL.push(10)
SLL.push(15)
SLL.unshift(20) // 20 -> 5 -> 10 -> 15
// console.log(SLL.insert(2, 8)) // 20 -> 5 -> 8 -> 10 -> 15
SLL.remove(3) // 20 -> 5 -> 15
// SLL.set(1, 8) // 5 --> 8
// console.log(SLL.get(1))
// SLL.push(20)
// SLL.pop()
// SLL.shift()
console.log(SLL) // 20 -> 5 -> 10 -> 15