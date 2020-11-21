class MinHeap {
  constructor() {
    this.values = [];
    this.size = 0;
  }

  insert(val) {
    this.values.push(val);
    this.size++;
    if (this.size == 1) return true;
    let idx = this.size-1

    while (val < this.values[Math.floor((idx-1)/2)]) {
      [this.values[idx], this.values[Math.floor((idx-1)/2)]] = [this.values[Math.floor((idx-1)/2)], this.values[idx]]
      idx = Math.floor((idx-1)/2);
    }

    return true;
  }

  getMin() {
    if (this.size) return this.values[0];
    return false;
  }

  removeMin() {
    if (!this.getMin()) return false;
    this.size--
    if (this.size == 1) {
      this.values.pop();
      return true;
    }

    [this.values[0],this.values[this.size]] = [this.values[this.size],this.values[0]];
    this.values.pop();
    this.minHeapify(0)
    return true;
  }

  minHeapify(idx) {
    if (idx == this.size) return;
    let left = idx*2+1,
      right = idx*2+2,
      curr = idx;

    if (left < this.size && this.values[left] < this.values[idx]) curr = left;
    if (right < this.size && this.values[right] < this.values[curr]) curr = right;

    if (curr != idx) {
      [this.values[idx],this.values[curr]] = [this.values[curr],this.values[idx]];
      this.minHeapify(curr);
    }
  }
}

const minHeap = new MinHeap();

minHeap.insert(20)
minHeap.insert(25)
minHeap.insert(17)
minHeap.insert(27)
minHeap.insert(87)
minHeap.insert(28)
minHeap.insert(8)
// console.log(minHeap.getMin());
minHeap.removeMin();
console.log(minHeap);

/*
              17
        25          20
      27   87     28       

    [ 8, 25, 17, 27, 87, 28, 20]
    [ 0,  1,  2,  3,  4,  5,  6]
*/
