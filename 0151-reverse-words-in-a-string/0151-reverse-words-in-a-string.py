class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # S = ""
        # words = str(s).split(" ")
        # for i in reversed(words):
        #     if i == "":
        #         continue
        #     S = S + i + " "
        # return S[:-1]

        return " ".join(s.split()[::-1])