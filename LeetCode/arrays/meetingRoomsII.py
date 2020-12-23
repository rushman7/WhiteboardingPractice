# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

# Example 1:

# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2
# Example 2:

# Input: [[7,10],[2,4]]
# Output: 1

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        if len(intervals) == 0:
            return 0
        rooms = [intervals[0]]
        max_rooms = 1
        for i in range(1, len(intervals)):
            for j in range(0, len(rooms)):
                if intervals[i][0] >= rooms[j][1]:
                    rooms[j] = intervals[i]
                    break
                elif j == len(rooms)-1:
                    rooms.append(intervals[i])
            max_rooms = max(max_rooms, len(rooms))
        
        return max_rooms
        