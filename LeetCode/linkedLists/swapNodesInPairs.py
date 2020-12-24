# Given a linked list, swap every two adjacent nodes and return its head.

# You may not modify the values in the list's nodes. Only nodes itself may be changed.

 

# Example 1:


# Input: head = [1,2,3,4]
# Output: [2,1,4,3]
# Example 2:

# Input: head = []
# Output: []
# Example 3:

# Input: head = [1]
# Output: [1]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        sentinal = ListNode()
        temp = sentinal
        prev = None
        next = None
        while head and head.next:
            for _ in range(2):
                next = head.next
                head.next = prev
                prev = head
                head = next
            temp.next = prev
            temp = temp.next.next
            prev = None
            next = None
        temp.next = head
        return sentinal.next

# class Solution:
#     def swapPairs(self, head: ListNode) -> ListNode:
#         if not head or not head.next:
#             return head
#         sentinal = ListNode()
#         temp = sentinal
#         while head and head.next:
#             temp.next, head = self.swap(head)
#             temp = temp.next.next
        
#         return sentinal.next
#     def swap(self, node):
#         curr = node
#         next = None
#         prev = None
#         count = 0
#         while count < 2:
#             next = curr.next
#             curr.next = prev
#             prev = curr
#             curr = next
#             count+=1
#         prev.next.next = next
#         return prev, curr
        