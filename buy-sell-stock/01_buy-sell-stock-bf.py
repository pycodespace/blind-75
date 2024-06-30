class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit=0
        for i in range(0, len(prices)-1):
            for j in range(i+1, len(prices)):
                if (prices[j]-prices[i]) > max_profit:
                   max_profit = prices[j]-prices[i]
        return max_profit
        
prices = [7,1,5,3,6,4]
print(prices)                  
obj = Solution() 
output= obj.maxProfit(prices)
print(output)          