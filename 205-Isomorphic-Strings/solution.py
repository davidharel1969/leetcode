class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s)!=len(t):
            return False
        mapping={}
        reverse_mapping={}
        n=len(s)
        for c,d in zip(s,t):
            exist_mapping=mapping.get(c,None)
            if exist_mapping is None:
                if (d in reverse_mapping):
                    return False
                mapping[c]=d
                reverse_mapping[d]=c
                
            else:
                if exist_mapping!=d:
                    return False
        return True
                
            
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        