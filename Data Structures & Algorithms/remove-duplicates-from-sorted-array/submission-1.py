class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        my_set = set()
        for num in nums:
            my_set.add(num)

        nums[:] = my_set
        nums.sort()
             
        return len(my_set)
        