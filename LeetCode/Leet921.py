class Solution(object):
    def minAddToMakeValid(self, S):
        l, r= 0, 0
        for c in S:
            if c == '(':
                l += 1
            elif c == ')':
                if l > 0:
                    l -= 1
                else:
                    r += 1
        return l + r