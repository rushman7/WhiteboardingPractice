class Solution:
    def frequencySort(self, s: str) -> str:
        hash_map = Counter(s)
        max_freq = max(hash_map.values())
        buckets = [[] for _ in range(max_freq + 1)]
        
        for char, freq in hash_map.items():
            buckets[freq].append(char)
            
        result = []
        for i in range(len(buckets)-1, 0, -1):
            for char in buckets[i]:
                result.append(char * i)
                       
        return "".join(result)   