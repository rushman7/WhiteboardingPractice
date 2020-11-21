// Say you have an array for which the ith element is the price of a given stock on day i.

// If you were only permitted to complete at most one transaction 
// (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

// Note that you cannot sell a stock before you buy one.

function maxProfit(arr) {
  let profit = 0,
    buy = arr[0];

  for (i in arr) {
    if (arr[i] - buy > profit) profit = arr[i] - buy;
    if (arr[i] < buy) buy = arr[i]
  }

  return profit;
}

console.log(maxProfit([7,1,5,3,6,4])); // 5
console.log(maxProfit([7,6,4,3,1])); // 0
