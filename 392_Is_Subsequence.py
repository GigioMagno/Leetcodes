class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        S = len(s)
        T = len(t)
        j = 0

        if s == "":
            return True
        
        for i in range(T):
            if t[i] == s[j]:
                if j == S-1:
                    return True
                j+=1
        
        return False


