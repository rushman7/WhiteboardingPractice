class TimeMap:
    def __init__(self):
        self.time_map = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map or timestamp < self.time_map[key][0][0]:
            return ""
        arr = self.time_map[key]
        left, right = 0, len(arr)-1

        while left <= right:
            mid = (left + right) // 2
            if arr[mid][0] == timestamp:
                return arr[mid][1]
            if arr[mid][0] > timestamp:
                right = mid - 1
            else:
                left = mid + 1

        return arr[right][1]