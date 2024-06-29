class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        my_dict ={}
        for i in range(0,len(nums)):  
            t=target-nums[i]
            if t in my_dict: 
                return (i,my_dict[t])            
            if nums[i] not in my_dict:
                my_dict[nums[i]]=i
                  
nums = [3,2,4]
target = int('6')  
print(nums)                  
print(target)
obj = Solution() 
output= obj.twoSum(nums,target)
print(output)                  