// A company is planning to interview 2n people. 
// Given the array costs where costs[i] = [aCosti, bCosti], 
// the cost of flying the ith person to city a is aCosti, 
// and the cost of flying the ith person to city b is bCosti.

// Return the minimum cost to fly every person to a city 
// such that exactly n people arrive in each city.

function twoCitySchedule(costs) {
  let sum = 0;
  let diff = [];

  for (i in costs) diff.push([costs[i][0] - costs[i][1], i]);
  diff.sort((a,b) => a[0] - b[0])

  for (j in diff) {
    if (j < costs.length/2) sum += costs[diff[j][1]][0];
    else sum += costs[diff[j][1]][1]
  }
  
  return sum
}

console.log(twoCitySchedule([[10,20],[30,200],[400,50],[30,20]]))// 110
console.log(twoCitySchedule([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]))// 1859
console.log(twoCitySchedule([[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]))// 3086
// Example 1:

// Input: costs = [[10,20],[30,200],[400,50],[30,20]]
//                  A        A           B        B
// Output: 110
// Explanation: 
// The first person goes to city A for a cost of 10.
// The second person goes to city A for a cost of 30.
// The third person goes to city B for a cost of 50.
// The fourth person goes to city B for a cost of 20.

// The total minimum cost is 10 + 30 + 50 + 20 = 110 
// to have half the people interviewing in each city.

// Example 2:
// Input: costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
//                   -511      394        259     45         722       108
//                   A             B        B     A             B     A
// Output: 1859

// Example 3:
// Input: costs = [[515,563],[451,713],[537,709],[343,819],
// [855,779],[457,60],[650,359],[631,42]]
// Output: 3086