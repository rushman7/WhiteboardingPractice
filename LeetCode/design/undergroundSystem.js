// Implement the class UndergroundSystem that supports three methods:

// 1. checkIn(int id, string stationName, int t)

// A customer with id card equal to id, gets in the station stationName at time t.
// A customer can only be checked into one place at a time.
// 2. checkOut(int id, string stationName, int t)

// A customer with id card equal to id, gets out from the station stationName at time t.
// 3. getAverageTime(string startStation, string endStation) 

// Returns the average time to travel between the startStation and the endStation.
// The average time is computed from all the previous traveling from startStation to endStation that happened directly.
// Call to getAverageTime is always valid.
// You can assume all calls to checkIn and checkOut methods are consistent. That is, if a customer gets in at time t1 at some station, then it gets out at time t2 with t2 > t1. All events happen in chronological order.
class UndergroundSystem {
  constructor() {
      this.customers = new Map();
      this.times = new Map();
  }
  
  checkIn(id, startStation, t) {
      if (this.customers.has(id)) return -1;
      this.customers.set(id, [startStation, t])
  }
  
  checkOut(id, endStation, t) {
      if (!this.customers.has(id)) return -1;
      let data = this.customers.get(id);
      let direction = data[0]+endStation;
      
      if (this.times.has(direction)) {
          let prev = this.times.get(direction);
          this.times.set(direction, [prev[0] + t-data[1], prev[1] + 1])
      } else this.times.set(direction, [t-data[1],1])
      
      this.customers.delete(id)
  }
  
  getAverageTime(startStation, endStation) {
      let direction = startStation+endStation;
      
      if (this.times.has(direction)) {
          let data = this.times.get(direction)
          return data[0] / data[1]
      }
  }
}
