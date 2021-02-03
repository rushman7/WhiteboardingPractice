class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return None
        fast = head
        slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        
        return False