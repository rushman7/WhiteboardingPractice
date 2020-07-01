// Given two strings s and t, determine if they are both one edit distance apart.

// Note: 

// There are 3 possiblities to satisify one edit distance apart:

// Insert a character into s to get t
// Delete a character from s to get t
// Replace a character of s to get t
// Example 1:

// Input: s = "ab", t = "acb"
// Output: true
// Explanation: We can insert 'c' into s to get t.
// Example 2:

// Input: s = "cab", t = "ad"
// Output: false
// Explanation: We cannot get t from s by only one step.
// Example 3:

// Input: s = "1203", t = "1213"
// Output: true
// Explanation: We can replace '0' with '1' to get t.

var isOneEditDistance = function(s, t) {
  if (s === t) return false
  let str1 = s.length < t.length ? t : s;
  let str2 = s.length >= t.length ? t : s;
  let c = 0;
  let p = 0;
  
  for (let i=0;i<str1.length;i++) {
      if (str1[i] !== str2[p]) {
          c++
          if (str1.length === str2.length) {
              p++
          } 
          if (str1[i+1] === str2[p]) {
              i++
              p++
          }
      } else {
          console.log('line 27')
          p++
      }
  }
  return c <= 1 ? true : false
};