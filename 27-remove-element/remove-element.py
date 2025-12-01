class Solution:
    def removeElement(self, nums, val):
        k = 0  # index to place next non-val element

        for num in nums:
            if num != val:
                nums[k] = num
                k += 1

        return k
