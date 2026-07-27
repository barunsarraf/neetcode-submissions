class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()

        for i in range(len(nums)):
            j = i+1
            k=len(nums)-1
            while j<k:
                new_sum = nums[i]+nums[j]+nums[k]
                if new_sum==0:
                    result.add((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1
                elif new_sum<0:
                    j+=1
                else:
                    k-=1
        return list(result)