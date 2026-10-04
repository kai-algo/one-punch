"""
142. 环形链表 II（Linked List Cycle II）
难度：中等
链接：https://leetcode.cn/problems/linked-list-cycle-ii/

【题目】
给定一个链表的头节点 `head`，返回链表开始入环的第一个节点。如果链表无环，则返回 `null`。

如果链表中有某个节点，可以通过连续跟踪 `next` 指针再次到达，则链表中存在环。
为了表示给定链表中的环，评测系统内部使用整数 `pos` 来表示链表尾连接到链表中的位置（索引从 0 开始）。
如果 `pos` 是 -1，则在该链表中没有环。注意：`pos` 不作为参数进行传递，仅仅是为了标识链表的实际情况。

不允许修改链表。

【示例】
示例 1：
    输入：head = [3,2,0,-4], pos = 1
    输出：返回索引为 1 的链表节点
    解释：链表中有一个环，其尾部连接到第二个节点。

示例 2：
    输入：head = [1,2], pos = 0
    输出：返回索引为 0 的链表节点
    解释：链表中有一个环，其尾部连接到第一个节点。

示例 3：
    输入：head = [1], pos = -1
    输出：返回 null
    解释：链表中没有环。

【约束】
- 链表中节点的数目范围在范围 [0, 10^4] 内
- -10^5 <= Node.val <= 10^5
- pos 的值为 -1 或者链表中的一个有效索引

【进阶】
你是否可以使用 O(1) 空间解决此题？
"""

from typing import Optional


# LeetCode 上 ListNode 已经定义好，这里为了本地运行需要自己带上
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        # 这里好像不能用{}创建集合了，需要set()
        node_set = set()
        node_set.add(head)
        while head.next:
            if head.next in node_set:
                return head.next
            node_set.add(head.next)
            head = head.next

        return None


# ============ 感悟 ============
# 思路：
# 方法一（哈希集合，上面的写法）：遍历链表，把访问过的节点放进 set，
#   第一个「已经在 set 里」的节点就是入环点；走到 None 说明无环。
#   精简写法（去掉对 head 的特判，先查再加入）：
#       seen = set()
#       while head:
#           if head in seen:
#               return head
#           seen.add(head)
#           head = head.next
#       return None
#
# 方法二（快慢指针，O(1) 空间）：
#   a = 头到入环点，b = 入环点到相遇点，c = 环长。
#   两指针从 head 出发，slow 每次 1 步，fast 每次 2 步，相遇时：
#       slow 走 a+b，fast 走 a+b+n*c（多绕 n 圈）
#       2(a+b) = a+b+n*c  =>  a = (n-1)*c + (c-b)
#   c-b 是相遇点继续往前走到入环点的距离，
#   所以：一个指针从 head、一个从相遇点，都每次走 1 步，必在入环点相遇。
#
# 复杂度：方法一 时间 O(n)  空间 O(n)；方法二 时间 O(n)  空间 O(1)
#
# 易错点 / 收获：
# - {} 是空字典，空集合要写 set()
# - 判断节点相同要按对象（is / 放进 set），不能按值，值可能重复
#


# ============ 测试辅助 ============
def build_with_cycle(
    values: list[int], pos: int
) -> tuple[Optional[ListNode], list[ListNode]]:
    """列表 -> 链表，尾节点连到索引 pos 的节点（pos=-1 表示无环）。
    返回 (头节点, 所有节点列表)，节点列表用来把返回的节点还原成索引。"""
    nodes = [ListNode(v) for v in values]
    for a, b in zip(nodes, nodes[1:]):
        a.next = b
    if nodes and pos != -1:
        nodes[-1].next = nodes[pos]
    return (nodes[0] if nodes else None), nodes


def index_of(node: Optional[ListNode], nodes: list[ListNode]) -> int:
    """返回节点在原链表中的索引（按对象身份比较）；None 返回 -1。"""
    if node is None:
        return -1
    for i, n in enumerate(nodes):
        if n is node:
            return i
    return -2  # 返回了不属于原链表的节点


# ============ 测试用例 ============
def run_tests():
    sol = Solution()
    cases = [
        # (values, pos, 期望入环点索引, 说明)
        ([3, 2, 0, -4], 1, 1, "示例 1"),
        ([1, 2], 0, 0, "示例 2：整条链成环"),
        ([1], -1, -1, "示例 3：单节点无环"),
        ([], -1, -1, "空链表"),
        ([1], 0, 0, "单节点自环"),
        ([1, 2, 3, 4, 5], -1, -1, "多节点无环"),
        ([1, 2, 3, 4, 5], 4, 4, "尾节点自环"),
        ([1, 2], 1, 1, "两节点，尾部自环"),
        ([1, 2, 3, 4, 5], 0, 0, "入环点就是头节点"),
        ([1, 1, 1], 1, 1, "值全相同：要按节点而不是按值判断"),
        ([1, 2, 3, 4, 5, 6, 7, 8], 3, 3, "环在中间，环长 5，前缀长 3"),
    ]
    passed = 0
    for i, (values, pos, expected, desc) in enumerate(cases, 1):
        head, nodes = build_with_cycle(values, pos)
        got = index_of(sol.detectCycle(head), nodes)
        ok = got == expected
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] #{i} {desc}: 期望 {expected}, 实际 {got}")
    print(f"\n{passed}/{len(cases)} 通过")


if __name__ == "__main__":
    run_tests()
