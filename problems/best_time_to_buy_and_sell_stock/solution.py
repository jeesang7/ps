class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = float('inf')
        maxprofit = 0
        
        for p in prices:
            if p < minprice:
                minprice = p
            elif maxprofit < (p - minprice):
                maxprofit = p - minprice
            else:
                pass
        
        print(maxprofit)
        return maxprofit
        
        '''
        # Time Limit Exceeded: O(n^2)
        input_len = len(prices)        
        
        profit = 0
        output = 0
         
        for idx, val in enumerate(prices):
            for p in prices[idx:]:
                if prices[idx] < p:
                    # print(prices[idx], p)
                    profit = p - prices[idx]
                    if output < profit:
                        output = profit
        
        print(output)
        return output
        '''