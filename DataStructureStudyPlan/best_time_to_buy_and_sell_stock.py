# 121. Best Time to Buy and Sell Stock
# easy
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

def maxProfit(prices):
	"""
	:type prices: List[int]
	:rtype: int
	"""
	max_profit = 0
	start = prices[0]
	for x in prices:
		if max_profit < x - start:
			max_profit = x - start
		if x < start:
			start = x
		
	return max_profit