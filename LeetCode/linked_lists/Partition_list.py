class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        greater, lesser = ListNode(0), ListNode(0)
        g, l = greater, lesser
        
        while head:
            if head.val >= x:
                g.next = head
                g = g.next
            else:
                l.next = head
                l = l.next
            head = head.next

        g.next = None
        l.next = greater.next

        return lesser.next