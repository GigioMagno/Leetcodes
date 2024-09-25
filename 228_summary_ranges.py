class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        sequence = 1
        output = []
        l = len(nums)
        
        for i in range(l):
            if i+1 < l:
                if nums[i+1] - nums[i] == 1:
                    sequence += 1
                if sequence == 1:
                    output.append(str(nums[i]))
                elif sequence != 1 and nums[i+1] - nums[i] != 1:
                    output.append(str(nums[i-sequence+1]) + "->" + str(nums[i]))
                    sequence = 1
            else:
                if sequence == 1:
                    output.append(str(nums[i]))
                else:
                    output.append(str(nums[i-sequence+1]) + "->" + str(nums[i]))
        return output

       
