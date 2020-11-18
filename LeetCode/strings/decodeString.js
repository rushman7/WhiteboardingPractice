// Given an encoded string, return its decoded string.
// The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. 
// Note that k is guaranteed to be a positive integer.
// You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
// Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. 
// For example, there won't be input like 3a or 2[4].

function decodeString(str) {
  let arr = str.split("");
  let stack = [];
  let result = "";

  for (i in arr) { 
    if (arr[i] != "]") stack.push(arr[i]);
    else {
      let subStr = "";
      while (stack[stack.length-1] != "[") subStr+=stack.pop();

      stack.pop();
      let k = stack.pop();
      while (!isNaN(stack[stack.length-1])) {
        k.toString();
        k+=stack.pop();
      }
      k = k.split("").reverse().join("")
      
      subStr = subStr.repeat(k);

      if (stack.length > 0) for (let i=subStr.length-1;i>=0;i--) stack.push(subStr[i]);
      else {
        let sub = subStr.split("").reverse().join("")
        result += sub;
      }
    }
  }

  return result+=stack.join("");
}

// ["3","[","a","]","2","[","b","c","]"]

console.log(decodeString("100[leetcode]"))
// console.log(decodeString("3[a]2[bc]")) // "aaabcbc"
// console.log(decodeString("3[a2[c]]")) // "accaccacc"
// console.log(decodeString("2[abc]3[cd]ef")) // "abcabccdcdcdef"