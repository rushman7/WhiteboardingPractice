class Node {
  constructor(key, val) {
      this.val = val;
      this.key = key;
      this.next = null;
      this.prev = null;
  }
}

class LRUCache {
  constructor(capacity) {
      this.capacity = capacity;
      this.cache = {};
      this.head = null;
      this.tail = null;
      this.size = 0;
  }
  
  insert(key, val) {
      let node = new Node(key, val);
      if (!this.size) this.head = this.tail = node;
      else {
          node.next = this.head;
          this.head.prev = node;
          this.head = node;
      }
      this.size++
      return node;
  }
  
  pop() {
    if (this.size < 2) this.head = this.tail = null;
    else {
        this.tail.prev.next = null;
        this.tail = this.tail.prev;
    }
    this.size--
    return;
  }
  
  get(key) {
    if (this.cache[key]) {
      let node = this.cache[key]
      if (!node.next) this.pop();
      else if (node == this.head) return node.val;
      else {
        node.prev.next = node.next;
        node.next.prev = node.prev;
        this.size--
      }
      this.insert(key, node.val)
      return this.cache[key].val
    } else return -1
  }
  
  put(key, val) {
      if (!this.cache[key]) {
        let node = this.insert(key, val);
        this.cache[key] = node;
        if (this.size > this.capacity) {
          let node = this.tail;
          this.pop();
          delete this.cache[node.key]
        }
      } else {
        this.get(key);
        this.head.val = val;
        this.cache[key] = this.head;
      }
  }
};

const lRUCache = new LRUCache(2);

lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.put(4);    // {4=4, 3=3}

console.log('CACHE', lRUCache.cache, lRUCache.head)
