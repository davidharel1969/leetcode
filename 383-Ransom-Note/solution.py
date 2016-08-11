from collections import defaultdict
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazine_counter=defaultdict(int)
        ransom_counter=defaultdict(int)
        for x in ransomNote:
            ransom_counter[x]+=1
        for x in magazine:
            magazine_counter[x]+=1
        for x,count in ransom_counter.iteritems():
            if (magazine_counter[x]<count):
                return False
        return True