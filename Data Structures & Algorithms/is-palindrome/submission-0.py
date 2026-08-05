class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left = 0
        right = len(s)-1

        while left < right:
            if s[left].isalnum() != True:
                left += 1
                continue
            if s[right].isalnum() != True:
                right -= 1
                continue
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True
            