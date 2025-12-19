class Solution(object):
    def mostWordsFound(self, sentences):
        max_len = 0

        for sentence in sentences:
            word_count = len(sentence.split(" "))
            max_len = max(max_len, word_count)

        return max_len
