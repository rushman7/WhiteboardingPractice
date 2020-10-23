class Node {
  constructor(val, priority) {
    this.val = val;
    this.priority = priority;
  }
}

class PriorityQueue {
  constructor() {
    this.values = [];
  }

  enqueue(val, prio) {
    let node = new Node(val, prio)
    if (!this.values.length) return this.values.push(node);
    this.values.push(node);

    let index = this.values.length-1;
    let parentIndex = Math.floor((index-1)/2);

    while (this.values[index].priority < this.values[parentIndex].priority) {
      [this.values[index], this.values[parentIndex]] = [this.values[parentIndex], this.values[index]]
      index = parentIndex;
      parentIndex = Math.floor((index-1)/2);
      if (index == 0) break;
    }
  }

  dequeue() {
    if (this.values.length < 2) return this.values = [];
    [this.values[0], this.values[this.values.length-1]] = [this.values[this.values.length-1], this.values[0]]
    let max = this.values.pop();
    
    if (this.values.length <= 2) {
      if (this.values.length == 2) {
        if (this.values[0].priority > this.values[1].priority) [this.values[0], this.values[1]] = [this.values[1], this.values[0]]
      }
      return max;
    }

    let curr = 0,
        left = (2*curr) + 1,
        right = (2*curr) + 2

    while (this.values[curr].priority > this.values[left].priority || this.values[curr].priority > this.values[right].priority) {
      if (this.values[left].priority < this.values[right].priority) {
        [this.values[curr], this.values[left]] = [this.values[left], this.values[curr]];
        curr = left;
        left = (2*curr) + 1;
        right = (2*curr) + 2;
        if (left >= this.values.length) break;
        if (right >= this.values.length) {
          if (this.values[curr].priority > this.values[left].priority) [this.values[curr], this.values[left]] = [this.values[left], this.values[curr]];
          break;
        }
      } else {
        [this.values[curr], this.values[right]] = [this.values[right], this.values[curr]];
        curr = right;
        left = (2*curr) + 1;
        right = (2*curr) + 2;
        if (left >= this.values.length) break;
        if (right >= this.values.length) {
          if (this.values[curr].priority > this.values[left].priority) [this.values[curr], this.values[left]] = [this.values[left], this.values[curr]];
          break;
        }
      } 
    }
    
    return max;
  }
}

const priorityQueue = new PriorityQueue();

priorityQueue.enqueue('P1', 5)
priorityQueue.enqueue('P2', 2)
priorityQueue.enqueue('P3', 3)
priorityQueue.enqueue('P4', 1)
priorityQueue.enqueue('P5', 2)
priorityQueue.enqueue('P6', 3)
priorityQueue.enqueue('P7', 1)
priorityQueue.dequeue()

console.log(priorityQueue.values);

/*
              3
         2        1
      5    2   3    

    [1, 2, 1, 5, 2, 3, 3]
    [0, 1, 2, 3, 4, 5, 6]
*/
