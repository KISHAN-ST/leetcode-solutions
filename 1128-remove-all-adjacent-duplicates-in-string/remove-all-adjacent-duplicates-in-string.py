class Solution(object):
    def removeDuplicates(self, s):
        stack=[]
        top=-1
        for ch in s:
            if top>=0 and stack[top]==ch:
                stack.pop()
                top-=1
            else:
                stack.append(ch)
                top+=1
        return "".join(stack)
        """
        :type s: str
        :rtype: str
        """
        