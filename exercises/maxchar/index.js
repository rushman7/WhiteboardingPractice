// --- Directions
// Given a string, return the character that is most
// commonly used in the string.
// --- Examples
// maxChar("abcccccccd") === "c"
// maxChar("apple 1231111") === "1"

function maxChar(str) {
  let chars = {};

  for (let char of str) {
    chars[char] = chars[char] + 1 || 1;
  }

  return Object.keys(chars).reduce((a, b) => chars[a] > chars[b] ? a : b)
}

module.exports = maxChar;
