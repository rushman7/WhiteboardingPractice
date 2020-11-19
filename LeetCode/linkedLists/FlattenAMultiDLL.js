// You are given a doubly linked list which in addition to the next and previous pointers, 
// it could have a child pointer, which may or may not point to a separate doubly linked list. 
// These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, 
// as shown in the example below.

// Flatten the list so that all the nodes appear in a single-level, doubly linked list. 
// You are given the head of the first level of the list.

class Node {
  constructor(val, prev=null, next=null, child=null) {
    this.val = val;
    this.prev = prev;
    this.next = next;
    this.child = child;
  }

  // insert(val) {
  //   let node = new Node(val);
  //   let curr = this;
  //   while (curr.next) curr = curr.next;
  //   node.prev = curr;
  //   curr.next = node;
  // }

  // insertChild(nodeVal, val) {

  // }
}

let list = new Node(1)
list.insert(2)
list.insert(3)
list.insertChild(3, 7)


console.log(list)