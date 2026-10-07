"""
226. 翻转二叉树（Invert Binary Tree）
难度：简单
链接：https://leetcode.cn/problems/invert-binary-tree/

【题目】
给你一棵二叉树的根节点 `root`，翻转这棵二叉树，并返回其根节点。

【示例】
示例 1：
    输入：root = [4,2,7,1,3,6,9]
    输出：[4,7,2,9,6,3,1]

示例 2：
    输入：root = [2,1,3]
    输出：[2,3,1]

示例 3：
    输入：root = []
    输出：[]

【约束】
- 树中节点数目范围在 `[0, 100]` 内
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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = root.right, root.left
        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)
        # 在这里写解答
        return root


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
        ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1], "示例 1"),
        ([2, 1, 3], [2, 3, 1], "示例 2"),
        ([], [], "示例 3：空树"),
        ([1], [1], "单节点"),
        ([1, 2], [1, None, 2], "只有左孩子 -> 只有右孩子"),
        ([1, None, 2], [1, 2], "只有右孩子 -> 只有左孩子"),
        ([1, 2, None, 3], [1, None, 2, None, 3], "左斜链：每一层都要翻转"),
    ]
    passed = 0
    for i, (root, expected, desc) in enumerate(cases, 1):
        got = to_list(sol.invertTree(build_tree(root)))
        ok = got == expected
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] #{i} {desc}: 期望 {expected}, 实际 {got}")
    print(f"\n{passed}/{len(cases)} 通过")


if __name__ == "__main__":
    run_tests()
