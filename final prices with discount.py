'''
Given the array prices where prices[i] is the price of the ith item in a shop. There is a special discount for items in the shop, if you buy the ith item, then you will receive a discount equivalent to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i], otherwise, you will not receive any discount at all.

Return an array where the ith element is the final price you will pay for the ith item of the shop considering the special discount.
'''

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = [0]
        
        for i in range(1, len(prices)):
            while stack and prices[stack[-1]]>=prices[i]:
                index = stack.pop()
                prices[index] -= prices[i]
            
            stack.append(i)
        
        return prices