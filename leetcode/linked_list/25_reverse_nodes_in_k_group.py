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
        # 翻转 left..right 这一段（闭区间），就是 206 的迭代翻转，
        # 只是遇到 right 就停；翻转后 left.next 变成 None，由外面接回去
        def reverseLink(left, right):
            prev = None
            cur = left
            while cur:
                nxt = cur.next
                cur.next = prev
                if cur is right:
                    break
                prev = cur
                cur = nxt

        # dummy 处理「头节点会变」的问题
        head_dummy = ListNode()
        # prev：上一组翻转后的尾节点（第一组之前就是 dummy），用来接这一组的新头
        prev = head_dummy
        # left：当前组的头；right：向后探路的指针，count 数够 k 个就说明凑成一组
        left = head
        right = head
        count = 0
        while right:
            count += 1
            if count % k == 0:
                # 先记下下一组的头，翻转会断开 right.next
                nxt = right.next
                # 翻转
                reverseLink(left, right)
                # 和整体链接：
                # 上一组的尾 -> 这一组翻转后的新头(right)
                prev.next = right
                # 这一组翻转后的新尾(left) -> 下一组的头
                left.next = nxt
                # 移动指针：
                # 这一组的新尾成为下一组的 prev
                prev = left
                # right 设成 left，这样下面的 right = right.next 刚好走到 nxt
                right = left
                # 下一组的头
                left = nxt

            right = right.next

        # 不够 k 个的尾部不进入 if，保持原样，已经被上一组的 left.next = nxt 接住
        return head_dummy.next


# ============ 感悟 ============
# 思路：
# 每一组都是「数够 k 个 -> 翻转 -> 接回去」三步，思路清晰最重要。
# 我的写法（单次扫描）：right 向后走并计数，count 是 k 的倍数时凑成一组，
#   用 206 的迭代翻转翻 left..right，再把 prev(上一组尾) -> right(新头)、
#   left(新尾) -> nxt(下一组头) 接上，然后移动 prev / left / right。
#   尾部不足 k 个时不进 if，保持原样。
#
# 另一种写法（先找尾、再翻转，三步分开写，更好讲清楚）：
#   def reverseKGroup(self, head, k):
#       dummy = ListNode(next=head)
#       pre = dummy                      # 上一组的尾节点
#       while True:
#           tail = pre
#           for _ in range(k):           # 先数够 k 个，不够就直接结束
#               tail = tail.next
#               if not tail:
#                   return dummy.next
#           nxt = tail.next
#           group_head = pre.next
#           prev, cur = nxt, group_head  # prev 初值是 nxt，翻转后尾节点自动接上
#           while cur is not nxt:
#               cur.next, prev, cur = prev, cur, cur.next
#           pre.next = tail              # 上一组接到翻转后的新头
#           pre = group_head             # 原来的头现在是这一组的尾
#
# 复杂度：时间 O(n)  空间 O(1)
#
# 易错点 / 收获：
# - 翻转前一定要先确认后面有 k 个节点，不够就保持原样
# - 每组翻转后要记住新头（接到上一组后面）和新尾（留给下一组去接）
# - 翻转前先存 nxt（下一组的头），翻转会断开原来的指向
# - 技巧：翻转时让 prev 初值 = nxt，尾节点自动指向下一组，不用再手动接
# - 写链表题先理清「每一步改哪几个指针、顺序是什么」，再动手写
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
