String.prototype.hashCode = function(size) {
  let hash = 0;
  if (this.length == 0) return hash;
  for (let i = 0; i < this.length; i++) hash = (((hash<<5)-hash) + this.charCodeAt(i)) % size;
  return hash;
}

class HashTable {
  constructor(size=13) {
    this.keyMap = new Array(size);
  }

  set(key, value) {
    let idx = key.hashCode(this.keyMap.length)
    if (this.keyMap[idx]) this.keyMap[idx].push([key, value])
    else {
      let arr = [[key, value]];
      this.keyMap[idx] = arr;
    }

    return this;
  }

  get(key) {
    let idx = key.hashCode(this.keyMap.length)
    if (this.keyMap[idx]) {
      if (this.keyMap[idx].length > 1) {
        for (let i=0;i<this.keyMap[idx].length;i++) {
          if (this.keyMap[idx][i][0] == key) return this.keyMap[idx][i];
        }
      } else return this.keyMap[idx][0]
    }

    return undefined;
  }

  keys() {
    let result = [];
    for (let i=0;i<this.keyMap.length;i++) {
      if (this.keyMap[i]) {
        if (this.keyMap[i].length > 1) {
          for (let j=0;j<this.keyMap[i].length;j++) {
            result.push(this.keyMap[i][j][0])
          }
        } else result.push(this.keyMap[i][0][0])
      }
    }

    return result;
  }

  values() {
    let result = [];
    for (let i=0;i<this.keyMap.length;i++) {
      if (this.keyMap[i]) {
        if (this.keyMap[i].length > 1) {
          for (let j=0;j<this.keyMap[i].length;j++) {
            result.push(this.keyMap[i][j][1])
          }
        } else result.push(this.keyMap[i][0][1])
      }
    }

    return result;
  }
}

const ht = new HashTable();

ht.set('blue', '#585AEE')
ht.set('black', '#000000')
ht.set('orange', '#DD9E36')
ht.set('green', '#48DD36')
ht.set('purple', '#865CE0')
ht.set('yellow', '#D2E05C')
ht.set('red', '#F33636')

console.log(ht.keyMap);
// console.log(ht.keys())
// console.log(ht.values())
