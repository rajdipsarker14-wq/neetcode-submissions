class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        new_list = []
        for num in nums:
            if num != val:
                new_list.append(num)
                
        nums[:] = new_list
        return len(new_list)
                
        