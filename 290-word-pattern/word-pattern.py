class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split()
        
        # Lengths must match
        if len(pattern) != len(words):
            return False
        
        mapPT = {}
        mapTP = {}
        
        for p, w in zip(pattern, words):
            
            # Check pattern -> word mapping
            if p in mapPT:
                if mapPT[p] != w:
                    return False
            else:
                mapPT[p] = w
            
            # Check word -> pattern mapping
            if w in mapTP:
                if mapTP[w] != p:
                    return False
            else:
                mapTP[w] = p
        
        return True
