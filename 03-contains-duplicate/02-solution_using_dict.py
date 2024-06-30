class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """ 
        alreay_traversed ={}       
        for i in range(0,len(nums)):
            if nums[i] in alreay_traversed:
                return True
            else:
                alreay_traversed[nums[i]]=i       
        return False
nums = [3,1,5,3,6,4]
print(nums)                  
obj = Solution() 
output= obj.containsDuplicate(nums)
print(output)           