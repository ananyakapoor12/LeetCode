class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        """for i in range (0,len(nums)):
            for j in range(i+1,len(nums)): #time limit exceeded - 0(n^2)
                if nums[i]==nums[j]:
                    return True
        
        return False"""

        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False