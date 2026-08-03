class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_word = strs[0]
        for i in range(len(first_word)): 
            for j in range(1,len(strs)): 
                if i >= len(strs[j]) or first_word[i] != strs[j][i]: 
                    return first_word[:i]

        return first_word

    