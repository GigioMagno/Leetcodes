class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        #Length of the words
        len1 = len(word1)
        len2 = len(word2)
        minimum = min([len1, len2])
        #output list
        output = []
        for i in range(minimum+1):
            try:
                output.append(word1[i])
            except:
                output.append(word2[i :])
                return "".join(output)
            try:
                output.append(word2[i])
            except:
                output.append(word1[i+1 :])
                return "".join(output)
            if len1 == len2 and i == minimum-1:
                return "".join(output)
            
            
