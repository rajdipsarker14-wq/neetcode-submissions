class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        new_target = 0
        i = 0

        for num in nums:
            if num in my_dict:
                my_dict[num].append(i)
            else:
                my_dict[num] = [i] 
            i += 1

        for key in my_dict:
            new_target = target - key
            if new_target in my_dict:
                if key == new_target:
                    if(len(my_dict[key]) > 1):
                        return [my_dict[key][0], my_dict[new_target][1]]
                else:
                    return [my_dict[key][0],my_dict[new_target][0]]




