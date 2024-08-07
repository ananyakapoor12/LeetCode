#Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        k = k%n #if k>len of nums

        def reverse(start,end):
           while start<end:
              nums[start], nums[end] = nums[end], nums[start]
              start+=1
              end-=1
        
        reverse(0,n-1) #reverse whole array 
        reverse(0,k-1) #reverse first k elements
        reverse(k,n-1) #reverse n-k elements

        print(nums)

