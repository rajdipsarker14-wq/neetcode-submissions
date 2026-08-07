# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val         
        self.next = next
    
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        nums = []
        result = []
        while current is not None:
            nums.append(current.val)
            current = current.next

        start = len(nums)-1
        while start >= 0:
            result.append(nums[start])
            start -= 1
        if(len(result) > 0):
            head = ListNode(result[0])
            current = head
        else:
            current = head
            return head

        for i in range(1,len(result)):
            current.next = ListNode(result[i])
            current = current.next
    
        return head





        
        