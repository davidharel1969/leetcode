from collections import defaultdict
def get_word_count(words):
    ans=defaultdict(int)
    for word in words:
        ans[word]+=1
    return ans
def get_starts(s,words):
    def is_match(i):
        found_counter=defaultdict(int)
        for j in xrange(len(words)):
            found_word=s[i+j*word_len:i+(j+1)*word_len]
            if found_word not in word_counter:
                return False
            found_counter[found_word]+=1
            if (found_counter[found_word]>word_counter[found_word]):
                return False
        return True
            
        
    word_counter=get_word_count(words)
    word_len=len(words[0])
    for i in xrange(len(s)-word_len*len(words)+1):
        if is_match(i):
            yield i

        
    
    
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        return list(get_starts(s,words))

        