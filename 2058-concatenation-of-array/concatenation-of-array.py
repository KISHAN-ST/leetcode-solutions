class Solution(object):
    def getConcatenation(self, nums):
        curr_length=len(nums)
        for i in range(curr_length):
            nums.append(nums[i])
        return nums
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        