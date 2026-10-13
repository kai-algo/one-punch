"""
394. 字符串解码（Decode String）
难度：中等
链接：https://leetcode.cn/problems/decode-string/

【题目】
给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为：`k[encoded_string]`，表示其中方括号内部的 `encoded_string` 正好重复 `k` 次。注意 `k` 保证为正整数。

你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 `k`，例如不会出现像 `3a` 或 `2[4]` 的输入。

测试用例保证输出的长度不会超过 `10^5`。

【示例】
示例 1：
    输入：s = "3[a]2[bc]"
    输出："aaabcbc"

示例 2：
    输入：s = "3[a2[c]]"
    输出："accaccacc"

示例 3：
    输入：s = "2[abc]3[cd]ef"
    输出："abcabccdcdcdef"

示例 4：
    输入：s = "abc3[cd]xyz"
    输出："abccdcdcdxyz"

【约束】
- `1 <= s.length <= 30`
- `s` 由小写英文字母、数字和方括号 `'[]'` 组成
- `s` 保证是一个有效的输入
- `s` 中所有整数的取值范围为 `[1, 300]`
"""


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c == "]":
                temp_list = []
                while stack[-1] != "[":
                    temp_list.append(stack.pop())
                temp_list.reverse()
                stack.pop()
                number = 1
                num_list = []
                while stack and stack[-1].isdigit():
                    num_list.append(stack.pop())
                if num_list:
                    number = 0
                    num_list.reverse()
                    for n in num_list:
                        number = number * 10 + int(n)
                for _ in range(number):
                    for t in temp_list:
                        stack.append(t)
            else:
                stack.append(c)
        return "".join(stack)


"""
1. 栈里存的东西太碎
数字和字母都是一个字符一个字符压进去的,所以到了 ] 要弹两轮,再用 reverse 还原顺序,再手工拼数字。最后展开时,又把字符一个个压回栈。改成压「一层的上下文」就不需要这些步骤:

2. number = 1 的分支其实用不到
题目保证 [ 前面一定有数字,所以 num_list 不会为空,if num_list 和 number = 1 可以删。

3. 边读边累积数字
读到数字时 num = num * 10 + int(c),不用先压栈再反向还原。

下面是常见的写法,栈里存 (进入 [ 之前的字符串, 重复次数):

def decodeString(self, s: str) -> str:
    stack = []
    cur, num = "", 0
    for c in s:
        if c.isdigit():
            num = num * 10 + int(c)
        elif c == "[":
            stack.append((cur, num))
            cur, num = "", 0
        elif c == "]":
            prev, k = stack.pop()
            cur = prev + cur * k
        else:
            cur += c
    return cur

这个版本里,[ 时保存现场并清空,] 时恢复现场并合并。没有内层 while,没有 reverse,五个分支一目了然。

两种写法的复杂度:
- 你的版本是字符栈,展开时逐个字符压回,耗时和输出长度成正比。
- 上面的版本用字符串乘法 cur * k,也是 O(输出长度),但常数小很多,因为是在 C 层复制。



"""

# ============ 感悟 ============
# 思路：
#
# 复杂度：时间 O( )  空间 O( )
#
# 易错点 / 收获：
#


# ============ 测试用例 ============
def run_tests():
    sol = Solution()
    cases = [
        # (输入参数..., 期望输出, 说明)
        ("3[a]2[bc]", "aaabcbc", "示例 1"),
        ("3[a2[c]]", "accaccacc", "示例 2：嵌套"),
        ("2[abc]3[cd]ef", "abcabccdcdcdef", "示例 3：括号后跟普通字符"),
        ("abc3[cd]xyz", "abccdcdcdxyz", "示例 4：括号前后都有普通字符"),
        ("abc", "abc", "没有任何编码"),
        ("1[a]", "a", "最小规模 / k=1"),
        ("10[a]", "a" * 10, "多位数字 k"),
        ("100[leetcode]", "leetcode" * 100, "三位数 k"),
        ("2[2[2[a]]]", "a" * 8, "三层嵌套"),
        ("2[a2[b]c]d", "abbcabbcd", "括号内前后都有字符 + 内层嵌套"),
    ]
    passed = 0
    for i, (*args, expected, desc) in enumerate(cases, 1):
        got = sol.decodeString(*args)
        ok = got == expected
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] #{i} {desc}: 期望 {expected}, 实际 {got}")
    print(f"\n{passed}/{len(cases)} 通过")


if __name__ == "__main__":
    run_tests()
