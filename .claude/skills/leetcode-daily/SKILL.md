---
name: leetcode-daily
description: 根据用户粘贴的 LeetCode 题目（中文题面）生成一个每日练习 py 文件，包含中文题目、函数签名、测试用例和感悟区，文件名为「题号_英文名.py」。当用户粘贴一道 LeetCode 题、或说「来今天的题」「生成题目」时使用。
---

# leetcode-daily

把用户粘贴的一道 LeetCode 题，变成项目 `leetcode/{专题}/` 文件夹下的一个练习文件（专题文件夹不存在则先创建）。题目必须分类存放，不要直接放在 `leetcode/` 根目录。

## 步骤

1. **解析题面**：提取题号、中文标题、难度、题目描述、示例、约束。忽略「相关标签」「相关企业」「premium lock icon」等网页杂质。
   - 题面缺少示例或约束时，凭对该题的了解补全；没把握的不要编造，在文件里注明「约束待核对」。
2. **确定专题文件夹**：先 `ls leetcode/` 查看已有专题，优先放入已有的；没有合适的再新建。
   - 文件夹用英文小写下划线命名，如 `prefix_suffix_decomposition`、`linked_list`、`two_pointers`、`binary_search`、`dynamic_programming`。
   - 归类依据是这道题的核心解法 / 套路，而不是官方标签。拿不准时先问用户。
3. **确定文件名**：`{题号}_{英文slug下划线}.py`，如 `135_candy.py`，完整路径形如 `leetcode/prefix_suffix_decomposition/135_candy.py`。英文名用 LeetCode 官方英文标题（小写，空格转下划线）。题号不确定时先问用户。若文件已存在（在任何专题文件夹下都算），不要覆盖，告诉用户。
4. **写文件**，严格按下面模板。
5. **运行一次**（`python3 leetcode/{专题}/文件名`）确认文件语法正确、未实现时会给出清晰提示，而不是崩溃在无关位置。
6. 简短告知文件路径，然后直接开始和用户讨论这道题（不要贴整份文件内容）。

## 文件模板

```python
"""
{题号}. {中文标题}（{英文标题}）
难度：{简单/中等/困难}
链接：https://leetcode.cn/problems/{slug-with-dashes}/

【题目】
{中文题目描述，保留原意，公式和变量用反引号或原样}

【示例】
示例 1：
    输入：{...}
    输出：{...}
    解释：{...}

【约束】
- {...}
"""

class Solution:
    def {方法名}(self, {参数}: {类型}) -> {返回类型}:
        # 在这里写解答
        pass


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
        ({...}, {...}, "示例 1"),
    ]
    passed = 0
    for i, (*args, expected, desc) in enumerate(cases, 1):
        got = sol.{方法名}(*args)
        ok = got == expected
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] #{i} {desc}: 期望 {expected}, 实际 {got}")
    print(f"\n{passed}/{len(cases)} 通过")


if __name__ == "__main__":
    run_tests()
```

## 规则

- **不写解答**：方法体只放 `pass`，除非用户明确要求给答案。
- 方法名、参数名沿用 LeetCode 官方 Python3 签名；类型注解用**内置泛型**：`list[int]`、`dict[str, int]`、`tuple[int, int]`，**不要** `from typing import List/Dict/Tuple`（Ruff UP035 会报 deprecated）。模板里默认不写 `from typing import ...`，只有确实需要 `Optional` 之类（链表、树题）时才 `from typing import Optional`。Python 3.9 下不要用 `X | None` 写法，保持 `Optional[X]`。
- 测试用例至少包含：题目所有示例 + 最小规模（如 n=1）+ 边界（全相同、全递增、全递减、含 0/负数等，视题而定）+ 1~2 个容易踩坑的用例。每个用例的期望值必须自己推算确认正确，并在说明里写出该用例考察什么。
- 涉及「返回任意合法答案」「原地修改」「链表/树」等无法直接 `==` 比较的题，调整测试写法（转换成列表、排序后比较、写校验函数等），并保持模板其余结构不变。链表题在文件里自带 `ListNode` 类和 `build` / `to_list` 辅助函数（参考 `leetcode/linked_list/` 下已有文件）。
- 同一专题下积累多道题后，可建议用户在该文件夹补一个 `README.md` 对比各题特性。
- 中文描述要通顺自然，不要机翻腔；用户粘贴的中文题面原文优先保留。
