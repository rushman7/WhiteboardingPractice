// Implement the RandomizedSet class:
// bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
// bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
// int getRandom() Returns a random element from the current set of elements 
// (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
// Follow up: Could you implement the functions of the class with each function works in average O(1) time?

class RandomizedSet {
  constructor() {
    this.cache = {};
    this.values = [];
  }
  
  insert(val) {
    if (val in this.cache) return false;

    this.values.push(val);
    this.cache[val] = this.values.length-1;

    return true;
  }
  
  remove(val) {
    // console.log('32', this.cache[val], val)
    if (val in this.cache) {
      this.cache[this.values[this.values.length-1]] = this.cache[val];
      [this.values[this.cache[val]],this.values[this.values.length-1]] = [this.values[this.values.length-1],this.values[this.cache[val]]]
      delete this.cache[val];
      this.values.pop()
      return true;
    }

    return false;
  }
  
  getRandom() {
    let num = Math.floor(Math.random() * this.values.length);
    return this.values[num]
  }
};

let random = new RandomizedSet();
random.insert(1); // true
random.remove(2); // false
random.insert(2); // true
random.getRandom(); // 1 - 2
console.log(random.remove(1)); // true
console.log(random.insert(2)); // false
console.log(random.getRandom()); // 1 - 2

console.log(random);