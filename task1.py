class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_l = 1
        max_l = 1    

        for i in range(1, len(nums)):
            if(nums[i] > nums[i-1]):
                current_l += 1
            else:
                max_l = max(current_l, max_l)
                current_l = 1

        max_l = max(current_l, max_l)
        return max_l 