// --- Directions
// Given a string, return the character that is most
// commonly used in the string.
// --- Examples
// maxChar("abcccccccd") === "c"
// maxChar("apple 1231111") === "1"

function maxChar(str) {
  let charMap = {};
  str.split('').map(char => {
    charMap.hasOwnProperty(char) ? charMap[char]++ : charMap[char] = 1;
  })

  const keys = Object.keys(charMap);

  return keys.reduce((a, b) => charMap[a] > charMap[b] ? a : keys[0])
}



module.exports = maxChar;
