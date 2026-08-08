class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def bs(arr,left,right):
            if left<=right:
                mid = left + (right-left)//2
                if mid < 0 or mid >= len(arr):
                    return -1
                if arr[mid]==target:
                    return mid
                if target>arr[mid]:
                    return bs(arr,mid+1,right)
                else:
                    return bs(arr,left,mid-1)
            else:
                return -1

        def findPivot(arr,left,right):
            if left<right:
                mid = left + (right-left)//2

                if mid>0 and arr[mid-1]>arr[mid]:
                    return mid

                if arr[mid]>arr[right]:
                    return findPivot(arr,mid+1,right)
                else:
                    return findPivot(arr,left,mid-1)
            else:
                return left
        if not nums:
            return -1
        
        if len(nums)==1:
            if nums[0]==target:
                return 0
            else:
                return -1
        
        if nums[0]<nums[-1]:
            return bs(nums,0,len(nums)-1)
        else:
            pivot = findPivot(nums,0,len(nums)-1)
            if target >= nums[0]:
                return bs(nums, 0, pivot - 1)
            else:
                return bs(nums, pivot, len(nums) - 1)