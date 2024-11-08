class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        s1, s2, s = m - 1, n - 1, m + n - 1

        while s1 >= 0 and s2 >= 0:
            if nums1[s1] > nums2[s2]:
                nums1[s] = nums1[s1]
                s1 -= 1
            else:
                nums1[s] = nums2[s2]
                s2 -= 1
            s -= 1

        while s2 >= 0:
            nums1[s] = nums2[s2]
            s2 -= 1
            s -= 1