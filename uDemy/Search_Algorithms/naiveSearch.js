  // naive string search
// Write a function which accepts a string and a pattern,
// and counts the number of times the pattern appears in the string.

// Time Complexity - O(n * m)

function naiveSearch(str, val) {
  let counter = 0;

  for (let i = 0;i<str.length;i++) {
    if (str[i] == [val[0]]) {
      let isValid = true;
      for (let j = 1; j<val.length;j++) {
        if (str[i+j] != val[j]) {
          isValid = false;
          break;
        }
      }
      if (isValid) counter++
    }
  }

  return counter;
}


console.log(naiveSearch('wowomgomg', 'omg')) // 2
console.log(naiveSearch('helloolo', 'lo')) // 2
console.log(naiveSearch('lorie loled', 'lol')) // 1