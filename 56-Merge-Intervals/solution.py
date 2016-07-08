	   # Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

def dot_in_interval(dot,interval):
	return dot>=interval.start and dot<=interval.end
def overlap(a,b):
    if dot_in_interval(a.start,b): return True
    if dot_in_interval(a.end,b): return True
    if dot_in_interval(b.start,a): return True
    if dot_in_interval(b.end,a): return True
    return False


class Solution(object):
    def find_start(self,val,start,end):
        if end-start<=0:
            return start
        pivot=(start+end)/2
        pivot_value=self.ans[pivot]
        if (val<pivot_value):
            return self.find_start(val,start,pivot)
        return self.find_start(val,pivot+1,end)
        
    def find_last(self,interval,start):
        #print self.ans,start,self.ans[start:]
        for i,x in enumerate(self.ans[start:],start):
            if interval.end<x.start:
                return i-1
        return len(self.ans)-1    
    def append(self,x):
        #print x,self.ans
        start=self.find_start(x.end,0,len(self.ans)-1)
        #print start
        for i in xrange(start,len(self.ans)):
            exist=self.ans[i]
            if x.end<exist.start:
                self.ans.insert(i, x)
                return
            if overlap(exist,x):
                last_index=self.find_last(x,i+1)
                last=self.ans[last_index]
                new_interval=Interval(min(exist.start,x.start),max(x.end,last.end))
                self.ans=self.ans[0:i]+[new_interval]+self.ans[last_index+1:]
                return
        self.ans.append(x)
            
        
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        self.ans=[]
        for x in intervals:
            self.append(x)
        return self.ans

