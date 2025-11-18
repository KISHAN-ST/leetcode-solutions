class Solution:
    def firstUniqChar(self, s):
        freq = {}

        # Step 1: Count frequency
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        # Step 2: Find the first char with frequency 1
        for i, ch in enumerate(s):
            if freq[ch] == 1:
                return i

        return -1
