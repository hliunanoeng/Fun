class Solution:
    def mincostTickets(self, days, costs):
        set_d = set(days)
        cost_cumu = [0] * (1 + days[-1])
        cost_cumu[0] = 0
        for i in range(1, days[-1] + 1):
            if i in set_d:
                d_pass = costs[0] + cost_cumu[i - 1]
                w_pass = costs[1] + cost_cumu[i - 7] if i - 7 >= 0 else costs[1]
                m_pass = costs[2] + cost_cumu[i - 30] if i - 30 >= 0 else costs[2]
                cost_cumu[i] = min(d_pass, w_pass, m_pass)
            else:
                cost_cumu[i] = cost_cumu[i - 1]

        # return
        return cost_cumu[-1]