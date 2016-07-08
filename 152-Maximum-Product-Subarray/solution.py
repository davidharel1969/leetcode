class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsofar=nums[0]
        maxendinghere=nums[0]
        minendinghere=nums[0]
        #print maxsofar,maxendinghere,minendinghere
        for i,x in enumerate(nums[1:]):
            maxendinghere,minendinghere=max(x,maxendinghere*x,minendinghere*x),min(x,maxendinghere*x,minendinghere*x)
            
            maxsofar=max(maxsofar,maxendinghere)
            #print x,maxsofar,maxendinghere,minendinghere
        return maxsofar
                
                