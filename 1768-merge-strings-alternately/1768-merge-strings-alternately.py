class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = []

        for a, b in zip(word1, word2):
            result.extend((a, b))

        result.append(word1[len(result)//2:])
        result.append(word2[len(result)//2:])

        return "".join(result)