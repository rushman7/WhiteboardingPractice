# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]
 

# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lower-case English letters.

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    ans = [[(strs[0], Counter(strs[0]))]]
    for i in range(1, len(strs)):
        sCount = Counter(strs[i])
        
        added = False
        for j in range(len(ans)):
            if ans[j][0][1] == sCount:
                ans[j].append((strs[i], sCount))
                added = True
                break
        if not added:
            ans.append([(strs[i], sCount)])
    
    output = []
    
    for s in ans:
        res = []
        for t in s:
            res.append(t[0])
        output.append(res)
    return output