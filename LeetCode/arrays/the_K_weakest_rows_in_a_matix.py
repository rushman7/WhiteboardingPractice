class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        result = []
        
        for j in range(len(mat[0])):
            for i in range(len(mat)):
                if mat[i][j] == 0 and (mat[i][j-1] != 0 if j > 0 else True):
                    result.append(i)
                    if len(result) == k:
                        return result
        i = 0 
        while len(result) < k:
            if mat[i][-1] == 1:
                result.append(i)
            i+=1
        return result