class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        t = -1
        result = [None] *len(s)
        for i in range(len(s)):
            result[i] = s[t]
            t -= 1
        s[:] = result