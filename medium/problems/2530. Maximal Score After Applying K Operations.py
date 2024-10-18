import heapq

def maxScore(nums, k):
    max_heap = [-num for num in nums]
    heapq.heapify(max_heap)

    score = 0

    for i in range(k):
        max_val = -heapq.heappop(max_heap)
        score += max_val

        new_val = (max_val + 2) // 3
        heapq.heappush(max_heap, -new_val)

    return score
