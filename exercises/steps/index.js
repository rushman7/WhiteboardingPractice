// --- Directions
// Write a function that accepts a positive number N.
// The function should console log a step shape
// with N levels using the # character.  Make sure the
// step has spaces on the right hand side!
// --- Examples
//   steps(2)
//       '# '
//       '##'
//   steps(3)
//       '#  '
//       '## '
//       '###'
//   steps(4)
//       '#   '
//       '##  '
//       '### '
//       '####'

// function steps(n) {
//   for (let i = 0; i < n; i++) {
//     let stair = '';

//     for (let j = 0; j < n; j++) {
//       if (j <= i) {
//         stair += '#';
//       } else {
//         stair += ' ';
//       }
//     }
//     console.log(stair);
//   }
// }

function steps(n, i = 0, stair = '') {
  if (i === n){
    return;
  }

  if (stair.length === n) {
    console.log(stair);
    return steps(n, i + 1);
  }

  if (stair.length <= i) {
    stair += '#';
  } else {
    stair += ' ';
  }
  steps(n, i, stair);
}

module.exports = steps;
