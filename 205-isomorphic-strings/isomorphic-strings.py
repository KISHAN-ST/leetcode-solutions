class Solution(object):
    def isIsomorphic(self, s, t):
        mapST = {}
        mapTS = {}
        
        for i in range(len(s)):
            c1, c2 = s[i], t[i]
            
            # Check s -> t mapping
            if c1 in mapST:
                if mapST[c1] != c2:
                    return False
            else:
                mapST[c1] = c2
            
            # Check t -> s mapping
            if c2 in mapTS:
                if mapTS[c2] != c1:
                    return False
            else:
                mapTS[c2] = c1
        
        return True
