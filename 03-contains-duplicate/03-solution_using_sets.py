class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """ 
        alreay_traversed = set()       
        for i in range(0,len(nums)):
            print(nums[i],i)
            print(alreay_traversed)
            if nums[i] in alreay_traversed:
                return True
            else:
                alreay_traversed.add(nums[i])
        return False
nums = [3,3]
print(nums)                  
obj = Solution() 
output= obj.containsDuplicate(nums)
print(output)           