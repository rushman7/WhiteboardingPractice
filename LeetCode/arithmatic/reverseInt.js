// Given a 32-bit signed integer, reverse digits of an integer.
// Assume we are dealing with an environment that could 
// only store integers within the 32-bit signed integer range: [−231,  231 − 1].

function reverseInt(n) {
  let num = n.toString()
  if (num.length <= 1) return n;

  let result = "";

  for (let i=num.length-1;i>=0;i--) if (!isNaN(num[i])) result+=num[i];
  result = parseInt(result)
  if (result > Math.pow(2,31) || n < Math.pow(-2, 31)) return 0;
  return num[0] == "-" ? result*-1 : result
}

console.log(reverseInt(123)); // 321
console.log(reverseInt(-123)); // -321
console.log(reverseInt(120)); // 21
console.log(reverseInt(0)); // 0
console.log(reverseInt(1534236469)) // 0
