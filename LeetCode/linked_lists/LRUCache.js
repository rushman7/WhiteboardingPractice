class Node {
    constructor(key, val) {
        this.val = val;
        this.key = key;
        this.next = null;
        this.prev = null
    }
}
class LRUCache {
    constructor(capacity) {
        this.head = new Node();
        this.tail = new Node();
        this.capacity = capacity;
        this.size = 0;
        this.cache = {};
    }
    
    get(key) {
        if (this.cache[key]) {
            let temp = this.cache[key];
            if (this.head.next == temp) return this.cache[key].val
            else {
                this.remove(temp);
                this.add(temp);
                return temp.val
            }
        }
        return -1;
    }

    put(key, val) {
        let node = new Node(key, val);
        if (this.cache[key]) {
            this.remove(this.cache[key]);
            this.add(node);
        } else {
            if (this.size < this.capacity) this.add(node);
            else {
                this.remove(this.tail.prev)
                this.add(node);
            }
        }
    }
    
    add(node) {
        if (this.size == 0) {
            node.prev = this.head;
            node.next = this.tail;
            this.head.next = node;
            this.tail.prev = node;
        } else {
            this.head.next.prev = node;
            node.next = this.head.next
            node.prev = this.head;
            this.head.next = node;
        }
        this.cache[node.key] = node
        this.size++;
    }
    
    remove(node) {
        this.size--;
        delete this.cache[node.key];
        let prev = node.prev;
        let next = node.next;
        prev.next = next;
        next.prev = prev;
    }
};