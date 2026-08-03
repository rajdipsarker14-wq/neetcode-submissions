class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        my_dict = {}

        for num in nums:
            if num in my_dict:
                my_dict[num]+= 1
            else:
                my_dict[num] = 1

        highest = 0
        for key in my_dict:
            if my_dict[key]> highest:
                highest = my_dict[key]
                answer = key

        return answer