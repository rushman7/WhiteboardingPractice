// You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

// You may assume the two numbers do not contain any leading zero, except the number 0 itself.

// Example:

// Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
// Output: 7 -> 0 -> 8
// Explanation: 342 + 465 = 807.

var addTwoNumbers = function(l1, l2) {
  const result = new ListNode();
  let node = result;
  let buffer = 0;
  
  while (l1 != null || l2 != null) {
      let val;
      if (l1 === null) val = l2.val;
      else if (l2 === null) val = l1.val;
      else val = l1.val + l2.val
      
      val+=buffer;
      buffer = 0;
      if (val > 9) {
          val = val - 10;
          buffer++
      }
      
      let newNode = new ListNode(val,null)
      node = node.next = newNode;
      l1 = (l1 != null) ? l1.next : l1
      l2 = (l2 != null) ? l2.next : l2
  }
  if (buffer > 0) node.next = new ListNode(buffer, null)
  return result.next
};