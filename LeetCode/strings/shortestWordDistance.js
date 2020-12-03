// Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

// Example:
// Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

// Input: word1 = “coding”, word2 = “practice”
// Output: 3
// Input: word1 = "makes", word2 = "coding"
// Output: 1
// Note:
// You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

var shortestDistance = function(words, word1, word2) {
  let result = Infinity,
      idx1 = -1,
      idx2 = -1;
  for (let i=0;i<words.length;i++) {
      if (words[i] == word1) idx1 = i;
      if (words[i] == word2) idx2 = i;
      if (idx1 >= 0 && idx2 >= 0) result = Math.min(result, Math.abs(idx1 - idx2))
  }
  
  return result
};