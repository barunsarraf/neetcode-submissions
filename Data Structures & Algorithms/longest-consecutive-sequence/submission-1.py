class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = []
        if not nums:
            return 0
        for k, v in enumerate(nums):
            res.append((k,v))
        res = sorted(res,key=lambda x: x[1])

        final_res = []
        print(res)
        for i in range(len(res)):
            temp = []
            curr_max_key = res[i][0]
            curr_max_value = res[i][1]
            temp.append(curr_max_value)
            for j in range(len(res)):
                if i!=j:
                    if res[j][1] == curr_max_value + 1:
                        curr_max_value = res[j][1]
                        temp.append(curr_max_value)
            if temp:
                final_res.append(temp)
                temp = []
        r = sorted(final_res,key=lambda x: len(x),reverse=True)
        return len(r[0])
            