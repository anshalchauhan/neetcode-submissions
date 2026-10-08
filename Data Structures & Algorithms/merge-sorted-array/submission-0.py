class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        merge_list = []
        i, j = 0, 0
        while i < m and j < n:
            if nums1[i] > nums2[j]:
                merge_list.append(nums2[j])
                j += 1
            else:
                merge_list.append(nums1[i])
                i += 1
        
        while i < m:
            merge_list.append(nums1[i])
            i += 1
        
        while j < n:
            merge_list.append(nums2[j])
            j += 1
        
        for i in range(0, m + n):
            nums1[i] = merge_list[i]