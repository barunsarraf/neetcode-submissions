class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def helper(start,target,path):
            if target==0:
                res.append(path.copy())
                return

            if target<0:
                return

            for i in range(start,len(nums)):

                curr = nums[i]

                path.append(curr)

                helper(i,target-curr,path)

                path.pop()

        helper(0,target,[])
        return res