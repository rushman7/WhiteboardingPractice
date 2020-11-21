// Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

// An input string is valid if:

// Open brackets must be closed by the same type of brackets.
// Open brackets must be closed in the correct order.

var isValid = function(s) {
  let stack = [];
  let left = {
      '{' : '}',
      '(' : ')',
      '[' : ']'
  }
  
  for (let char of s) {
      if (left[char]) {
          stack.push(char)
      } else {
          let temp = stack.pop()
          if (char !== left[temp]) return false
      }
  }
  
  return stack.length > 0 ? false : true
};