var copyRandomList = function(head, hashMap=new Map()) {
  if (!head) return head;
  if (hashMap.has(head)) return hashMap.get(head)
  
  let node = new Node(head.val)
  hashMap.set(head, node);
  
  node.next = copyRandomList(head.next, hashMap)
  node.random = copyRandomList(head.random, hashMap)
  
  return node;
};

