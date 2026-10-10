"""
450. 删除二叉搜索树中的节点（Delete Node in a BST）
难度：中等
链接：https://leetcode.cn/problems/delete-node-in-a-bst/

【题目】
给定一个二叉搜索树的根节点 `root` 和一个值 `key`，删除二叉搜索树中的 `key` 对应的节点，
并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。

一般来说，删除节点可分为两个步骤：
1. 首先找到需要删除的节点；
2. 如果找到了，删除它。

【示例】
示例 1：
    输入：root = [5,3,6,2,4,null,7], key = 3
    输出：[5,4,6,2,null,null,7]
    解释：给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。
        一个正确的答案是 [5,4,6,2,null,null,7]，另一个正确答案是 [5,2,6,null,4,null,7]。

示例 2：
    输入：root = [5,3,6,2,4,null,7], key = 0
    输出：[5,3,6,2,4,null,7]
    解释：二叉树不包含值为 0 的节点。

示例 3：
    输入：root = [], key = 0
    输出：[]

【约束】
- 节点数的范围 `[0, 10^4]`
- `-10^5 <= Node.val <= 10^5`
- 节点值唯一
- `root` 是合法的二叉搜索树
- `-10^5 <= key <= 10^5`

【进阶】
要求算法时间复杂度为 O(h)，h 为树的高度。
"""

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                root = root.right
            elif not root.right:
                root = root.left
            else:
                successor = root.right
                while successor.left:
                    successor = successor.left
                root.val = successor.val
                root.right = self.deleteNode(root.right, successor.val)

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


def inorder(root: Optional[TreeNode]) -> list[int]:
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []


def is_valid_bst(
    node: Optional[TreeNode], low=float("-inf"), high=float("inf")
) -> bool:
    if not node:
        return True
    if not low < node.val < high:
        return False
    return is_valid_bst(node.left, low, node.val) and is_valid_bst(
        node.right, node.val, high
    )


def run_tests():
    # 删除后的合法答案不唯一，所以不比较形状：
    # 校验「仍是 BST」且「中序序列 == 原中序去掉 key」
    sol = Solution()
    cases = [
        # (root, key, 说明)
        ([5, 3, 6, 2, 4, None, 7], 3, "示例 1：删除有两个孩子的节点"),
        ([5, 3, 6, 2, 4, None, 7], 0, "示例 2：key 不存在，树不变"),
        ([], 0, "示例 3：空树"),
        ([1], 1, "删除唯一节点，结果为空树"),
        ([5, 3, 6, 2, 4, None, 7], 5, "删除根（两个孩子）"),
        ([5, 3, 6, 2, 4, None, 7], 7, "删除叶子"),
        ([5, 3, 6, 2, 4, None, 7], 6, "删除只有右孩子的节点"),
        ([5, 3, 6, 2, None, None, 7], 3, "删除只有左孩子的节点"),
        ([5, 1, 6, None, 3, None, None, 2, 4], 1, "删除只有右孩子的节点，其子树较深"),
        ([2, 1], 2, "删除根，只有左孩子：新根应是 1"),
        (
            [5, 3, 8, 2, 4, 6, 9, None, None, None, None, None, 7],
            5,
            "删除根：后继节点 6 不是右孩子，且自身带右子树 7",
        ),
    ]
    passed = 0
    for i, (values, key, desc) in enumerate(cases, 1):
        original = inorder(build_tree(values))
        expected = [v for v in original if v != key]
        got_root = sol.deleteNode(build_tree(values), key)
        got = inorder(got_root)
        ok = got == expected and is_valid_bst(got_root)
        passed += ok
        print(
            f"[{'PASS' if ok else 'FAIL'}] #{i} {desc}: 期望中序 {expected}, 实际 {got}"
        )
    print(f"\n{passed}/{len(cases)} 通过")


if __name__ == "__main__":
    run_tests()
