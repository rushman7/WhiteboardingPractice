# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sentinal = ListNode()
        curr1, curr2, sent = l1, l2, sentinal
        
        def move_carry(head):
            curr = head
            carry = 0
            
            while curr:
                curr.val+=carry
                carry = 0
                if curr.val >= 10:
                    carry = 1
                    curr.val-=10
                if carry and not curr.next:
                    curr.next = ListNode(carry)
                    break
                curr = curr.next

            return head
        
        while curr1 or curr2:
            if curr1 and curr2:
                sent.next = ListNode(curr1.val+curr2.val)
                curr1, curr2 = curr1.next, curr2.next
            elif curr1:
                sent.next = ListNode(curr1.val)
                curr1 = curr1.next
            else:
                sent.next = ListNode(curr2.val)
                curr2 = curr2.next
            sent = sent.next
            
        sentinal.next = move_carry(sentinal.next)
        
        return sentinal.next

# O(1) extra space solution
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr1, curr2 = l1, l2
        len1, len2 = self.find_len(l1), self.find_len(l2)
        list1 = True
        if len2 > len1:list1 = False
        
        while curr1 or curr2:
            if list1:
                if curr1 and curr2:
                    curr1.val+=curr2.val
                    curr1, curr2 = curr1.next, curr2.next
                else:
                    curr1 = curr1.next
            else:
                if curr1 and curr2:
                    curr2.val+=curr1.val
                    curr1, curr2 = curr1.next, curr2.next
                else:
                    curr2 = curr2.next
        if list1:
            l1 = self.move_carry(l1)
        else:
            l2 = self.move_carry(l2)
        
        return l1 if list1 else l2
    
    def find_len(self, node, count=0):
        if not node: return count
        return self.find_len(node.next, count+1)
    
    def move_carry(self, head):
        curr = head
        carry = 0

        while curr:
            curr.val+=carry
            carry = 0
            if curr.val >= 10:
                carry = 1
                curr.val-=10
            if carry and not curr.next:
                curr.next = ListNode(carry)
                break
            curr = curr.next

        return head