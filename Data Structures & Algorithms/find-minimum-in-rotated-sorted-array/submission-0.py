class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return -1
        
        if len(nums)==1:
            return nums[0]
        
        if nums[0] < nums[-1]:
            return nums[0]
        
        def bs(arr, left, right):
            if left<=right:
                mid = left + (right-left)//2
                if mid > 0 and arr[mid-1]>arr[mid]:
                    return arr[mid]
                
                if arr[mid] > arr[right]:
                    return bs(arr,mid+1,right)
                else:
                    return bs(arr,left,mid-1)
            else:
                return -1

        return bs(nums,0,len(nums)-1)