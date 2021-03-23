class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        result = []
        words = set(wordlist)
        words_cap, words_vowel = {}, {}
        
        def re_vowels(word):
            return "".join(['_' if c in 'aeiou' else c for c in word])
        
        for word in wordlist:
            wordlow = word.lower()
            wordlv = re_vowels(wordlow)
            if wordlow not in words_cap:
                words_cap[wordlow] = word
            if wordlv not in words_vowel:
                words_vowel[wordlv] = word
        
        def query_results(query):
            result = []
            for word in query:
                wordlow = word.lower()
                wordlv = re_vowels(wordlow)

                if word in words:
                    result.append(word)
                elif wordlow in words_cap:
                    result.append(words_cap[wordlow])
                elif wordlv in words_vowel:
                    result.append(words_vowel[wordlv])
                else:
                    result.append("")
            return result
        
        return query_results(queries)