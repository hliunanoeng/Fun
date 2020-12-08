class Solution(object):
    def longestPalindrome(self, s):
        if len(s) == 1:
            return s
        output = ""
        for i in range(len(s)):
            output = max(output, self.Palindrome(s, i, i), self.Palindrome(s, i, i+1),key=len)
        return output

    def Palindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]