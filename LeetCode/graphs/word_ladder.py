# Given two words beginWord and endWord, and a dictionary wordList, return the length of the shortest transformation sequence from beginWord to endWord, such that:

# Only one letter can be changed at a time.
# Each transformed word must exist in the word list.
# Return 0 if there is no such transformation sequence.

 

# Example 1:

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog", return its length 5.
# Example 2:

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        g = defaultdict(list)
        L = len(beginWord)
        
        for word in wordList:
            for i in range(L): 
                g[word[:i] + '_' + word[i+1:]].append(word)
                
        q = deque([(beginWord, 1)])
        seen = set()
        
        while q:
            word, path_len = q.popleft()
            if word == endWord:
                return path_len
            
            for i in range(L):
                new_word = word[:i] + '_' + word[i+1:]
                for nei in g[new_word]:
                    if nei not in seen:
                        seen.add(nei)
                        q.append((nei, path_len+1))

        return 0