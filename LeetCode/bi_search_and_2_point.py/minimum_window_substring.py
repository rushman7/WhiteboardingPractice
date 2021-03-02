class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hash_map, hash_set, char_map = defaultdict(int), set(t), Counter(t)
        L, R, formed, r_L, r_R = 0, 0, 0, 0, 0
        min_len = len(s)
        
        while R <= len(s):
            while formed == len(hash_set):
                temp = s[L]
                if R-L <= min_len:
                    min_len, r_L, r_R = R-L, L, R
                if temp in hash_set:
                    hash_map[temp]-=1
                    if hash_map[temp] < char_map[temp]:
                        formed-=1
                L+=1
            if R >= len(s): break
            val = s[R]
            if val in hash_set:
                hash_map[val]+=1
                if hash_map[val] == char_map[val]:
                    formed+=1
            R+=1
        return s[r_L:r_R] if len(hash_map) == len(hash_set) else ""