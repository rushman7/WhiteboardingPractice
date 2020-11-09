// Given a string s of '(' , ')' and lowercase English characters. 

// Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

// Formally, a parentheses string is valid if and only if:

// It is the empty string, contains only lowercase characters, or
// It can be written as AB (A concatenated with B), where A and B are valid strings, or
// It can be written as (A), where A is a valid string.
 
function removePar(str) {
  let strArr = str.split("")
  let stack = [];

  for (let i=0;i<strArr.length;i++) {
    if (strArr[i] == '(' || strArr[i] == ')') {
      if (strArr[i] == ')' && stack.length == 0) delete strArr[i];
      else if (strArr[i] == '(') stack.push({string: '(', index: i});
      else stack.pop();
    }
  }
  for (i in stack) delete strArr[stack[i].index]
  
  return strArr.join("");
}


console.log(removePar("lee(t(c)o)de)")) // "lee(t(c)o)de"
console.log(removePar("a)b(c)d")) // "ab(c)d"
console.log(removePar("))((")) // ""
console.log(removePar("(a(b(c)d)")) // "a(b(c)d)"
