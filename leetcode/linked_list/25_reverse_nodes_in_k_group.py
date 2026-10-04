"""
25. K 个一组翻转链表（Reverse Nodes in k-Group）
难度：困难
链接：https://leetcode.cn/problems/reverse-nodes-in-k-group/

【题目】
给你链表的头节点 `head`，每 `k` 个节点一组进行翻转，请你返回修改后的链表。

`k` 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 `k` 的整数倍，
那么请将最后剩余的节点保持原有顺序。

你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

【示例】
示例 1：
    输入：head = [1,2,3,4,5], k = 2
    输出：[2,1,4,3,5]

示例 2：
    输入：head = [1,2,3,4,5], k = 3
    输出：[3,2,1,4,5]

【约束】
- 链表中的节点数目为 n
- 1 <= k <= n <= 5000
- 0 <= Node.val <= 1000

【进阶】
你可以设计一个只用 O(1) 额外内存空间的算法解决此问题吗？
"""

from typing import Optional


# LeetCode 上 ListNode 已经定义好，这里为了本地运行需要自己带上
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 在这里写解答
        pass


# ============ 感悟 ============
# 思路：
#
# 复杂度：时间 O( )  空间 O( )
#
# 易错点 / 收获：
#


# ============ 测试辅助 ============
def build(values: list[int]) -> Optional[ListNode]:
    """列表 -> 链表，返回头节点；空列表返回 None。"""
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_list(head: Optional[ListNode]) -> list[int]:
    """链表 -> 列表，方便用 == 比较。"""
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


# ============ 测试用例 ============
def run_tests():
    sol = Solution()
    cases = [
        # (head 的值列表, k, 期望输出列表, 说明)
        ([1, 2, 3, 4, 5], 2, [2, 1, 4, 3, 5], "示例 1：末尾剩 1 个保持原样"),
        ([1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5], "示例 2：末尾剩 2 个保持原样"),
        ([1], 1, [1], "最小规模：单节点"),
        ([1, 2, 3], 1, [1, 2, 3], "k=1：不翻转"),
        ([1, 2], 2, [2, 1], "k=n：整条翻转（两个节点）"),
        ([1, 2, 3, 4, 5], 5, [5, 4, 3, 2, 1], "k=n：整条翻转"),
        ([1, 2, 3, 4, 5, 6], 3, [3, 2, 1, 6, 5, 4], "n 恰好是 k 的整数倍"),
        ([1, 2, 3, 4], 4, [4, 3, 2, 1], "k=n=4"),
        ([1, 2, 3, 4, 5], 4, [4, 3, 2, 1, 5], "只有第一组够 k 个，剩 1 个"),
        ([1, 2, 3, 4, 5, 6, 7], 3, [3, 2, 1, 6, 5, 4, 7], "多组翻转 + 尾部不足 k 个"),
        ([1, 2, 3], 2, [2, 1, 3], "尾部不足 k 个：最后一个节点必须接回去"),
        ([1, 1, 2, 2], 2, [1, 1, 2, 2], "值相同：看结构不是看值"),
    ]
    passed = 0
    for i, (values, k, expected, desc) in enumerate(cases, 1):
        got = to_list(sol.reverseKGroup(build(values), k))
        ok = got == expected
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] #{i} {desc}: 期望 {expected}, 实际 {got}")
    print(f"\n{passed}/{len(cases)} 通过")


if __name__ == "__main__":
    run_tests()
