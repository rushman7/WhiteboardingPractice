class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        hash_map = {}
        
        for i, char in enumerate(S):
            if char not in hash_map:
                hash_map[char] = (i, i)
            else:
                hash_map[char] = (hash_map[char][0], i)
                
        curr_tuple = None

        res = []
        for char in hash_map:
            if not curr_tuple:
                curr_tuple = hash_map[char]
            else:
                if hash_map[char][0] < curr_tuple[1]:
                    prev_min = curr_tuple[0]
                    new_max = max(curr_tuple[1], hash_map[char][1])
                    curr_tuple = (prev_min, new_max)
                else:
                    left, right = curr_tuple
                    res.append(right-left+1)
                    curr_tuple = hash_map[char]
                    
        left, right = curr_tuple
        res.append(right-left+1)
        
        return res
