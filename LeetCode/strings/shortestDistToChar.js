// Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

var shortestToChar = function(S, C) {
  let prev = Infinity;
  let arr = [];
  for (let i=0;i<S.length;i++) {
      if (S[i] == C) prev = 0;
      else prev++
      
      arr[i] = prev;
  }
  prev = Infinity;

  for (let i=S.length-1;i>=0;i--) {
      if (S[i] == C) prev = 0;
      else prev++
      
      prev = Math.min(prev, arr[i])
      arr[i] = prev;
  }
  
  return arr
};