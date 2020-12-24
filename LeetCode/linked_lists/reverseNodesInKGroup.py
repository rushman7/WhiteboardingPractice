# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

# Follow up:

# Could you solve the problem in O(1) extra memory space?
# You may not alter the values in the list's nodes, only nodes itself may be changed.

class Solution(object):
    def reverseKGroup(self, head, k):
        val = k
        ans = ListNode()
        temp, curr = ans, head
        prev = next = None
        leftover = self.deepCopy(head)
        while curr and val > 0:
            val-=1
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            if val == 0:
                val = k
                leftover = self.deepCopy(next)
                temp.next = prev
                while temp.next: temp = temp.next
                prev = None
                next = None
        if val != k: temp.next = leftover
        return ans.next

    def deepCopy(self, head):
        if not head: return
        node = ListNode(head.val)
        node.next = self.deepCopy(head.next)
        return node
        