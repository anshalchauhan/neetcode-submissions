class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # bruteforce solution
        ans = ""
        j = 0
        min_length = len(strs[0])
        for st in strs:
            min_length = min(len(st), min_length)

        while min_length > j:
            char = strs[0][j]
            for i in range(1, len(strs)):
                if strs[i][j] != strs[i-1][j]:
                    return ans;
            ans += char
            j += 1
        return ans