// You work in an electronic exchange. Throughout the day, you receive ticks (trading data) which consists of 
// product name and its traded volume of stocks. Eg: {name: vodafone, volume: 20}. What data structure will you 
// maintain if:
// * You have to tell top k products traded by volume at end of day.
// * You have to tell top k products traded by volume throughout the day.

class MinBinaryHeap {
  constructor() {
    this.values = [];
  }
}

const minBiHeap = new MinBinaryHeap();

minBiHeap.insert({name: 'vodafone', volume: 20})
minBiHeap.insert({name: 'netflix', volume: 17})
minBiHeap.insert({name: 'twitter', volume: 21})
minBiHeap.insert({name: 'boeing', volume: 13})
minBiHeap.insert({name: 'vodafone', volume: 20})
minBiHeap.insert({name: 'netflix', volume: 31})
minBiHeap.insert({name: 'netflix', volume: 38})
// console.log(minBiHeap.values);

/*
              8
         25       17
      27    87 28    20    

    [8, 25, 17, 27, 87, 28, 20]
    [0,  1,  2,  3,  4,  5,  6]
*/
