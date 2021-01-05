# Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

 

# Example 1:


# Input: head = [1,2,3,3,4,4,5]
# Output: [1,2,5]
# Example 2:


# Input: head = [1,1,1,2,3]
# Output: [2,3]
 

# Constraints:

# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.

def deleteDuplicates(self, head: ListNode) -> ListNode:
    sentinal = ListNode(0, head)
    curr = head
    sent = sentinal
    
    while curr:
        if curr.next and curr.val == curr.next.val:
            while curr.next and curr.val == curr.next.val:
                curr = curr.next
            curr = curr.next
        else:
            sent.next = curr
            curr = curr.next
            sent = sent.next
    sent.next = curr
    return sentinal.next