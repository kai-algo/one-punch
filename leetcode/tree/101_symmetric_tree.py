"""
101. 对称二叉树（Symmetric Tree）
难度：简单
链接：https://leetcode.cn/problems/symmetric-tree/

【题目】
给你一个二叉树的根节点 `root`，检查它是否轴对称。

【示例】
示例 1：
    输入：root = [1,2,2,3,4,4,3]
    输出：true

示例 2：
    输入：root = [1,2,2,null,3,null,3]
    输出：false

【约束】
- 树中节点数目在范围 `[1, 1000]` 内
- `-100 <= Node.val <= 100`

进阶：你可以运用递归和迭代两种方法解决这个问题吗？
"""

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        # 在这里写解答
        def is_symmetric(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return is_symmetric(p.left, q.right) and is_symmetric(p.right, q.left)

        return is_symmetric(root.left, root.right)


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
        # (root, 期望输出, 说明)
        ([1, 2, 2, 3, 4, 4, 3], True, "示例 1"),
        ([1, 2, 2, None, 3, None, 3], False, "示例 2：同侧而非镜像"),
        ([1], True, "单节点"),
        ([1, 2, 2], True, "最小对称树"),
        ([1, 2, 3], False, "左右孩子值不同"),
        ([1, 2, 2, 2, None, 2], False, "左子树的左孩子 vs 右子树的右孩子（空）"),
        ([1, 2, 2, None, 3, 3], True, "左.right 与 右.left 镜像对应"),
        (
            [1, 2, 2, None, 3, None, 3],
            False,
            "同示例 2，易误写成比较 left.left 与 right.left",
        ),
    ]
    passed = 0
    for i, (root, expected, desc) in enumerate(cases, 1):
        got = sol.isSymmetric(build_tree(root))
        ok = got == expected
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] #{i} {desc}: 期望 {expected}, 实际 {got}")
    print(f"\n{passed}/{len(cases)} 通过")


if __name__ == "__main__":
    run_tests()
