class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i=0
        j=0
        length=len(nums)
        while j<length:
            if nums[j]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
            j+=1
            
        