// Given a string s, find the length of the longest substring without repeating characters.

 

// Example 1:

// Input: s = "abcabcbb"
// Output: 3
// Explanation: The answer is "abc", with the length of 3.
// Example 2:

// Input: s = "bbbbb"
// Output: 1
// Explanation: The answer is "b", with the length of 1.
// Example 3:

// Input: s = "pwwkew"
// Output: 3
// Explanation: The answer is "wke", with the length of 3.
// Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
// Example 4:

// Input: s = ""
// Output: 0

// MY SOLUTION

var lengthOfLongestSubstring = function(s) {
  if (s.length < 2) {
      return s.length
  }
  
  let result = []; // create an empty array

  for (let i=0;i<s.length;i++) {
    let subStr = s.charAt(i)
    let k = i;
    while(!subStr.includes(s.charAt(k+1))) {
      k++
      subStr = subStr.concat(s.charAt(k))
    }
    result.push(subStr)
  }
  result.sort((a,b) => b.length - a.length)
  return result[0].length
};

// OPTIMIZED SOLUTION

// var lengthOfLongestSubstring = function(s) {
//   let cache = {},
//       i = 0,
//       ans = 0;
  
//   for (let j=0;j<s.length;j++) {
//       if (cache[s.charAt(j)]) i = Math.max(cache[s.charAt(j)], i)

//       ans = Math.max(ans, j - i + 1)
//       cache[s.charAt(j)] = j+1
//   }
  
//   return ans
// };