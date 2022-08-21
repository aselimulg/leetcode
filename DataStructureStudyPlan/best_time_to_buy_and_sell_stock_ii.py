# 122. Best Time to Buy and Sell Stock II
# medium
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
def maxProfit(prices):
	"""
	:type prices: List[int]
	:rtype: int
	"""
	max_profit = 0
	before = prices[0]
	
	for x in prices:
		if x - before > 0:
			max_profit += x - before
		
		before = x

	return max_profit

print(maxProfit([7,6,4,3,1]))