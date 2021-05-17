class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x))
        dp_map = defaultdict(int)
        result = 0
        
        for word in words:
            dp_map[word] = self.get_chain(word, dp_map)
            result = max(result, dp_map[word])
        
        return result
                    
    def get_chain(self, word, dp_map):
        current_chain = 1
        
        for i in range(len(word)):
            edited_word = word[:i] + word[i+1:]
            
            if edited_word in dp_map:
                current_chain = max(current_chain, dp_map[edited_word] + 1)
                

        return current_chain