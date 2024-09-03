def candy(ratings):
    """
    :type ratings: List[int]
    :rtype: int
    """
    n = len(ratings)
    candies_list = [1] * n

    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies_list[i] = candies_list[i - 1] + 1

    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies_list[i] = max(candies_list[i], candies_list[i + 1] + 1)

    return sum(candies_list)
