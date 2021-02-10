class Solution:
    def copyRandomList(self, head, hash_map={}) -> 'Node':
        if not head:
            return None
        
        if head in hash_map:
            return hash_map[head]
        
        node = Node(head.val)
        hash_map[head] = node
        
        node.next = self.copyRandomList(head.next, hash_map)
        node.random = self.copyRandomList(head.random, hash_map)
        
        return node