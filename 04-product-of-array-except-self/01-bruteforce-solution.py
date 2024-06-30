class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product_array = []
        for i in range(0,len(nums)):
            product_i=1
            for j in range(0,len(nums)):
                if(i!=j):
                    product_i =product_i * nums[j]
            product_array.insert(i,product_i)
        return product_array
        
nums = [1,1,5]
print(nums)                  
obj = Solution() 
output= obj.productExceptSelf(nums)
print(output)           