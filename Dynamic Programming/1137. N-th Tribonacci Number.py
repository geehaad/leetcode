class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        
         if n<=2:
            return (n+1)>>1
        else:
            f = [0]*(n+1)
            f[1],f[2]=1,1
            for i in range(3,len(f)):
                f[i] = f[i-1]+f[i-2]+f[i-3]
            return f[-1]
        
        