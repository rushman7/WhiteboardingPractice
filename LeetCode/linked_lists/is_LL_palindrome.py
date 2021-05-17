class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        curr = head
        size = self.get_len(curr)
        mid = size // 2
        curr = head
        for _ in range(mid):
            curr = curr.next
            
        middle_node = self.reverse(curr)
        curr = head
        
        while middle_node:
            if curr.val != middle_node.val:
                return False
            curr = curr.next
            middle_node = middle_node.next
        
        return True
        
    def reverse(self, node):
        curr, prev, next = node, None, None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        return prev
    
    def get_len(self, node):
        size = 0
        while node:
            size += 1
            node = node.next
        return size