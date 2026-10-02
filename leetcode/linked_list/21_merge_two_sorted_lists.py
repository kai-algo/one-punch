"""
21. 合并两个有序链表（Merge Two Sorted Lists）
难度：简单
链接：https://leetcode.cn/problems/merge-two-sorted-lists/

【题目】
将两个升序链表合并为一个新的升序链表并返回。
新链表是通过拼接给定的两个链表的所有节点组成的。

【示例】
示例 1：
    输入：l1 = [1,2,4], l2 = [1,3,4]
    输出：[1,1,2,3,4,4]

示例 2：
    输入：l1 = [], l2 = []
    输出：[]

示例 3：
    输入：l1 = [], l2 = [0]
    输出：[0]

【约束】
- 两个链表的节点数目范围是 [0, 50]
- -100 <= Node.val <= 100
- l1 和 l2 均按非递减顺序排列
"""

from typing import Optional


# LeetCode 上 ListNode 已经定义好，这里为了本地运行需要自己带上
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
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
        # (list1, list2, 期望输出列表, 说明)
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4], "示例 1"),
        ([], [], [], "示例 2：两个都为空"),
        ([], [0], [0], "示例 3：一个为空"),
        ([0], [], [0], "另一个为空（与示例 3 对称）"),
        ([1], [2], [1, 2], "各一个节点"),
        ([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6], "一条链整体在另一条之前"),
        ([4, 5, 6], [1, 2, 3], [1, 2, 3, 4, 5, 6], "一条链整体在另一条之后"),
        ([5], [1, 2, 3], [1, 2, 3, 5], "长度悬殊：长链走完后还要拼接剩余部分"),
        ([1, 1], [1, 1], [1, 1, 1, 1], "全部相等"),
        ([-3, -1], [-2, 0], [-3, -2, -1, 0], "含负数，交错合并"),
    ]
    passed = 0
    for i, (v1, v2, expected, desc) in enumerate(cases, 1):
        got = to_list(sol.mergeTwoLists(build(v1), build(v2)))
        ok = got == expected
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] #{i} {desc}: 期望 {expected}, 实际 {got}")
    print(f"\n{passed}/{len(cases)} 通过")


if __name__ == "__main__":
    run_tests()
