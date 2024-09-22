class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        start_index = current_gas = 0

        for i in range(len(gas)):
            current_gas += gas[i] - cost[i]

            if current_gas < 0:
                start_index = i + 1
                current_gas = 0

        return start_index


# s = Solution()
# print(s.canCompleteCircuit(gas=[2,3,4], cost=[3,4,3]))
