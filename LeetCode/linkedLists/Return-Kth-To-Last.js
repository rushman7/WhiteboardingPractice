// Write a function that given the head of singly linked list, and an index (0 based) counted from the end of the list, returns the element corresponding to that index.

// The function must return a falsy value for invalid input values, like an out of range index.

// So for the list 66 -> 42 -> 13 -> 666, getKthLastElement() with index 2 should return the Node (predefined object for list nodes) corresponding to 42.


function getKthLastElement(head, k) {
  let p1 = head;
  let p2 = head;
  let i = 0;
  
  while (i < k) {
    i++
    p2 = p2.next
  }
  
  while (p2.next != null) {
    p1 = p1.next;
    p2 = p2.next;
  }
  
  return p1
}