"""
105. 从前序与中序遍历序列构造二叉树（Construct Binary Tree from Preorder and Inorder Traversal）
难度：中等
链接：https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

【题目】
给定两个整数数组 `preorder` 和 `inorder`，其中 `preorder` 是二叉树的先序遍历，
`inorder` 是同一棵树的中序遍历，请构造二叉树并返回其根节点。

【示例】
示例 1：
    输入：preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
    输出：[3,9,20,null,null,15,7]

示例 2：
    输入：preorder = [-1], inorder = [-1]
    输出：[-1]

【约束】
- `1 <= preorder.length <= 3000`
- `inorder.length == preorder.length`
- `-3000 <= preorder[i], inorder[i] <= 3000`
- `preorder` 和 `inorder` 均无重复元素
- `inorder` 均出现在 `preorder`
- `preorder` 保证为二叉树的前序遍历序列
- `inorder` 保证为二叉树的中序遍历序列
"""

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        for i, value in enumerate(inorder):
            if root.val == value:
                index = i

        root.left = self.buildTree(preorder[1 : index + 1], inorder[:index])
        root.right = self.buildTree(preorder[index + 1 :], inorder[index + 1 :])

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
        # (preorder, inorder, 期望输出（层序列表）, 说明)
        ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7], [3, 9, 20, None, None, 15, 7], "示例 1"),
        ([-1], [-1], [-1], "示例 2：单节点"),
        ([1, 2, 3], [3, 2, 1], [1, 2, None, 3], "左斜链：中序里根永远在最右"),
        (
            [1, 2, 3],
            [1, 2, 3],
            [1, None, 2, None, 3],
            "右斜链：中序里根永远在最左，左子树为空",
        ),
        ([1, 2, 3], [2, 1, 3], [1, 2, 3], "完全二叉树"),
        (
            [1, 2, 4, 3],
            [4, 2, 1, 3],
            [1, 2, 3, 4],
            "左子树有左孩子，右子树只有一个点：检查左右子树长度划分",
        ),
    ]
    passed = 0
    for i, (pre, ino, expected, desc) in enumerate(cases, 1):
        got = to_list(sol.buildTree(pre, ino))
        ok = got == expected
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] #{i} {desc}: 期望 {expected}, 实际 {got}")
    print(f"\n{passed}/{len(cases)} 通过")


if __name__ == "__main__":
    run_tests()
