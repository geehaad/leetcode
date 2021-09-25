class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(numbers) == 2:
            return [1,2]
        
        i = 0
        lenn = len(numbers)-1
        res = 0
        
        while True:
            res = numbers[i]+numbers[lenn]
            
            if target == res:
                return [i+1,lenn+1]
            
            elif target < res:
                lenn-=1
                
            elif target > res:
                i+=1
               
        
        
            
                
        