class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        for i in range(len(strs[0])):
            for st in strs[1:]:
                if i == len(st) or st[i] != strs[0][i]:
                    return ans
            ans += strs[0][i]
        return ans