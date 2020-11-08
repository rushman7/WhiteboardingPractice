// Given a stack of integers, sort it in ascending order using another temporary stack.

// Examples:

// Input : [34, 3, 31, 98, 92, 23]
// Output : [3, 23, 31, 34, 92, 98]

// Input : [3, 5, 1, 4, 2, 8]
// Output : [1, 2, 3, 4, 5, 8]
// Recommended: Please solve it on “PRACT

class Stack {
  constructor() {
    this.data = [];
  }

  push(val) {
    this.data.push(val);
  };

  pop() {
    if (this.size() === 0) {
      return 'Stack is empty'
    }
    return this.data.pop()
  };

  peek() {
    return this.data[this.data.length - 1]
  }

  size() {
    return this.data.length
  }

  isEmpty() {
    return this.data.length == 0 ? true : false
  }
};

function sort(stack) {
  let tempStack = new Stack();

  while (!stack.isEmpty()) {
    let temp = stack.pop();

    while (!tempStack.isEmpty() && tempStack.peek() > temp) {
      stack.push(tempStack.pop());
    }

    tempStack.push(temp);
  }

  return tempStack
}


const stack = new Stack();
stack.push(33); // 12
stack.push(12); // 23
stack.push(51); // 33
stack.push(23); // 51

sort(stack);