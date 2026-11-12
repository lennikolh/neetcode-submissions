class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        seen = {}

        for num in nums:
            seen[num] = seen.get(num, 0) + 1
        
        result = []

        for i in range(k):
            max_num = max(seen, key=seen.get)
            result.append(max_num)
            seen.pop(max_num)
        
        return result
    
        
