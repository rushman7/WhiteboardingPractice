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
}

const maxBiHeap = new MaxBinaryHeap();

maxBiHeap.insert(6)
maxBiHeap.insert(15)
maxBiHeap.insert(20)
maxBiHeap.insert(3)
maxBiHeap.insert(8)
maxBiHeap.insert(13)
maxBiHeap.insert(17)
maxBiHeap.insert(27)
maxBiHeap.insert(1)
maxBiHeap.insert(87)
maxBiHeap.insert(14)
maxBiHeap.insert(28)
maxBiHeap.insert(4)
maxBiHeap.insert(9)
maxBiHeap.insert(25)
console.log(maxBiHeap.values);

/*
              87
        27          28
      8   20     17    25
    3  1 6  14 13  4  9  15


    [87, 27, 28,  8, 20, 17, 25,  3,  1,  6, 14, 13,  4,  9, 15]
    [ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14]
*/
