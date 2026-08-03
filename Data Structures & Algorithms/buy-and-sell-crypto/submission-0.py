class Solution:
   def maxProfit(self, prices: List[int]) -> int:
    cheapest = prices[0]
    best = 0

    for p in prices:
        profit_today = p - cheapest
        if profit_today > best:
            best = profit_today
        if p < cheapest:
            cheapest = p

    return best


        