class PriorityQueue {
  constructor(comp, arr) {
    this.arr = arr;
    this.comp = comp;

    for (let i=Math.floor((this.arr.length-1)/2);i>=0;i--) this.heapify(i);
  }

  heapify(idx) {
    if (idx >= this.arr.length) return;

    let temp = idx;

    if((2 * idx) + 1 < this.arr.length && this.comp(this.arr[(2 * idx) + 1], this.arr[temp]) < 0) temp = (2 * idx) + 1;
    if((2 * idx) + 2 < this.arr.length && this.comp(this.arr[(2 * idx) + 2], this.arr[temp]) < 0) temp = (2 * idx) + 2;

    if (temp != idx) {
      [this.arr[temp], this.arr[idx]] = [this.arr[idx], this.arr[temp]]
      this.heapify(temp);
    }
  }

  removeMax() {
    let temp = this.arr[0];
    this.arr[0] = this.arr[this.arr.length-1];
    this.arr.pop();
    this.heapify(0);

    return temp;
  }
}

function topKFrequent(words, k) {
  let map = new Map();

  words.map((item) => map.set(item, (map.get(item) || 0) + 1))
  words = [...new Set(words)]

  let heap = new PriorityQueue((a, b) => {
    if (map.get(a) == map.get(b)) return a.localeCompare(b);
    return map.get(b)-map.get(a)
  }, words)

  let result = [];

  while(k--) result.push(heap.removeMax());

  return result;
};

console.log(topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4));
console.log(topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))
console.log(topKFrequent(["aaa","aa","a"],1))
console.log(topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 3))