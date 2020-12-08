class Solution(object):

    def __init__(self):
        self.d = dict()

    def findLatestStep(self, arr, m):
        s= len(arr)
        init = [0] * (s + 2)
        ii = -1

        if s == m:
            return m

        for i, n in enumerate(arr, 1):
            l = init[n-1]
            r = init[n+1]
            l_sum = l+r+1
            init[(n-l):(n+r+1)] = l_sum*[l_sum]

            self.get_d(l_sum)
            self.set_d(l_sum,1)
            self.get_d(l)
            self.set_d(l, -1)
            self.get_d(r)
            self.set_d(r, -1)

            if self.get_d(m)>0:
                ii=i

        return ii

    def get_d(self,v):
        if v in self.d.keys():
            return self.d[v]
        else:
            self.d[v] = 0
            return self.d[v]

    def set_d(self,k,v):
        self.d[k] = self.d[k]+v


