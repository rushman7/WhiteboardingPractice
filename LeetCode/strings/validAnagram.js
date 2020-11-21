// Given two strings s and t , write a function to determine if t is an anagram of s.

function isAnagram(s, t) {
  if (s.length != t.length) return false;
  let cacheS = {},
    cacheT = {}
  for (i in s) {
    if (cacheS[s[i]]) cacheS[s[i]]++;
    else cacheS[s[i]] = 1;
    if (cacheT[t[i]]) cacheT[t[i]]++;
    else cacheT[t[i]] = 1;
  }

  for (i in cacheS) {
    if (cacheS[i] != cacheT[i]) return false
  }

  return true;
}

console.log(isAnagram("anagram", "nagaram")) // true;

console.log(isAnagram("rat", "car")) // false