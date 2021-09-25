class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        h = 0
        s = list(s)
        for i in range(len(s)):
            if(s[i]==' '):
                s[h:i] = reversed(s[h:i])
                h = i+1
                
            elif(i==len(s)-1):
                s[h:i+1] = reversed(s[h:i+1])
                
        return "".join(s)
            
                