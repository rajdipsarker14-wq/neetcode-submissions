class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        my_list = []
        second_list = []
        for i in range(len(t)):
            my_list.append(t[i])
        my_list.sort()

        for i in range(len(s)):
            second_list.append(s[i])
        second_list.sort()

        for i in range(len(s)):
            if my_list[i] != second_list[i]:
                return False
        return True
