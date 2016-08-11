class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start=0
        cur=set()
        maxsofar=0
        for i,x in enumerate(s):
            if (x not in  cur):
                cur.add(x)
                maxsofar=max(maxsofar,i-start+1)
                #print x,cur
            else:
                for j in xrange(start,i):
                    y=s[j]
                    if (y==x):
                        start=j+1
                        break
                    else:
                        cur.remove(y)
                    
        return maxsofar
            

                
                