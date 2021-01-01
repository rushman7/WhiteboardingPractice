# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

# Example 1:


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    sentinal = ListNode()
    curr = sentinal
    while l1 or l2:
        curr.next = ListNode((l1.val if l1 else 0) + (l2.val if l2 else 0))
        if l1: l1 = l1.next
        if l2: l2 = l2.next
        curr = curr.next
    sentinal.next = self.adjustListValues(sentinal.next)
    return sentinal.next
    
def reverseList(self, root):
    curr, prev, next = root, None, None
    
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    
    return prev

def adjustListValues(self, root):
    curr, carry = root, 0
    
    while curr:
        curr.val+=carry
        carry = 0
        if curr.val > 9:
            carry = 1
            curr.val-=10
        if not curr.next and carry:
            curr.next = ListNode(carry)
            break
        curr = curr.next

    return root