"""
337. 打家劫舍 III（House Robber III）
难度：中等
链接：https://leetcode.cn/problems/house-robber-iii/

【题目】
小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为 `root`。

除了 `root` 之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到
“这个地方的所有房屋的排列类似于一棵二叉树”。如果两个直接相连的房子在同一天晚上被打劫，
房屋将自动报警。

给定二叉树的 `root`。返回在不触动警报的情况下，小偷能够盗取的最高金额。

【示例】
示例 1：
    输入：root = [3,2,3,null,3,null,1]
    输出：7
    解释：小偷一晚能够盗取的最高金额 3 + 3 + 1 = 7

示例 2：
    输入：root = [3,4,5,1,3,null,1]
    输出：9
    解释：小偷一晚能够盗取的最高金额 4 + 5 = 9

【约束】
- 树的节点数在 `[1, 10^4]` 范围内
- `0 <= Node.val <= 10^4`
"""

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # skip rob & rob
        # skip rob
        skip_rob = self.rob(root.left) + self.rob(root.right)
        # rob
        rob = root.val
        if root.left:
            rob += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            rob += self.rob(root.right.left) + self.rob(root.right.right)
        return max(skip_rob, rob)


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
        ([3, 2, 3, None, 3, None, 1], 7, "示例 1"),
        ([3, 4, 5, 1, 3, None, 1], 9, "示例 2"),
        ([1], 1, "单节点"),
        ([0], 0, "全是 0"),
        ([1, 2, 3], 5, "不偷根，偷两个孩子 2+3 > 1"),
        ([5, 1, 1], 5, "偷根 5 > 孩子之和 2"),
        ([2, 1, 3, None, 4], 7, "偷右孩子 3 + 左孙子 4（不相邻）> 偷根 2+4"),
        ([4, 1, None, 2, None, 3], 7, "链 4-1-2-3：偷 4 和 3，而不是简单隔一个偷"),
        ([2, 10, 10, 1, None, None, 1], 20, "不偷根，偷两个孩子 10+10"),
    ]
    passed = 0
    for i, (root, expected, desc) in enumerate(cases, 1):
        got = sol.rob(build_tree(root))
        ok = got == expected
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] #{i} {desc}: 期望 {expected}, 实际 {got}")
    print(f"\n{passed}/{len(cases)} 通过")


if __name__ == "__main__":
    run_tests()
