class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remaining_value_needed = dict()
        for i in range(len(nums)):
            if nums[i] in remaining_value_needed:
                return [remaining_value_needed[nums[i]],i]
            else:
                remaining_value_needed[target-nums[i]] = i
        return [-1,-1]