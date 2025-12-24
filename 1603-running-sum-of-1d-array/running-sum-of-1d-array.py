class Solution(object):
    def runningSum(self, nums):
        result=[]
        sum=0
        for i in range(len(nums)):
            sum=sum+nums[i]
            result.append(sum)
        return result
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        