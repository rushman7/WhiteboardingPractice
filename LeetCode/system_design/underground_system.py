# Implement the UndergroundSystem class:

# void checkIn(int id, string stationName, int t)
# A customer with a card id equal to id, gets in the station stationName at time t.
# A customer can only be checked into one place at a time.
# void checkOut(int id, string stationName, int t)
# A customer with a card id equal to id, gets out from the station stationName at time t.
# double getAverageTime(string startStation, string endStation)
# Returns the average time to travel between the startStation and the endStation.
# The average time is computed from all the previous traveling from startStation to endStation that happened directly.
# Call to getAverageTime is always valid.
# You can assume all calls to checkIn and checkOut methods are consistent. If a customer gets in at time t1 at some station, they get out at time t2 with t2 > t1. All events happen in chronological order.

class UndergroundSystem:

    def __init__(self):
        self.customers = {}
        self.avg_times = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customers[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, time = self.customers[id]
        del self.customers[id]
        
        if f"{startStation}->{stationName}" in self.avg_times:
            avgs, total_trips = self.avg_times[f"{startStation}->{stationName}"]
            self.avg_times[f"{startStation}->{stationName}"] = (t-time+avgs, total_trips+1)
        else:
            self.avg_times[f"{startStation}->{stationName}"] = (t-time, 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, trips = self.avg_times[f"{startStation}->{endStation}"]
        return total_time/trips