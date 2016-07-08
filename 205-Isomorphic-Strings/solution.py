class Solution(object):
    def isIsomorphic(self, s, t):
        if (len(s)!=len(t)):
            return False
        mapping={}
        reverse_mapping={}
        n=len(s)
        for i in range(n):
            c=s[i]
            d=t[i]
            exist_mapping=mapping.get(ord(c),None)
            if (exist_mapping==None):
                if (reverse_mapping.get(ord(d),None)!=None):
                    return False
                mapping[ord(c)]=d
                reverse_mapping[ord(d)]=c
                
            else:
                if exist_mapping!=d:
                    return False
        return True
                
            
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        