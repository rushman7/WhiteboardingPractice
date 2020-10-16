class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
    this.prev = null;
  }
}

class DoublyLinkedList{
  constructor() {
    this.length = 0;
    this.head = null;
    this.tail = null;
  }

  push(val) {
    let node = new Node(val);
    if (!this.length) this.head = this.tail = node;
    
    this.tail.next = node;
    node.prev = this.tail;
    this.tail = node;
    this.length++

    return this;
  }

  
  pop() {
    if (!this.length) return false;

    if (this.length == 1) {
      this.length--
      return this.head = this.tail = null
    }

    this.tail = this.tail.prev;
    this.tail.next = null;
    this.length--
    return this;
  }

  shift() {
    if (!this.length) return false;

    if (this.length == 1) {
      this.length--
      return this.head = this.tail = null
    }

    this.head = this.head.next;
    this.head.prev = null;
    this.length--
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
    console.log(this)
  }
}

const DLL = new DoublyLinkedList();

DLL.push(5).push(10).push(15).push(20).push(25)
  .pop().shift()
DLL.print()
