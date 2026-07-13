class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            if num in d:
                d[num]+=1
            else:
                d[num]=1
        freq = list(d)

        result = sorted(d.items(),key=lambda x: x[1], reverse=True)
        
        return [result[k][0] for k in range(k)]