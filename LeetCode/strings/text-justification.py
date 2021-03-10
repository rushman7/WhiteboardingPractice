class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        start_word, end_word = 0, 0

        while start_word < len(words):
            curr_str = ''
            spaces, end_word, words_amount = self.get_words(start_word, end_word, words, maxWidth)
            
            # check line will contain more than 1 word
            if words_amount:
                if end_word == len(words): # check this is last line in word for left-justified edge case
                    start_word, curr_str = self.create_last_str(start_word, words_amount, spaces, curr_str, words)
                else: # non-last line words created
                    start_word, curr_str = self.create_str(start_word, words_amount, spaces, curr_str, words)
            else:
                curr_str += words[start_word] + spaces * ' '
                start_word += 1

            result.append(curr_str)

        return result
    
    # get total words in line, end word of line (first word in following line), and how many words are in this line
    def get_words(self, start_word, end_word, words, maxWidth):
        curr_count, spaces = 0, 0
        
        while end_word < len(words) and len(words[end_word]) + spaces + curr_count <= maxWidth:
            curr_count+=len(words[end_word])
            end_word+=1
            spaces+=1
        
        spaces += (maxWidth - curr_count - spaces)
        words_amount = end_word - start_word - 1
        return spaces, end_word, words_amount
    
    # build curr str to add to result and update our start_words index
    def create_str(self, start_word, words_amount, spaces, curr_str, words):
        while spaces:
            curr_str = curr_str + words[start_word] + ceil(spaces/words_amount)*' '
            spaces -= ceil(spaces/words_amount)
            words_amount-=1
            start_word+=1
            
        curr_str+=words[start_word]
        
        return start_word+1, curr_str
    
    # build curr str of last line to add to result and update our start_words index
    def create_last_str(self, start_word, words_amount, spaces, curr_str, words):
        while words_amount:
            curr_str += words[start_word] + ' '
            words_amount-=1
            start_word+=1
            spaces-=1
        curr_str += words[start_word] + spaces * ' '
        
        return start_word+1, curr_str