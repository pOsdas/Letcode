def hIndex(citations):
    citations.sort(reverse=True)
    # print(citations)

    h_index = 0

    for i in range(len(citations)):
        if citations[i] >= i + 1:
            h_index = i + 1
        else:
            break

    return h_index


print(hIndex([3, 0, 6, 1, 5]))
# 6 5 3 1 0
