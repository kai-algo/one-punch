"""
437. 路径总和 III（Path Sum III）
难度：中等
链接：https://leetcode.cn/problems/path-sum-iii/

【题目】
给定一个二叉树的根节点 `root`，和一个整数 `targetSum`，求该二叉树里节点值之和等于 `targetSum`
的路径的数目。

路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的
（只能从父节点到子节点）。

【示例】
示例 1：
    输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
    输出：3
    解释：和等于 8 的路径有 3 条。

示例 2：
    输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
    输出：3

【约束】
- 二叉树的节点个数的范围是 `[0, 1000]`
- `-10^9 <= Node.val <= 10^9`
- `-1000 <= targetSum <= 1000`
"""

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # 在这里写解答
        pass


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
        # (root, targetSum, 期望输出, 说明)
        ([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1], 8, 3, "示例 1"),
        ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1], 22, 3, "示例 2"),
        ([], 0, 0, "空树"),
        ([1], 1, 1, "单节点"),
        ([1], 0, 0, "单节点不等"),
        ([0, 1, 1], 1, 4, "含 0：0->1 与 1 各算一条，左右各两条"),
        ([1, None, 2, None, 3, None, 4, None, 5], 3, 2, "链：1+2 和 3"),
        ([1, -2, -3, 1, 3, -2, None, -1], -1, 4, "负数：不能剪枝"),
        ([0, 0, 0], 0, 5, "全 0：3 个单点 + 2 条根到孩子的边 = 5 条"),
    ]
    passed = 0
    for i, (root, target, expected, desc) in enumerate(cases, 1):
        got = sol.pathSum(build_tree(root), target)
        ok = got == expected
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] #{i} {desc}: 期望 {expected}, 实际 {got}")
    print(f"\n{passed}/{len(cases)} 通过")


if __name__ == "__main__":
    run_tests()
