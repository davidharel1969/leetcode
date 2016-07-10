import collections
class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.the_set=collections.defaultdict(int)
        

    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        self.the_set[number]+=1
        
        

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        #print self.the_set
        for x in self.the_set:
            other=value-x
            if other in self.the_set and (x!=other or self.the_set[x]>1):
                return True
        return False
        

# Your TwoSum object will be instantiated and called as such:
# twoSum = TwoSum()
# twoSum.add(number)
# twoSum.find(value)