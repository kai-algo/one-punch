"""
235. 二叉搜索树的最近公共祖先（Lowest Common Ancestor of a Binary Search Tree）
难度：中等
链接：https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-search-tree/

【题目】
给定一个二叉搜索树，找到该树中两个指定节点的最近公共祖先。

最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，
满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

【示例】
示例 1：
    输入：root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
    输出：6
    解释：节点 2 和节点 8 的最近公共祖先是 6。

示例 2：
    输入：root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
    输出：2
    解释：节点 2 和节点 4 的最近公共祖先是 2，因为根据定义最近公共祖先节点可以为节点本身。

示例 3：
    输入：root = [2,1], p = 2, q = 1
    输出：2

【约束】
- 所有节点的值都是唯一的
- `p`、`q` 为不同节点且均存在于给定的二叉搜索树中
- 树中节点数目在范围 `[2, 10^5]` 内
- `-10^9 <= Node.val <= 10^9`
"""

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        # 在这里写解答
        if p.val > q.val:
            p, q = q, p

        ans = None
        node = root
        while node:
            if node.val < p.val:
                node = node.right
            elif node.val > q.val:
                node = node.left
            else:
                ans = node
                break

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


def find_node(root: Optional[TreeNode], val: int) -> TreeNode:
    """在 BST 中按值找到节点（测试用，LeetCode 里 p、q 直接以节点形式传入）。"""
    node = root
    while node and node.val != val:
        node = node.left if val < node.val else node.right
    assert node is not None
    return node


def run_tests():
    sol = Solution()
    tree = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
    cases = [
        # (root, p, q, 期望的 LCA 值, 说明)
        (tree, 2, 8, 6, "示例 1：p、q 分居根两侧"),
        (tree, 2, 4, 2, "示例 2：祖先是 p 本身"),
        ([2, 1], 2, 1, 2, "示例 3：最小规模，p 是根"),
        (tree, 4, 2, 2, "p、q 顺序反过来（p > q）"),
        (tree, 3, 5, 4, "都在 4 的两侧，LCA 在深处"),
        (tree, 0, 5, 2, "跨越 2 的左右子树"),
        (tree, 7, 9, 8, "都在右子树，LCA 是 8"),
        (tree, 0, 9, 6, "最小与最大值，LCA 是根"),
        ([5, None, 6], 5, 6, 5, "退化成链"),
    ]
    passed = 0
    for i, (values, p, q, expected, desc) in enumerate(cases, 1):
        root = build_tree(values)
        got = sol.lowestCommonAncestor(root, find_node(root, p), find_node(root, q))
        got_val = got.val if got else None
        ok = got_val == expected
        passed += ok
        print(
            f"[{'PASS' if ok else 'FAIL'}] #{i} {desc}: 期望 {expected}, 实际 {got_val}"
        )
    print(f"\n{passed}/{len(cases)} 通过")


if __name__ == "__main__":
    run_tests()
