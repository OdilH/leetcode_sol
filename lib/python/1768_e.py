class Solution:
    def mergeAlternately(self, word1: str, word2:str) -> str:
        l = ""
        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                l += word1[i]
            if i < len(word2):
                l += word2[i]
        return l

sol = Solution()
print(sol.mergeAlternately("abc","cbd"))
