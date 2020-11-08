// Given a string, determine if a permutation of the string could form a palindrome.

// Example 1:

// Input: "code"
// Output: false
// Example 2:

// Input: "aab"
// Output: true
// Example 3:

// Input: "carerac"
// Output: true

var canPermutePalindrome = function(s) {
  let even = s.length % 2 ? false : true;
  let map = {};
  
  for (char of s) {
      if (map[char]) {
          map[char]++
      } else {
          map[char] = 1
      }
  }
  
  let oddAmount = 0;
  
  for (i in map) {
      if (map[i] % 2 === 1) oddAmount++;
  }
  
  if (!even && oddAmount > 1) return false
  if (even && oddAmount > 0) return false
  
  return true
};