// Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

// push(x) -- Push element x onto stack.
// pop() -- Removes the element on top of the stack.
// top() -- Get the top element.
// getMin() -- Retrieve the minimum element in the stack.

class MinStack {
  constructor() {
      this.stack = [];
      this.min = 0;
  }
  
  push(val) {
      if (this.stack.length == 0) this.min = val;
      else if (this.min > val) this.min = val;
      
      this.stack.push([val, this.min])
  }
  
  pop() {
      this.stack.pop();
      if (this.stack.length == 0) this.min = 0;
      else this.min = this.stack[this.stack.length-1][1]
  }
  
  top() {
      return this.stack[this.stack.length-1][0];
  }
  
  getMin() {
      return this.stack[this.stack.length-1][1]
  }
};