class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0,len(nums)-1):
            for j in range(i + 1,len(nums)):
                if nums[i] +  nums[j] == target:
                    return (i,j) 
nums = [2,7,11,15]
target = int('9')  
print(nums)                  
print(target)
obj = Solution() 
output= obj.twoSum(nums,target)
print(output)                  