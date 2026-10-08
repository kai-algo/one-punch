"""
199. 二叉树的右视图（Binary Tree Right Side View）
难度：中等
链接：https://leetcode.cn/problems/binary-tree-right-side-view/

【题目】
给定一个二叉树的根节点 `root`，想象自己站在它的右侧，按照从顶部到底部的顺序，
返回从右侧所能看到的节点值。

【示例】
示例 1：
    输入：root = [1,2,3,null,5,null,4]
    输出：[1,3,4]

示例 2：
    输入：root = [1,2,3,4,null,null,null,5]
    输出：[1,3,4,5]

示例 3：
    输入：root = [1,null,3]
    输出：[1,3]

示例 4：
    输入：root = []
    输出：[]

【约束】
- 二叉树的节点个数的范围是 `[0, 100]`
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
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        res = []
        if not root:
            return res
        queue = deque([root])
        while queue:
            length = len(queue)
            for i in range(length):
                node = queue.popleft()
                if i == length - 1:
                    res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res


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
        ([1, 2, 3, None, 5, None, 4], [1, 3, 4], "示例 1"),
        (
            [1, 2, 3, 4, None, None, None, 5],
            [1, 3, 4, 5],
            "示例 2：深层只有左子树时，左边的节点也会被看到",
        ),
        ([1, None, 3], [1, 3], "示例 3"),
        ([], [], "示例 4：空树"),
        ([1], [1], "单节点"),
        ([1, 2], [1, 2], "只有左孩子：第 2 层可见的是左孩子"),
        ([1, 2, 3, 4], [1, 3, 4], "左子树更深：第 3 层只有左边的 4"),
    ]
    passed = 0
    for i, (root, expected, desc) in enumerate(cases, 1):
        got = sol.rightSideView(build_tree(root))
        ok = got == expected
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] #{i} {desc}: 期望 {expected}, 实际 {got}")
    print(f"\n{passed}/{len(cases)} 通过")


if __name__ == "__main__":
    run_tests()
