class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_frequency_map = {}
        for num in nums:
            num_frequency_map[num] = num_frequency_map.get(num, 0) + 1
        top_k_elements = []
        for num, frequency in num_frequency_map.items():
            heappush(top_k_elements, (frequency, num))
            if len(top_k_elements) > k:
                heappop(top_k_elements)
        top_numbers = []
        while top_k_elements:
            top_numbers.append(heappop(top_k_elements)[1])
        return top_numbers