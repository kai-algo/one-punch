"""
155. 最小栈（Min Stack）
难度：中等
链接：https://leetcode.cn/problems/min-stack/

【题目】
设计一个支持 `push`，`pop`，`top` 操作，并能在常数时间内检索到最小元素的栈。

实现 `MinStack` 类：
- `MinStack()` 初始化堆栈对象。
- `void push(int val)` 将元素 val 推入堆栈。
- `void pop()` 删除堆栈顶部的元素。
- `int top()` 获取堆栈顶部的元素。
- `int getMin()` 获取堆栈中的最小元素。

每个操作的时间复杂度都要求 O(1)。

【示例】
示例 1：
    输入：
        ["MinStack","push","push","push","getMin","pop","top","getMin"]
        [[],[-2],[0],[-3],[],[],[],[]]
    输出：
        [null,null,null,null,-3,null,0,-2]
    解释：
        MinStack minStack = new MinStack();
        minStack.push(-2);
        minStack.push(0);
        minStack.push(-3);
        minStack.getMin();   --> 返回 -3
        minStack.pop();
        minStack.top();      --> 返回 0
        minStack.getMin();   --> 返回 -2

【约束】
- `-2^31 <= val <= 2^31 - 1`
- `pop`、`top` 和 `getMin` 操作总是在非空栈上调用
- `push`、`pop`、`top` 和 `getMin` 最多被调用 `3 * 10^4` 次
"""


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_stack and self.min_stack[-1] < val:
            self.min_stack.append(self.min_stack[-1])
        else:
            self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]


# ============ 感悟 ============
# 思路：
#
# 复杂度：时间 O( )  空间 O( )
#
# 易错点 / 收获：
#


# ============ 测试用例 ============
def run_tests():
    # 每个用例：(操作序列, 期望输出序列, 说明)；push/pop 的期望为 None
    cases = [
        (
            [
                ("push", -2),
                ("push", 0),
                ("push", -3),
                ("getMin",),
                ("pop",),
                ("top",),
                ("getMin",),
            ],
            [None, None, None, -3, None, 0, -2],
            "示例 1",
        ),
        (
            [("push", 5), ("top",), ("getMin",), ("pop",)],
            [None, 5, 5, None],
            "最小规模：只有一个元素",
        ),
        (
            [("push", 1), ("push", 1), ("pop",), ("getMin",)],
            [None, None, None, 1],
            "重复的最小值：弹出一个后最小值仍是 1",
        ),
        (
            [
                ("push", 3),
                ("push", 2),
                ("push", 1),
                ("getMin",),
                ("pop",),
                ("getMin",),
                ("pop",),
                ("getMin",),
            ],
            [None, None, None, 1, None, 2, None, 3],
            "递减入栈，逐个弹出时最小值依次回退",
        ),
        (
            [("push", 1), ("push", 2), ("push", 3), ("pop",), ("getMin",), ("top",)],
            [None, None, None, None, 1, 2],
            "递增入栈，最小值始终是栈底",
        ),
        (
            [("push", -2147483648), ("push", 2147483647), ("getMin",), ("top",)],
            [None, None, -2147483648, 2147483647],
            "int 边界值",
        ),
    ]
    passed = 0
    for i, (ops, expected, desc) in enumerate(cases, 1):
        st = MinStack()
        got = []
        for name, *args in ops:
            got.append(getattr(st, name)(*args))
        ok = got == expected
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] #{i} {desc}: 期望 {expected}, 实际 {got}")
    print(f"\n{passed}/{len(cases)} 通过")


if __name__ == "__main__":
    run_tests()
