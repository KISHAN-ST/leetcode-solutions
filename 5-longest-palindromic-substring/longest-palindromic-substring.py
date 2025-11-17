class Solution(object):
   
 
 def longestPalindrome(self, s):
      large=""
      n=len(s)
      for i in range(n+1):
        for j in range(i+1,n+1):
            k=s[i:j]
            if k==k[::-1] and (len(k)>len(large)):
                large=k
      return large



