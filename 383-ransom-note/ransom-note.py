class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        freqMag = {}
        
        # Count magazine letters
        for ch in magazine:
            freqMag[ch] = freqMag.get(ch, 0) + 1
        
        # Check ransomNote requirements
        for ch in ransomNote:
            if ch not in freqMag or freqMag[ch] == 0:
                return False
            freqMag[ch] -= 1
        
        return True
