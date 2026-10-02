class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # O(nlogn + mlogm) solution
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        return sorted_s == sorted_t