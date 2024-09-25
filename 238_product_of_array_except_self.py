class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L = []
        R = []
        mult_l = 1
        mult_r = 1
        l = len(nums)
        ans = []

        for i in range(l):
            L.append(mult_l)
            mult_l = mult_l * nums[i]
        
        for i in range(l-1, -1, -1):
            R.append(mult_r)
            mult_r = mult_r * nums[i]

        for i in range(l):
            ans.append(L[i]*R[l-1-i])    
        
        return ans
