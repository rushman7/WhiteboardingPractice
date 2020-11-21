class MaxBinaryHeap {
  constructor() {
    this.values = [];
  }

  insert(val) {
    this.values.push(val);

    let index = this.values.length-1;
    let parentIndex = Math.floor((index-1)/2);

    while (this.values[index] > this.values[parentIndex]) {
      [this.values[index],this.values[parentIndex]] = [this.values[parentIndex],this.values[index]]
      index = parentIndex;
      parentIndex = Math.floor((index-1)/2);
    }
  }

  removeMax() {
    if (this.values.length < 2) return this.values = [];
    [this.values[0], this.values[this.values.length-1]] = [this.values[this.values.length-1], this.values[0]]
    this.values.pop();
    let curr = 0,
        left = (2*curr) + 1,
        right = (2*curr) + 2

    while (this.values[curr] < this.values[left] || this.values[curr] < this.values[right]) {
      if (left < this.values.length && right < this.values.length) {
        if (this.values[left] > this.values[right]) {
          [this.values[curr], this.values[left]] = [this.values[left], this.values[curr]];
          curr = left;
          left = (2*curr) + 1;
          right = (2*curr) + 2;
        } else {
          [this.values[curr],this.values[right]] = [this.values[right], this.values[curr]];
          curr = right;
          left = (2*curr) + 1;
          right = (2*curr) + 2;
        }
      } else if (left < this.values.length) {
        [this.values[curr], this.values[left]] = [this.values[left], this.values[curr]];
        break;
      }
    }
    
    return console.log(this.values)
  }


}

const maxBiHeap = new MaxBinaryHeap();

maxBiHeap.insert(20)
maxBiHeap.insert(25)
maxBiHeap.insert(17)
maxBiHeap.insert(27)
maxBiHeap.insert(87)
maxBiHeap.insert(28)
maxBiHeap.insert(8)
maxBiHeap.removeMax()
// console.log(maxBiHeap.values);

/*
              87
        27          28
      25   20     17    8

              27
        25          17
      20   8       

    [87, 27, 28,  8, 20, 17, 25]
    [ 0,  1,  2,  3,  4,  5,  6]
*/
