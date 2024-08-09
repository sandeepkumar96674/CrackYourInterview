class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        curr = gas[-1] - cost[-1]
        min_gas = curr
        min_index = 0
        for i in range(0, len(gas)-1):
            curr += gas[i] - cost[i]
            if curr < min_gas:
                min_gas = curr
                min_index = i+1
        return min_index if curr >= 0 else -1