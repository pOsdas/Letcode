def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    profit = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit


# print(maxProfit([7, 1, 5, 3, 6, 4]))