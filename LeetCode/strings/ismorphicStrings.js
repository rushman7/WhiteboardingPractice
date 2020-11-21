// Given two strings s and t, determine if they are isomorphic.

// Two strings are isomorphic if the characters in s can be replaced to get t.

// All occurrences of a character must be replaced with another character 
// while preserving the order of characters. 
// No two characters may map to the same character but a character may map to itself.

var isIsomorphic = function(s, t) {
  let cacheS = {};
  let cacheT = {};
  
  for (i in s) {
      if (cacheS[s[i]] && cacheS[s[i]] != t[i]) return false;
      else cacheS[s[i]] = t[i];
      if (cacheT[t[i]] && cacheT[t[i]] != s[i]) return false;
      else cacheT[t[i]] = s[i];
  }
  
  for (i in cacheS) if (cacheT[cacheS[i]] != i) return false;
  for (i in cacheT) if (cacheS[cacheT[i]] != i) return false;
  
  return true;
};