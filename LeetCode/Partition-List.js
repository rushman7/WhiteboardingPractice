// Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

// You should preserve the original relative order of the nodes in each of the two partitions.

// Example:

// Input: head = 1->4->3->2->5->2, x = 3
// Output: 1->2->2->4->3->5

var partition = function(head, x) {
  const lower = new ListNode();
  const higher = new ListNode();
  let l1 = lower;
  let l2 = higher;
  
  while (head) {
      if (head.val < x) l1 = l1.next = head;
      else l2 = l2.next = head;
      let next = head.next;
      head.next = null;
      head = next;
  }
  
  l1.next = higher.next
  return lower.next
};