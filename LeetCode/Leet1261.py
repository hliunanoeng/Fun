from collections import deque

class TreeNode(object):
    def __init__(self, marker, val, left=None, right=None):
        self.marker = marker
        self.val = val
        self.left = left
        self.right = right

class FindElements(object):

    def __init__(self, treedata):
        self.treedata = treedata
        self.record = []
        self.n = iter(treedata)
        self.mytree = TreeNode(next(self.n),0)
        self.l = deque([self.mytree])
        self.recovery()

    def recovery(self):
        while len(self.l)>=1:
            head = self.l.popleft()
            try:

                left_i = next(self.n)
                if left_i == -1:
                    head.left = TreeNode(-1,(2*head.val)+1)
                    self.record.append((2*head.val)+1)
                    self.l.append(head.left)
                else:
                    head.left = TreeNode("x","NA")

                right_i = next(self.n)
                if right_i == -1:
                    head.right = TreeNode(-1, (2 * head.val) + 2)
                    self.record.append((2 * head.val) + 2)
                    self.l.append(head.right)
                else:
                    head.right = TreeNode("x", "NA")

            except StopIteration:
                break

    def find(self,target):
        a = target in self.record
        print(a)

test = [-1,"x",-1,-1,"x",-1]
t = FindElements(test)
