class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        a,b = list(set(word1)),list(set(word2))
        # print(sorted(a),sorted(b))
        if len(word1) != len(word2) :
            return False
        if  sorted(a) != sorted(b) :
            return False
        x,y = [],[]
        for i in range(len(a)) :
            x.append(word1.count(a[i]))
            y.append(word2.count(b[i]))
        x.sort()
        y.sort()
        for i in range(len(x)):
            if x[i] != y[i]:
                return False
        return True