"""
100. 相同的树（Same Tree）
难度：简单
链接：https://leetcode.cn/problems/same-tree/

【题目】
给你两棵二叉树的根节点 `p` 和 `q`，编写一个函数来检验这两棵树是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

【示例】
示例 1：
    输入：p = [1,2,3], q = [1,2,3]
    输出：true

示例 2：
    输入：p = [1,2], q = [1,null,2]
    输出：false
    解释：值相同，但结构不同（2 一个是左孩子，一个是右孩子）。

示例 3：
    输入：p = [1,2,1], q = [1,1,2]
    输出：false
    解释：结构相同，但对应位置的值不同。

【约束】
- 两棵树上的节点数目都在范围 `[0, 100]` 内
- `-10^4 <= Node.val <= 10^4`
"""

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


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
        # (p, q, 期望输出, 说明)
        ([1, 2, 3], [1, 2, 3], True, "示例 1"),
        ([1, 2], [1, None, 2], False, "示例 2：结构不同"),
        ([1, 2, 1], [1, 1, 2], False, "示例 3：值不同"),
        ([], [], True, "两棵空树"),
        ([], [1], False, "一空一非空"),
        ([1], [1], True, "单节点相同"),
        ([1, None, 2], [1, None, 3], False, "结构相同、右孩子值不同"),
        ([1, 2, 3, 4], [1, 2, 3, None, 4], False, "深层结构不同（4 左右位置不同）"),
    ]
    passed = 0
    for i, (p, q, expected, desc) in enumerate(cases, 1):
        got = sol.isSameTree(build_tree(p), build_tree(q))
        ok = got == expected
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] #{i} {desc}: 期望 {expected}, 实际 {got}")
    print(f"\n{passed}/{len(cases)} 通过")


if __name__ == "__main__":
    run_tests()
