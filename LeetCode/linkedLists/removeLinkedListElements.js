// Remove all elements from a linked list of integers that have value val.

var removeElements = function(head, val) {
  let node = new ListNode(0, head);
  
  let prev = node,
      curr = head;
  
  while (curr) {
      if (curr.val == val) prev.next = curr.next;
      else prev = curr;
      curr = curr.next;
  }
  
  return node.next;
};