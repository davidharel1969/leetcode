class Solution(object):
    def bsearch(self,left,right,level):
        print ' '*level,left,right
        if right-left<4:
            for i in xrange(left,right+1):
                if self.nums[i]==self.target:
                    return i
            return -1
        pivot=(left+right)/2
        pivot_value=self.nums[pivot]
        print ' '*level,'>',pivot,pivot_value
        if self.target==pivot_value:
            return pivot
        if self.nums[left]<pivot_value:
            if self.target<pivot_value and self.nums[left]<=self.target:
                return self.bsearch(left,pivot,level+1)
            else:
                return self.bsearch(pivot,right,level+1)
        else:
            if pivot_value<=self.target and self.target<=self.nums[right]:
                return self.bsearch(pivot,right,level+1)
            else:
                return self.bsearch(left,pivot,level+1)
            
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        self.nums=nums
        self.target=target
        return self.bsearch(0,len(nums)-1,0)