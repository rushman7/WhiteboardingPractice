# Given a singly linked list, determine if it is a palindrome.

# Example 1:

# Input: 1->2
# Output: false
# Example 2:

# Input: 1->2->2->1
# Output: true
# Follow up:
# Could you do it in O(n) time and O(1) space?

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        curr = head
        ans = []
        
        while curr:
            ans.append(curr.val)
            curr = curr.next
            
        return ans == ans[::-1]