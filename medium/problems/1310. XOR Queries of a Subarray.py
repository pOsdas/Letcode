def xorQueries(arr, queries):
    """
    :type arr: List[int]
    :type queries: List[List[int]]
    :rtype: List[int]
    """
    n = len(arr)
    prefix_xor = [0] * n
    prefix_xor[0] = arr[0]

    for i in range(1, n):
        prefix_xor[i] = prefix_xor[i - 1] ^ arr[i]

    result = []
    for left, right in queries:
        if left == 0:
            result.append(prefix_xor[right])
        else:
            result.append(prefix_xor[right] ^ prefix_xor[left - 1])

    return result
