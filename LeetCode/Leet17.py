class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = [0, 0, 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

        s = []
        for i in digits:
            s.append(mapping[int(i)])

        from itertools import product

        if len(s) == 0:
            return []

        combinations = list(product(*s))

        results = []
        for i in combinations:
            results.append(''.join(list(i)))

        return (results)

