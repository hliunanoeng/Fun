class Solution(object):
    def lengthOfLongestSubstring(self, s: str) -> int:
        S = set()
        i_start = 0
        l = 0
        for i_finish in range(len(s)):
            while s[i_finish] in S:
                S.remove(s[i_start])
                i_start += 1
            S.add(s[i_finish])
            l_alt = i_finish-i_start+1
            l = max(l, l_alt)
        return l