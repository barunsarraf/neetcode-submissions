class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s_set = set()
        for num in nums:
            if num in s_set:
                return True
            else:
                s_set.add(num)
        return False