// Write a function to crush candy in one dimensional board. In candy crushing games, 
// groups of like items are removed from the board. In this problem, any 
// sequence of 3 or more like items should be removed and any items adjacent to 
// that sequence should now be considered adjacent to each other. This process should 
// be repeated as many time as possible. You should greedily remove characters from left to right.

function candyCrush(str, sIdx=0, eIdx=1) {
  if (eIdx >= str.length) return str;

  while (str[sIdx] == str[eIdx]) eIdx++

  if ((eIdx - sIdx) > 2) {
    let res = str.replace(str.substring(sIdx,eIdx),'')
    return candyCrush(res, sIdx=0, eIdx=1)
  } else return candyCrush(str, sIdx+1, eIdx=sIdx+1)
}


console.log(candyCrush("aaabbbc")) // "c"
console.log(candyCrush("aabbbacd")) // "cd"
console.log(candyCrush("aabbccddeeedcba")) // ""
console.log(candyCrush("aaabbbacd")) // "acd"