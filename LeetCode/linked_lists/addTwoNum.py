class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sentinal = ListNode(0)
        curr_sent = sentinal
        carry = 0
        
        while l1 or l2:
            num = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = 0
            if num > 9:
                carry = 1
                num-=10

            curr_sent.next = ListNode(num)

            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
            curr_sent = curr_sent.next

        if carry:
            curr_sent.next = ListNode(carry)

        return sentinal.next