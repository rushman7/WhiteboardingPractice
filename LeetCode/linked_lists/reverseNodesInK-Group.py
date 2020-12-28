# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

# Follow up:

# Could you solve the problem in O(1) extra memory space?
# You may not alter the values in the list's nodes, only nodes itself may be changed.
 

# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]
# Example 2:


# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]
# Example 3:

# Input: head = [1,2,3,4,5], k = 1
# Output: [1,2,3,4,5]
# Example 4:

# Input: head = [1], k = 1
# Output: [1]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
    sentinal = ListNode()
    temp = sentinal
    curr = head
    while curr:
        temp.next, curr = self.reverseKNodes(curr, k)
        while temp.next:
            temp = temp.next
    return sentinal.next

def reverseKNodes(self,root,count):
    curr = root
    prev = None
    next = None
    temp_count = count
    while temp_count and curr:
        temp_count-=1
        curr = curr.next
    if temp_count:
        return root, None
    curr = root
    while count and curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        count-=1
    return prev, curr