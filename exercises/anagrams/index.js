// --- Directions
// Check to see if two provided strings are anagrams of eachother.
// One string is an anagram of another if it uses the same characters
// in the same quantity. Only consider characters, not spaces
// or punctuation.  Consider capital letters to be the same as lower case
// --- Examples
//   anagrams('rail safety', 'fairy tales') --> True
//   anagrams('RAIL! SAFETY!', 'fairy tales') --> True
//   anagrams('Hi there', 'Bye there') --> False

function anagrams(stringA, stringB) {
  return cleanString(stringA) === cleanString(stringB);
}
function cleanString(str) {
  return str.replace(/[^\w]/g, '').toLowerCase().split('').sort().join('');
}

// function anagrams(stringA, stringB) {
//   const wordA = stringA.replace(/[^\w]/g, "").toLowerCase();
//   const wordB = stringB.replace(/[^\w]/g, "").toLowerCase();

//   let charsA = {};
//   let charsB = {};

//   for (let char of wordA) {
//     charsA[char] = charsA[char] + 1 || 1;
//   }

//   for (let char of wordB) {
//     charsB[char] = charsB[char] + 1 || 1;
//   }

//   if (Object.keys(charsA).length !== Object.keys(charsB).length) {
//     return false;
//   }

//   for (let char in charsA) {
//     if (charsA[char] !== charsB[char]) {
//       return false;
//     }
//   }

//   return true;
// }

module.exports = anagrams;
