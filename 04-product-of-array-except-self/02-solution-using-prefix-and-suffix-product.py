class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product_array = [1] * len(nums)
        prefix_product_dict = {0: nums[0]}
        for i in range(1,len(nums)):
            if i !=1 :    
                prefix_product_dict[i] = nums[i-1] * prefix_product_dict[i-1]
            else:
                prefix_product_dict[i] = nums[i-1]  
                
        suffix_product = 1
        print(prefix_product_dict)
        for j in range(len(nums)-1,-1,-1):
            # print(len(nums)-j,j,len(nums)-j-1)
            print(j,suffix_product)
            # print(prefix_product_dict[len(nums)-j-1])
            # print(product_array[j])            
            product_array[j] = prefix_product_dict[len(nums)-j-1] * suffix_product   
            suffix_product = suffix_product * nums[j]
        return product_array
#---------------------------        
nums = [1,2,3,4]
print(nums)                  
obj = Solution() 
output= obj.productExceptSelf(nums)
print(output)           