class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """        
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if((i!=j) and nums[i] == nums[j]):
                    print(nums[i], nums[j])
                    return True        
        return False
nums = [3,1,5,3,6,4]
print(nums)                  
obj = Solution() 
output= obj.containsDuplicate(nums)
print(output)           