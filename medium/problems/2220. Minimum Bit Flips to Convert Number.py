def minBitFlips(start, goal):
    """
    :type start: int
    :type goal: int
    :rtype: int
    """
    count = 0
    start, goal = bin(start)[2:], bin(goal)[2:]
    if len(start) < len(goal):
        while len(start) != len(goal):
            start = '0' + start

    if len(goal) < len(start):
        while len(goal) != len(start):
            goal = '0' + goal

    start = list(start)
    goal = list(goal)
    for i in range(len(start)):
        if start[i] != goal[i]:
            start[i] = goal[i]
            count += 1

    return count
