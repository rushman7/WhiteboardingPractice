# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        len1 = self.findLen(l1)
        len2 = self.findLen(l2)
        
        ans = ListNode()
        curr = ans
        while len1 > 0 and len2 > 0:
            if len1 > len2:
                curr.next = ListNode(l1.val)
                l1 = l1.next
                len1-=1
            elif len2 > len1:
                curr.next = ListNode(l2.val)
                l2 = l2.next
                len2-=1
            elif len2 == len1:
                curr.next = ListNode(l1.val+l2.val)
                l1 = l1.next
                l2 = l2.next
                len1-=1
                len2-=1
            curr = curr.next
            
        return self.revList(self.adjustNum(self.revList(ans.next)))
        
    def adjustNum(self, node):
        curr = node
        carry = 0
        while curr or carry == 1:
            if carry == 1:
                curr.val+=1
                carry = 0
            if curr.val >= 10:
                carry = 1
                curr.val-=10
            if not curr.next and carry == 1:
                temp_node = ListNode(carry)
                curr.next = temp_node
                carry = 0
                curr = curr.next
            else:
                curr = curr.next
        return node
    
    def findLen(self, node, count=0):
        if not node: return count
        return self.findLen(node.next, count=count+1)
    
    def revList(self, node):
        curr = node
        prev = None
        next = None
        
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        return prev
