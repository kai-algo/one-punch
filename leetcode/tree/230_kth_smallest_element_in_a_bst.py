"""
230. 二叉搜索树中第 K 小的元素（Kth Smallest Element in a BST）
难度：中等
链接：https://leetcode.cn/problems/kth-smallest-element-in-a-bst/

【题目】
给定一个二叉搜索树的根节点 `root`，和一个整数 `k`，请你设计一个算法查找其中第 `k` 小的元素
（从 1 开始计数）。

【示例】
示例 1：
    输入：root = [3,1,4,null,2], k = 1
    输出：1

示例 2：
    输入：root = [5,3,6,2,4,null,null,1], k = 3
    输出：3

【约束】
- 树中的节点数为 `n`
- `1 <= k <= n <= 10^4`
- `0 <= Node.val <= 10^4`

【进阶】
如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 `k` 小的值，你将如何优化算法？
"""

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = None
        count = 0

        # 中序遍历
        def dfs(node):
            nonlocal ans, count
            if not node or ans is not None:
                return
            dfs(node.left)
            count += 1
            if count == k:
                ans = node.val
                return
            dfs(node.right)

        dfs(root)

        return ans


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


def run_tests():
    sol = Solution()
    cases = [
        # (root, k, 期望输出, 说明)
        ([3, 1, 4, None, 2], 1, 1, "示例 1"),
        ([5, 3, 6, 2, 4, None, None, 1], 3, 3, "示例 2"),
        ([1], 1, 1, "单节点"),
        ([5, 3, 6, 2, 4, None, None, 1], 6, 6, "k = n：最大值在最右"),
        ([5, 3, 6, 2, 4, None, None, 1], 1, 1, "最小值在最左深处"),
        ([1, None, 2], 2, 2, "退化成右链"),
        ([3, 2, None, 1], 2, 2, "退化成左链：中序 1,2,3"),
        ([5, 3, 6, 2, 4, None, None, 1], 4, 4, "k 落在左子树的右孩子上，需要回溯计数"),
    ]
    passed = 0
    for i, (root, k, expected, desc) in enumerate(cases, 1):
        got = sol.kthSmallest(build_tree(root), k)
        ok = got == expected
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] #{i} {desc}: 期望 {expected}, 实际 {got}")
    print(f"\n{passed}/{len(cases)} 通过")


if __name__ == "__main__":
    run_tests()
