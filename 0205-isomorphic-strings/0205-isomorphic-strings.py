class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        setA,setB = {},{}
        i,j = 1,1
        S,T = [],[]
        for x in s :
            if x not in setA:
                setA[x] = i
                i += 1
            S.append(setA[x])
        for x in t :
            if x not in setB :
                setB[x] = j
                j += 1
            T.append(setB[x])
        # print(S,T)
        return S == T