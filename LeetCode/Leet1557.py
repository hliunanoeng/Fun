class Solution(object):
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        dest_set = set()
        for i in edges:
            dest_set.add(i[1])

        iso_set = set(list(range(n))).difference(dest_set)
        return list(iso_set)