from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck):
        ans = [0]*len(deck)
        idx = deque(range(len(deck)))
        for x in sorted(deck):
            ans[idx.popleft()] = x
            if idx:
                idx.append(idx.popleft())
        return ans