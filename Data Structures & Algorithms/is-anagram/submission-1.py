class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_dict = {}
        second_dict = {}

        if len(s) != len(t):
            return False

        for char in t:
            if char in my_dict:
                my_dict[char] += 1
            else:
                my_dict[char] = 1

        for char in s:
            if char in second_dict:
                second_dict[char] += 1
            else:
                second_dict[char] = 1
        if second_dict != my_dict:
            return False
        
        return True

    


