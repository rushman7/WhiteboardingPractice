# Reverse a linked list from position m to n. Do it in one-pass.

# Note: 1 ≤ m ≤ n ≤ length of list.

# Example:

# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def reverseBetween(self, head, m, n):
        count = 1
        ans = ListNode()
        temp = ans
        curr = head
        prev = None
        next = None
        
        while curr:
            if count < m or count > n:
                temp.next = curr
                curr = curr.next
                temp = temp.next
            else:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            if count == n:
                temp.next = prev
                while temp.next: temp = temp.next
            count+=1
        return ans.next