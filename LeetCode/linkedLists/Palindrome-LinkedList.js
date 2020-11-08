// Given a singly linked list, determine if it is a palindrome.

// Example 1:

// Input: 1->2
// Output: false
// Example 2:

// Input: 1->2->2->1
// Output: true

var isPalindrome = function(head) {
  if (!head) return true
  let arr = [];
  while (head) {
      arr.push(head.val);
      head = head.next;
  }
  
  return arr.join("") === arr.reverse().join("") ? true : false
};