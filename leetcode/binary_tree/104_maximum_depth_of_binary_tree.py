"""
104. 二叉树的最大深度（Maximum Depth of Binary Tree）
难度：简单
链接：https://leetcode.cn/problems/maximum-depth-of-binary-tree/

【题目】
给定一个二叉树 `root`，返回其最大深度。

二叉树的最大深度是指从根节点到最远叶子节点的最长路径上的节点数。

【示例】
示例 1：
    输入：root = [3,9,20,null,null,15,7]
    输出：3

示例 2：
    输入：root = [1,null,2]
    输出：2

【约束】
- 树中节点的数量在 `[0, 10^4]` 区间内
- `-100 <= Node.val <= 100`
"""

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_depth = 0
        queue = deque([root])
        while queue:
            max_depth += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return max_depth


# ============ 感悟 ============
# 思路：
#
# 复杂度：时间 O( )  空间 O( )
#
# 易错点 / 收获：
#


# ============ 测试用例 ============
def build_tree(values: list[Optional[int]]) -> Optional[TreeNode]:
    """层序列表（LeetCode 格式，None 表示空节点）-> 二叉树。"""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


def to_list(root: Optional[TreeNode]) -> list[Optional[int]]:
    """二叉树 -> 层序列表（LeetCode 格式，去掉末尾多余的 None）。"""
    if not root:
        return []
    res: list[Optional[int]] = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node is None:
            res.append(None)
            continue
        res.append(node.val)
        queue.append(node.left)
        queue.append(node.right)
    while res and res[-1] is None:
        res.pop()
    return res


def run_tests():
    sol = Solution()
    cases = [
        # (root, 期望输出, 说明)
        ([3, 9, 20, None, None, 15, 7], 3, "示例 1"),
        ([1, None, 2], 2, "示例 2"),
        ([], 0, "空树"),
        ([1], 1, "单节点"),
        ([1, 2, None, 3], 3, "左斜链：深度等于节点数"),
        ([1, 2, 3, 4, None, None, 5], 3, "左右子树深度相同"),
    ]
    passed = 0
    for i, (root, expected, desc) in enumerate(cases, 1):
        got = sol.maxDepth(build_tree(root))
        ok = got == expected
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] #{i} {desc}: 期望 {expected}, 实际 {got}")
    print(f"\n{passed}/{len(cases)} 通过")


if __name__ == "__main__":
    run_tests()
