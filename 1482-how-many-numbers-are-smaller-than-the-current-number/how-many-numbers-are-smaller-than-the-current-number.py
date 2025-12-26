class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        result=[]
        for i in range(len(nums)):
            min_count=0
            for j in range(len(nums)):
                if nums[i]>nums[j]:
                    min_count+=1
            result.append(min_count)
        return result

        """
        :type nums: List[int]
        :rtype: List[int]
        """
        