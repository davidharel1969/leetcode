def reverse(nums,left,right):
    mid=(right-left)/2
    for i in xrange(mid+1):
        nums[left+i],nums[right-i]=nums[right-i],nums[left+i]
    #print left,right,mid,nums
        


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        #print k
        reverse(nums,0,len(nums)-1)
        reverse(nums,0,k-1)
        reverse(nums,k,len(nums)-1)