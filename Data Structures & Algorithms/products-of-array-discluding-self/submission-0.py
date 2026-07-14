class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count_zero = 0
        result = []
        current_prod = 1
        for num in nums:
            if num==0:
                count_zero+=1
            else:
                current_prod*=num

        
        for num in nums:
            if count_zero==1 and num!=0:
                result.append(0)
            elif count_zero==1 and num==0:
                result.append(current_prod)
            elif count_zero>1:
                result.append(0)
            else:
                result.append(current_prod//num)
        return result