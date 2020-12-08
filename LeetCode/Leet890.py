class Solution:
    def findAndReplacePattern(self, words, pattern):
        l = []
        for w in words:
            dic_p2w = {}
            dic_w2p = {}
            check = True
            for i in range(len(w)):
                if (pattern[i] in dic_p2w):
                    if (dic_p2w[pattern[i]] != w[i]):
                        check = False
                        break
                elif (w[i] in dic_w2p):
                    check = False
                    break
                else:
                    dic_p2w[pattern[i]] = w[i]
                    dic_w2p[w[i]] = pattern[i]
            if (check):
                l.append(w)
        return l