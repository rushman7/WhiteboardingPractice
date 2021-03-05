class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        curr_a = headA
        curr_b = headB
        
        while curr_a != curr_b:
            curr_a = headB if not curr_a else curr_a.next
            curr_b = headA if not curr_b else curr_b.next
        
        return curr_a
