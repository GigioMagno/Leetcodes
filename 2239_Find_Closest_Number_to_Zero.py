class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        minimum = nums[0]
        for element in nums:
            if abs(element) < abs(minimum):
                minimum = element

        if abs(minimum) in nums:
            return abs(minimum)
        else:
            return minimum
        
        
