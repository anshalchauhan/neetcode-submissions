class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # O(n + m) solution
        hashmap_s = {}
        hashmap_t = {}

        for char in s:
            if char in hashmap_s:
                hashmap_s[char] += 1
            else: 
                hashmap_s[char] = 1

        for char in t:
            if char in hashmap_t:
                hashmap_t[char] += 1
            else:
                hashmap_t[char] = 1

        if len(hashmap_t) != len(hashmap_s):
            return False
        
        for key, value in hashmap_s.items():
            if key not in hashmap_t:
                return False
            else:
                if hashmap_t[key] != value:
                    return False
        
        return True