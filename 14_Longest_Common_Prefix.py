class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = float('inf')
        prefix = ""

        for string in strs:
            if len(string) < min_length:
                min_length = len(string)
        
        flag = 0

        for i in range(min_length):
            curr_chr = strs[0][i]
            for string in strs:
                if string[i] != curr_chr:
                    flag = 1
            if flag == 0:
                prefix = prefix + curr_chr
            
            if flag == 1:
                return prefix
        
        return prefix


                
