// A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

 

// Example 1:

// Input: S = "ababcbacadefegdehijhklij"
// Output: [9,7,8]
// Explanation:
// The partition is "ababcbaca", "defegde", "hijhklij".
// This is a partition so that each letter appears in at most one part.
// A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
 

// Note:

// S will have length in range [1, 500].
// S will consist of lowercase English letters ('a' to 'z') only.

var partitionLabels = function(S) {
  let first = {},
      last = {},
      letters = {};
  
  for (i in S) {
      if (first[S[i]]) last[S[i]] = i;
      else {
          first[S[i]] = i;
          last[S[i]] = i;
          letters[S[i]] = S[i]
      }
  }
  
  let result = [],
      min = parseInt(first[S[0]]),
      max = parseInt(last[S[0]]);
  for (i in letters) {
      if (first[i] >= min && last[i] <= max) continue;
      if (first[i] < max && last[i] > max) max = parseInt(last[i]);
      else {
          result.push(max - min + 1);
          min = parseInt(first[i]);
          max = parseInt(last[i]);
      }
  }
  
  result.push(max - min + 1);
  
  return result;
};