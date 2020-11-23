// Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

// Examples:

// s = "leetcode"
// return 0.

// s = "loveleetcode"
// return 2.
 

// Note: You may assume the string contains only lowercase English letters.

var firstUniqChar = function(s) {
  let hashMap = new Map();
  
  for (let i=0;i<s.length;i++) {
      if (hashMap.has(s[i])) hashMap.set(s[i], [hashMap.get(s[i])[0], hashMap.get(s[i])[1]+1])
      else hashMap.set(s[i], [i, 1]);
  }
  
  for (i of hashMap) if (i[1][1] == 1) return i[1][0]
  
  return -1
};