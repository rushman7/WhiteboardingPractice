# In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

# Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

 

# Example 1:

# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
# Example 2:

# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false
# Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
# Example 3:

# Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# Output: false
# Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hashMap = {letter:i for i,letter in enumerate(order)}
        
        for i in range(len(words)-1):
            if hashMap[words[i][0]] > hashMap[words[i+1][0]]:
                return False
            elif hashMap[words[i][0]] == hashMap[words[i+1][0]]:
                word_one = len(words[i])
                word_two = len(words[i+1])
                for j in range(min(word_one, word_two)):
                    if hashMap[words[i][j]] > hashMap[words[i+1][j]]:
                        return False
                    if hashMap[words[i][j]] < hashMap[words[i+1][j]]:
                        break
                    if j == word_two-1 and word_one > word_two:
                        return False
        return True
