class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        output = 0
        c = ""
        for i in range(len(s)):
            if s[i] not in c:
                c += s[i]
            else:
                output = max(output,len(c))
                c = c[c.index(s[i])+1:]+s[i]
        output = max(output,len(c))
        return output