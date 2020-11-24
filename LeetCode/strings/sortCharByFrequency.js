// Given a string, sort it in decreasing order based on the frequency of characters.

// Example 1:

// Input:
// "tree"

// Output:
// "eert"

// Explanation:
// 'e' appears twice while 'r' and 't' both appear once.
// So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
// Example 2:

// Input:
// "cccaaa"

// Output:
// "cccaaa"

// Explanation:
// Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
// Note that "cacaca" is incorrect, as the same characters must be together.
// Example 3:

// Input:
// "Aabb"

// Output:
// "bbAa"

// Explanation:
// "bbaA" is also a valid answer, but "Aabb" is incorrect.
// Note that 'A' and 'a' are treated as two different characters.

var frequencySort = function(s) {
  let hashMap = new Map();
  let result = '';
  
  for (i in s) {
      if (hashMap.get(s[i])) hashMap.set(s[i], hashMap.get(s[i])+1)
      else hashMap.set(s[i], 1)
  }
  
  let sortedMap = new Map([...hashMap].sort((a, b) => b[1] - a[1]))
  
  for (i of sortedMap) result+=i[0].repeat(i[1])
  
  return result;
};