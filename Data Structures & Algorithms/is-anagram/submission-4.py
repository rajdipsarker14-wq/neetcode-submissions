class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_dict = {}

        for char in t:
            if char in my_dict:
                my_dict[char] += 1
            else:
                my_dict[char] = 1

        for char in s:
            if char in my_dict:
                my_dict[char] -= 1
            else:
                return False

        if all(value == 0 for value in my_dict.values()):
            return True

        return False