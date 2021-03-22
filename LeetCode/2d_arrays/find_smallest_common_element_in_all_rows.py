class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        hash_map = defaultdict(int)
        
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                hash_map[mat[i][j]]+=1
                
        for keys in hash_map:
            if hash_map[keys] == len(mat):
                return keys
            
        return -1