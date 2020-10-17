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

  unshift(val) {
    let node = new Node(val);
    if (!this.length) this.head = this.tail = node;
    
    node.next = this.head;
    this.head.prev = node;
    this.head = node;
    this.length++

    return this;
  }

  get(index) {
    if (index < 0 || index >= this.length || !this.length) return null;

    let curr;

    if (index <= this.length/2) {
      curr = this.head;
      while (index > 0) { 
        index--
        curr = curr.next;
      }
    } else {
      curr = this.tail;
      let count = this.length-1;
      while (index < count) { 
        count--
        curr = curr.prev;
      }
    }

    return curr;
  }

  set(index, val) {
    let node = this.get(index)

    if (node) node.val = val;

    return node;
  }

  insert(index, val) {
    if (index == 0) return this.unshift(val);
    if (index == this.length) return this.push(val);

    let next = this.get(index);
    let node = new Node(val);

    if (next) {
      node.prev = next.prev;
      node.next = next;
      next.prev.next = node;
      next.prev = node;
    }

    this.length++
    return next ? node : next;
  }

  remove(index) {
    if (index == 0) return this.shift();
    if (index == this.length-1) return this.pop();

    let node = this.get(index);

    if (node) {
      node.prev.next = node.next;
      node.next.prev = node.prev;
    }

    this.length--
    return node;
  }

  print() { 
    let arr = [];
    let curr = this.head;
    while (curr) {
      arr.push(curr.val)
      curr=curr.next
    }
    console.log(arr)
    // console.log(this)
  }
}

const DLL = new DoublyLinkedList();

DLL.push(5).push(10).push(15).push(20).push(25).push(30)
  .pop().shift().unshift(4)
  DLL.print()
