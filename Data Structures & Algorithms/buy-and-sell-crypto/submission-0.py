class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        if not prices:
            return max_profit

        curr_max = prices[-1]

        for i in range(len(prices)-2,-1,-1):

            if curr_max>prices[i]:
                curr_profit = curr_max- prices[i]
                max_profit = max(curr_profit,max_profit)

            curr_max = max(curr_max,prices[i])

        return max_profit