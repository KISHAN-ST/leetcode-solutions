class Solution(object):
    def buildArray(self, nums):
        result=[]
        for i in range(len(nums)):
            result.append(nums[nums[i]])
        return result
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        