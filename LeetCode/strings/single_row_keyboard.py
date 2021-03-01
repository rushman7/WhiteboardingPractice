class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        hash_map = defaultdict(int)
        result, curr = 0, 0
        for i in range(len(keyboard)):
            hash_map[keyboard[i]] = i
        for char in word:
            val = hash_map[char]
            result += abs(curr - val)
            curr = val
        return result