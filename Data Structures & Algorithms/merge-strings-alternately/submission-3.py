class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        longer_word = ""
        shorter_word = ""
        result = ""
        i = 0

        if len(word1) > len(word2):
            longer_word = word1
            shorter_word = word2
        else:
            longer_word = word2
            shorter_word = word1
    
        while i < len(shorter_word) and word1 == longer_word:
            result += longer_word[i]
            result += shorter_word[i]
            if i == len(shorter_word)-1:
                break
            i += 1

        while i < len(shorter_word) and word2 == longer_word:
            result += shorter_word[i]
            result += longer_word[i]
            if i == len(shorter_word)-1:
                break
            i += 1

        i+=1
        
        while i < len(longer_word):
            result += longer_word[i]
            i += 1
        
        return result
        

        