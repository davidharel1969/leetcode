import collections
class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        self.loc=collections.defaultdict(list)
        for i,x in enumerate(words):
            self.loc[x].append(i)
        

    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        ans=10000000000
        for i in self.loc[word1]:
            for j in self.loc[word2]:
                ans=min(ans,abs(i-j))
        return ans


# Your WordDistance object will be instantiated and called as such:
# wordDistance = WordDistance(words)
# wordDistance.shortest("word1", "word2")
# wordDistance.shortest("anotherWord1", "anotherWord2")