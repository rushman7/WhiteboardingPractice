class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        result, count = 0, Counter(arr)
        keys = sorted(count)
        n = len(keys)
        
        for i in range(n):
            result += self.three_sum(i, i, n-1, keys, count, target)
            
        return result % (10**9 + 7)
    
    def three_sum(self, i, j, k, keys, count, target):
        total = 0
        
        while j <= k:
            if keys[i] + keys[j] + keys[k] > target:
                k-=1
            elif keys[i] + keys[j] + keys[k] < target:
                j+=1
            else:
                x, y, z = keys[i], keys[j], keys[k]
                if x < y < z:
                    total += count[x] * count[y] * count[z]
                elif x == y < z:
                    total += count[x] * (count[y]-1) / 2 * count[z]
                elif x < y == z:
                    total += count[x] * count[y] * (count[z]-1) / 2
                else:
                    total += count[x] * (count[y]-1) * (count[z]-2) / 6
                k-=1
                j+=1

        return round(total)