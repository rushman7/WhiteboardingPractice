# Given a non-negative integer represented as a linked list of digits, plus one to the integer.

# The digits are stored such that the most significant digit is at the head of the list.

 

# Example 1:

# Input: head = [1,2,3]
# Output: [1,2,4]
# Example 2:

# Input: head = [0]
# Output: [1]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        node = self.rev(head)
        node.val+=1
        curr = node
        
        while curr.val == 10:
            curr.val = 0
            if curr.next:
                curr.next.val+=1
            else:
                curr.next = ListNode(1)
            curr = curr.next
        
        return self.rev(node)
            
    def rev(head):
        curr = head
        prev = None
        next = None
        
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            
        return prev
            
        