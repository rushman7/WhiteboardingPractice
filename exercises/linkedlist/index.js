// --- Directions
// Implement classes Node and Linked Lists
// See 'directions' document

class Node {
  constructor(data, next = null) {
    this.data = data;
    this.next = next;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
  }

  insertFirst(data) {
    this.head = new Node(data, this.head);
  }

  size() {
    let counter = 0;
    let node = this.head;

    while (node) {
      counter++;
      node = node.next;
    }

    return counter;
  }

  getFirst() {
    return this.head;
  }

  getLast() {
    let node = this.head;

    if (!node) {
      return null;
    }

    while (node.next) {
      node = node.next;
    }

    return node;
  }

  clear() {
    this.head = null;
  }

  removeFirst() {
    if (!this.head) {
      return null;
    }

    return this.head = this.head.next;
  }

  removeLast() {
    if (!this.head) {
      return null;
    }

    if (!this.head.next) {
      this.head = null;
      return null;
    }

    let previous = this.head;
    let node = this.head.next;
    while (node.next) {
      previous = node;
      node = node.next;
    }

    previous.next = null;
  }

  insertLast(data) {
    const last = this.getLast();

    if (last) {
      last.next = new Node(data);
    } else {
      this.head = new Node(data);
    }
  }

  getAt(index) {
    if (this.head === null) {
      return null;
    }

    let node = this.head;

    for (let i = 0; i < index; i++) {
      node = node.next
    }

    return node;
  }

  removeAt(index) {
    if (!this.head) {
      return;
    }

    if (this.size() <= index) {
      return;
    }

    if (index === 0) {
      this.head = this.head.next;
      return;
    }

    let previous = this.getAt(index - 1);
    previous.next = previous.next.next;
  }

  insertAt(data, index) {
    if (!this.head) {
      return this.insertFirst(data);
    }

    if (this.size() <= index) {
      return this.insertLast(data);
    }

    if (index === 0) {
      return this.insertFirst(data);
    }

    let node = this.getAt(index - 1);
    node.next =  new Node(data, node.next)
  }

  forEach(fn) {
    let node = this.head;
    let counter = 0;

    while (node) {
      fn(node, counter);xc
      node = node.next;
      counter++;
    }
  }
}

module.exports = { Node, LinkedList };
