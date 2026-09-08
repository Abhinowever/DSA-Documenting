class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        i = prev = 0
        l = len(chars)

        while i < l :
            curr = chars[i]
            start = i

            while i < l and curr == chars[i]:
                i += 1
            
            count = i - start

            chars[prev] = curr
            prev += 1

            if count > 1 :
                for digit in str(count) :
                    chars[prev] = digit 
                    prev += 1
                    
        return prev