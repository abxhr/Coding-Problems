# Author: Abshar Mohammed Aslam

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = left + 1
        max_profit = 0
        while right < len(prices):
            curr_profit = prices[right] - prices[left]
            if prices[left] < prices[right]:
                max_profit = max(max_profit, curr_profit)
            else:
                left = right
            right += 1
        return max_profit
