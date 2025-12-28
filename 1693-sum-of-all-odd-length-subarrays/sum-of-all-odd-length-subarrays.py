class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        total = 0
        n = len(arr)

        for i in range(n):
            left = i + 1
            right = n - i
            odd_count = (left * right + 1) // 2
            total += arr[i] * odd_count

        return total
