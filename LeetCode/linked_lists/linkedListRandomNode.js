// Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

// Follow up:
// What if the linked list is extremely large and its length is unknown to you? Could you solve this efficiently without using extra space?

class ListNode {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

class Solution {
  constructor(head) {
      this.head = head;
  }
  
  getRandom() {
      let random = 0;
      let curr = this.head;
      let res = 0;
      
      while (curr) {
          random++
          res = Math.ceil(Math.random() * random)
          curr = curr.next;
      }
      curr = this.head;
      console.log(res)
      while (res>1) {
          curr = curr.next
          res--
      }
      
      return curr.val
  }
}

let head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
let solution = new Solution(head);

console.log(solution.getRandom())