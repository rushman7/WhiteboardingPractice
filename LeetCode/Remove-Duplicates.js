// Given an unsorted linked list, delete all duplicates such that each element appear only once.

// Example 1:

// Input: 1->1->2
// Output: 1->2
// Example 2:

// Input: 1->1->2->3->3
// Output: 1->2->3

var deleteDuplicates = function(head) {
  if (!head || head.next === null)    return head
  let visited = {};
  let curr = head;
  visited[curr.val] = true;
  
  while (curr != null && curr.next != null) {
      if (visited[curr.next.val]) {
          curr.next = curr.next.next
      } else {
          visited[curr.next.val] = true;
          curr = curr.next
      }
  }
  return head
};