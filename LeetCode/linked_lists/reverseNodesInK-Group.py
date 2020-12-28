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
    # create a sentinal node as our final result (O(N) space)
    sentinal = ListNode()
    # create a reference to our sentinal
    temp = sentinal
    # while there are nodes to reverse
    while head:
        # sentinals.next and head, if not enough nodes to reverse temp next is just whats left of head, 
        # else its reversed and head is now k nodes further
        temp.next, head = self.reverseKNodes(head, k)
        while temp.next:
            # move our sentinal reference to last node (k times)
            temp = temp.next
    return sentinal.next

def reverseKNodes(self,head,k):
    # reverse k nodes function 
    curr = head
    prev = None
    next = None
    count = k
    # checking first if we have enough nodes to reverse
    while count and curr:
        count-=1
        curr = curr.next
    # if not enough nodes, return the original head
    if count:
        return head, None
    # re-refernce the head
    curr = head
    while k and curr:
        # reverse nodes k times
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        k-=1
    # return our new reversed nodes as prev, and remaining unreversed nodes as curr
    return prev, curr