"""
206. 反转链表（Reverse Linked List）
难度：简单
链接：https://leetcode.cn/problems/reverse-linked-list/

【题目】
给你单链表的头节点 `head`，请你反转链表，并返回反转后的链表。

【示例】
示例 1：
    输入：head = [1,2,3,4,5]
    输出：[5,4,3,2,1]

示例 2：
    输入：head = [1,2]
    输出：[2,1]

示例 3：
    输入：head = []
    输出：[]

【约束】
- 链表中节点的数目范围是 [0, 5000]
- -5000 <= Node.val <= 5000

【进阶】
链表可以选用迭代或递归方式完成反转。你能否用两种方法解决这道题？
"""

from typing import Optional


# LeetCode 上 ListNode 已经定义好，这里为了本地运行需要自己带上
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
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
        # (head 的值列表, 期望输出列表, 说明)
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], "示例 1"),
        ([1, 2], [2, 1], "示例 2：两个节点"),
        ([], [], "示例 3：空链表"),
        ([1], [1], "单个节点"),
        ([1, 2, 3], [3, 2, 1], "奇数个节点"),
        ([1, 1, 1], [1, 1, 1], "值全相同：看结构不是看值"),
        ([-1, 0, 1], [1, 0, -1], "含负数和 0"),
        ([1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1], "偶数个节点"),
    ]
    passed = 0
    for i, (values, expected, desc) in enumerate(cases, 1):
        got = to_list(sol.reverseList(build(values)))
        ok = got == expected
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] #{i} {desc}: 期望 {expected}, 实际 {got}")
    print(f"\n{passed}/{len(cases)} 通过")


if __name__ == "__main__":
    run_tests()
