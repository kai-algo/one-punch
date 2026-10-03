"""
141. 环形链表（Linked List Cycle）
难度：简单
链接：https://leetcode.cn/problems/linked-list-cycle/

【题目】
给你一个链表的头节点 `head`，判断链表中是否有环。

如果链表中有某个节点，可以通过连续跟踪 `next` 指针再次到达，则链表中存在环。
为了表示给定链表中的环，评测系统内部使用整数 `pos` 来表示链表尾连接到链表中的位置
（索引从 0 开始）。注意：`pos` 不作为参数进行传递，仅仅是为了标识链表的实际情况。

如果链表中存在环，则返回 `true`。否则，返回 `false`。

【示例】
示例 1：
    输入：head = [3,2,0,-4], pos = 1
    输出：true
    解释：链表中有一个环，其尾部连接到第二个节点。

示例 2：
    输入：head = [1,2], pos = 0
    输出：true
    解释：链表中有一个环，其尾部连接到第一个节点。

示例 3：
    输入：head = [1], pos = -1
    输出：false
    解释：链表中没有环。

【约束】
- 链表中节点的数目范围是 [0, 10^4]
- -10^5 <= Node.val <= 10^5
- pos 为 -1 或者链表中的一个有效索引

【进阶】
你能用 O(1)（即，常量）内存解决此问题吗？
"""

from typing import Optional


# LeetCode 上 ListNode 已经定义好，这里为了本地运行需要自己带上
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        fast, slow = head.next, head
        while fast.next and fast.next.next:
            if fast == slow:
                return True
            slow = slow.next
            fast = fast.next.next

        return False


# ============ 感悟 ============
# 思路：
#
# 复杂度：时间 O( )  空间 O( )
#
# 易错点 / 收获：
# 1. 起点错开是为了让第一次 fast == slow 不立刻命中。 这迫使你先写 if not head or not head.next 的特判,还要用 fast.next and fast.next.next 这个较长的条件。
# 2. 标准写法让两个指针都从 head 出发,先移动,再比较。 这样就不需要特判:
# def hasCycle(self, head: Optional[ListNode]) -> bool:
#     slow = fast = head
#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next
#         if slow is fast:
#             return True
#     return False
#    - 空链表时 fast 是 None,循环不进入,直接返回 False。
#    - 单节点时 fast.next 是 None,同样返回 False。
#    - 循环条件只需要 fast and fast.next,因为 fast.next.next 取到 None 是允许的,下一轮条件会判断出来。
# 3. 判断节点是否相同用 is,不要用 ==。 ListNode 没有定义 __eq__,所以现在两者结果一样。但 is 表达的是「同一个对象」,意图更清楚,而且不会被将来加的 __eq__ 影响。


# ============ 测试辅助 ============
def build(values: list[int], pos: int) -> Optional[ListNode]:
    """列表 -> 链表；pos 为尾节点要连回的下标，-1 表示无环。"""
    if not values:
        return None
    nodes = [ListNode(v) for v in values]
    for a, b in zip(nodes, nodes[1:]):
        a.next = b
    if pos != -1:
        nodes[-1].next = nodes[pos]
    return nodes[0]


# ============ 测试用例 ============
def run_tests():
    sol = Solution()
    cases = [
        # (head 的值列表, pos, 期望输出, 说明)
        ([3, 2, 0, -4], 1, True, "示例 1：环在中间"),
        ([1, 2], 0, True, "示例 2：整条链成环"),
        ([1], -1, False, "示例 3：单节点无环"),
        ([], -1, False, "空链表：head 为 None"),
        ([1], 0, True, "单节点自环"),
        ([1, 2, 3], 2, True, "尾节点自环"),
        ([1, 2, 3, 4, 5], -1, False, "较长的无环链表"),
        ([1, 1, 1, 1], -1, False, "值全相同但无环：不能靠比较值判断"),
        ([1, 2, 3, 4, 5, 6], 2, True, "环在中后段"),
    ]
    passed = 0
    for i, (values, pos, expected, desc) in enumerate(cases, 1):
        got = sol.hasCycle(build(values, pos))
        ok = got == expected
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] #{i} {desc}: 期望 {expected}, 实际 {got}")
    print(f"\n{passed}/{len(cases)} 通过")


if __name__ == "__main__":
    run_tests()
