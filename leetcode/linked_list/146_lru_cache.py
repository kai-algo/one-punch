"""
146. LRU 缓存（LRU Cache）
难度：中等
链接：https://leetcode.cn/problems/lru-cache/

【题目】
请你设计并实现一个满足 LRU（最近最少使用）缓存约束的数据结构。

实现 `LRUCache` 类：
- `LRUCache(int capacity)`：以正整数作为容量 `capacity` 初始化 LRU 缓存
- `int get(int key)`：如果关键字 `key` 存在于缓存中，则返回关键字的值，否则返回 `-1`
- `void put(int key, int value)`：如果关键字 `key` 已经存在，则变更其数据值 `value`；
  如果不存在，则向缓存中插入该组 `key-value`。如果插入操作导致关键字数量超过 `capacity`
  ，则应该逐出最久未使用的关键字。

函数 `get` 和 `put` 必须以 `O(1)` 的平均时间复杂度运行。

【示例】
示例 1：
    输入：
        ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
        [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    输出：
        [null, null, null, 1, null, -1, null, -1, 3, 4]
    解释：
        LRUCache lRUCache = new LRUCache(2);
        lRUCache.put(1, 1); // 缓存是 {1=1}
        lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
        lRUCache.get(1);    // 返回 1
        lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
        lRUCache.get(2);    // 返回 -1 (未找到)
        lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
        lRUCache.get(1);    // 返回 -1 (未找到)
        lRUCache.get(3);    // 返回 3
        lRUCache.get(4);    // 返回 4

【约束】
- 1 <= capacity <= 3000
- 0 <= key <= 10000
- 0 <= value <= 10^5
- 最多调用 2 * 10^5 次 get 和 put

【提示】
面试里通常期望手写「哈希表 + 双向链表」，而不是直接用 OrderedDict。
"""


class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        # cache
        self.cache = {}
        self.capacity = capacity

        # link
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_to_head(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_to_head(node)
            node.value = value
        else:
            node = Node(key, value)
            self._add_to_head(node)
            self.cache[key] = node
            if len(self.cache) > self.capacity:
                del self.cache[self.tail.prev.key]
                self._remove(self.tail.prev)

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next = node
        node.next.prev = node

    # def get(self, key: int) -> int:
    #     if key in self.cache:
    #         self.move_to_head(key)
    #         return self.cache[key].value
    #     else:
    #         return -1

    # def put(self, key: int, value: int) -> None:
    #     if key in self.cache:
    #         self.move_to_head(key)
    #         self.cache[key].value = value
    #     else:
    #         node = self.add_to_head(key, value)
    #         self.cache[key] = node
    #         if len(self.cache) > self.capacity:
    #             del_key = self.delete_tail()
    #             del self.cache[del_key]

    # def move_to_head(self, key):
    #     node = self.cache[key]
    #     # move
    #     node.prev.next = node.next
    #     node.next.prev = node.prev

    #     # head
    #     node.prev = self.head
    #     node.next = self.head.next
    #     self.head.next = node
    #     node.next.prev = node

    # def add_to_head(self, key, value):
    #     node = Node(key, value)
    #     node.prev = self.head
    #     node.next = self.head.next
    #     self.head.next = node
    #     node.next.prev = node
    #     return node

    # def delete_tail(self):
    #     node = self.tail.prev
    #     self.tail.prev = node.prev
    #     self.tail.prev.next = self.tail
    #     return node.key


# ============ 感悟 ============
# 思路：
# 哈希表 + 双向链表，各管一件事：
#   - 哈希表 key -> 节点：O(1) 找到节点；
#   - 双向链表：维护使用顺序，头部 = 最近使用，尾部 = 最久未用；
#   - 两个哨兵节点 head / tail：头尾插入删除都不用判空。
# get：命中就把节点移到头部再返回值，未命中返回 -1。
# put：key 已存在 -> 更新值 + 移到头部；
#      不存在 -> 新建节点插到头部，超过容量就淘汰 tail.prev（同时删哈希表里的 key）。
#
# 复杂度：时间 get / put 均 O(1)  空间 O(capacity)
#
# 易错点 / 收获：
# 1. 方法名前的 _（如 _remove、_add_to_head）：Python 约定，表示「类内部用的辅助方法」，
#    对外接口只有 get / put。只是君子协议，不强制。
# 2. 方法拆解：把链表操作拆成两个原子操作 _remove（摘下）和 _add_to_head（插入），
#    「移动到头部 = 摘下 + 插入」，淘汰尾节点 = 摘下 tail.prev。
#    原来 move_to_head / add_to_head / delete_tail 里重复的指针操作，抽出来后只改一处。
#    （注释掉的旧代码保留作为思路演变的记录）
# 3. 拆开后「移动」要自己组合：put 的更新分支漏了 _remove，不会报错，
#    只会悄悄把链表搞乱（case 4 暴露）。可以再封装一个 _move_to_head 避免漏写。
# 4. 节点里必须存 key：淘汰尾节点时要靠它反查并删除哈希表里的项。
#    淘汰顺序：先取 tail.prev.key 删字典，再摘节点。
# 5. 必须是双向链表：删除任意节点需要 O(1) 拿到前驱。
# 6. value 可能是 0：判断命中用 `key in cache`，不能用 `if not value`。
# 7. 线程安全：get 也会改链表，所以也要加锁；临界区要覆盖「查字典 + 改链表 + 改字典」
#    整个过程，用一把 threading.Lock 包住 get / put 入口即可
#    高并发优化：分片（按 hash(key) 分段，各自一把锁）、读路径异步更新顺序。


# ============ 测试用例 ============
def run_tests():
    cases = [
        # (容量, 操作序列, 期望的 get 结果序列, 说明)
        # 操作：("put", key, value) 或 ("get", key)；期望里只记录 get 的返回值
        (
            2,
            [
                ("put", 1, 1),
                ("put", 2, 2),
                ("get", 1),
                ("put", 3, 3),
                ("get", 2),
                ("put", 4, 4),
                ("get", 1),
                ("get", 3),
                ("get", 4),
            ],
            [1, -1, -1, 3, 4],
            "示例 1：get 刷新最近使用 + 满了淘汰最久未用",
        ),
        (
            1,
            [("put", 2, 1), ("get", 2), ("put", 3, 2), ("get", 2), ("get", 3)],
            [1, -1, 2],
            "容量 1：每次 put 新 key 都淘汰旧 key",
        ),
        (
            2,
            [("get", 1)],
            [-1],
            "空缓存 get：返回 -1",
        ),
        (
            2,
            [
                ("put", 1, 1),
                ("put", 2, 2),
                ("put", 1, 10),
                ("put", 3, 3),
                ("get", 2),
                ("get", 1),
                ("get", 3),
            ],
            [-1, 10, 3],
            "put 已存在的 key：要更新值并刷新为最近使用（所以淘汰的是 2 不是 1）",
        ),
        (
            2,
            [
                ("put", 1, 1),
                ("put", 1, 2),
                ("put", 1, 3),
                ("put", 2, 4),
                ("get", 1),
                ("get", 2),
            ],
            [3, 4],
            "反复 put 同一个 key：不能重复计数，不能提前淘汰",
        ),
        (
            1,
            [("put", 1, 0), ("get", 1), ("put", 2, 2), ("get", 1), ("get", 2)],
            [0, -1, 2],
            "value 为 0：不能用 `if not value` 判断是否命中",
        ),
    ]
    passed = 0
    for i, (capacity, ops, expected, desc) in enumerate(cases, 1):
        cache = LRUCache(capacity)
        got = []
        for op in ops:
            if op[0] == "put":
                cache.put(op[1], op[2])
            else:
                got.append(cache.get(op[1]))
        ok = got == expected
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] #{i} {desc}: 期望 {expected}, 实际 {got}")
    print(f"\n{passed}/{len(cases)} 通过")


if __name__ == "__main__":
    run_tests()
