# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        res = 0

        q = deque()
        q.append((root, root.val))

        while q:

            for i in range(len(q)):
                node, maxval = q.popleft()
                if node and node.val >= maxval:
                    res += 1
                if node:
                    q.append((node.left, max(node.val, maxval)))
                    q.append((node.right, max(node.val, maxval)))
        return res
                            