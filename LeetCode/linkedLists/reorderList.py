# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

# You may not modify the values in the list's nodes, only nodes itself may be changed.

# Example 1:

# Given 1->2->3->4, reorder it to 1->4->2->3.
# Example 2:

# Given 1->2->3->4->5, reorder it to 1->5->2->4->3.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        if not head:
            return head
        copy, count = self.reverse(self.copy(head))
        curr = head
        
        left = True
        prev = None
        while count > 0:
            if left:
                next = curr.next
                curr.next = ListNode(copy.val, next)
                copy = copy.next
            prev = curr
            curr = curr.next
            left = not left
            count-=1
        prev.next = None
        
    def copy(self, node):
        if not node: return
        copy = ListNode(node.val)
        copy.next = self.copy(node.next)
        return copy
        
    def reverse(self, node):
        count = 0
        curr = node
        prev = None
        next = None
        
        while curr:
            count+=1
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            
        return prev, count