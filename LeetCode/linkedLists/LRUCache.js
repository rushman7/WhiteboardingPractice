class Node {
  constructor(key, val) {
      this.key = key;
      this.val = val;
      this.next = null;
      this.prev = null;
  }
}

class LRUCache {
  constructor(capacity) {
      this.capacity = capacity;
      this.cache = {};
      this.size = 0;
      this.head = new Node();
      this.tail = new Node();
      this.head.next = this.tail;
      this.tail.prev = this.head;
  }

  get(key) {
      let node = this.cache[key];
      if (!node) return -1;

      this.remove(node);
      this.add(node);
      return node.val
  }

  put(key, val) {
      let node = this.cache[key];
      
      if (node) {
          node.val = val;
          this.remove(node);
          this.add(node);
      } else {
          if (this.size == this.capacity) {
              delete this.cache[this.tail.prev.key];
              this.remove(this.tail.prev)
          }
          
          node = new Node(key, val);
          
          this.cache[key] = node;
          this.add(node);
      }
  }
  
  add(node) {
      let headNext = this.head.next;
      this.head.next = node;
      node.prev = this.head;
      if (headNext) {
          node.next = headNext;
          headNext.prev = node;
      }
      this.size++
  }
  
  remove(node) {
      let next = node.next;
      let prev = node.prev;
      
      next.prev = prev;
      prev.next = next;
      this.size--
  }
};