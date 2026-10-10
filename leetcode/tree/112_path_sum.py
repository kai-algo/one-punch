"""
112. 路径总和（Path Sum）
难度：简单
链接：https://leetcode.cn/problems/path-sum/

【题目】
给你二叉树的根节点 `root` 和一个表示目标和的整数 `targetSum`。判断该树中是否存在
根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和 `targetSum`。如果存在，
返回 `true`；否则，返回 `false`。

叶子节点是指没有子节点的节点。

【示例】
示例 1：
    输入：root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
    输出：true
    解释：等于目标和的根节点到叶节点路径为 5 -> 4 -> 11 -> 2。

示例 2：
    输入：root = [1,2,3], targetSum = 5
    输出：false
    解释：树中存在两条根节点到叶子节点的路径：
        (1 -> 2): 和为 3
        (1 -> 3): 和为 4
        不存在 sum = 5 的根节点到叶子节点的路径。

示例 3：
    输入：root = [], targetSum = 0
    输出：false
    解释：由于树是空的，所以不存在根节点到叶子节点的路径。

【约束】
- 树中节点的数目在范围 `[0, 5000]` 内
- `-1000 <= Node.val <= 1000`
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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def dfs(node, now_sum):
            now_sum += node.val
            if not node.left and not node.right and now_sum == targetSum:
                return True
            is_left = False
            is_right = False
            if node.left:
                is_left = dfs(node.left, now_sum)
            if node.right:
                is_right = dfs(node.right, now_sum)
            return is_left or is_right

        # 在这里写解答
        return dfs(root, 0)


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
        # (root, targetSum, 期望输出, 说明)
        ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 22, True, "示例 1"),
        ([1, 2, 3], 5, False, "示例 2"),
        ([], 0, False, "示例 3：空树，即使 target=0 也是 False"),
        ([1], 1, True, "单节点即叶子"),
        ([1, 2], 1, False, "根不是叶子：不能在 1 处就停"),
        ([1, 2], 3, True, "只有左孩子，路径 1->2"),
        ([-2, None, -3], -5, True, "负数：不能因和<0 或>target 就剪枝"),
        ([-2, None, -3], -2, False, "负数：路径到根为 -2 但根不是叶子"),
    ]
    passed = 0
    for i, (root, target, expected, desc) in enumerate(cases, 1):
        got = sol.hasPathSum(build_tree(root), target)
        ok = got == expected
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] #{i} {desc}: 期望 {expected}, 实际 {got}")
    print(f"\n{passed}/{len(cases)} 通过")


if __name__ == "__main__":
    run_tests()
