import typing

class Solution(object):
    def twoCitySchedCost(self, costs: typing.List[typing.List[int]]) -> int:
        l_sorted = sorted(costs, key=lambda x: x[0] - x[1])
        result = 0
        for i in range(len(costs)):
            if i < len(costs) / 2:
                result += l_sorted[i][0]
            else:
                result += l_sorted[i][1]

        return result


