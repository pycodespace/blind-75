class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_purchases = prices[0]
        max_profit=0
        for i in range(1, len(prices)):
            if prices[i] < min_purchases:
                min_purchases = prices[i]
            elif max_profit< (prices[i]-min_purchases):
                max_profit = prices[i]-min_purchases
        return max_profit
        
prices = [7,1,5,3,6,4]
print(prices)                  
obj = Solution() 
output= obj.maxProfit(prices)
print(output)          