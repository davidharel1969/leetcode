class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsofar=nums[0]
        maxendinghere=maxsofar
        for x in nums[1:]:
            maxendinghere=max(maxendinghere+x,x)
            maxsofar=max(maxsofar,maxendinghere)
        return maxsofar