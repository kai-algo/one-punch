# one-punch：每日一道 LeetCode

这个项目用来每天练一道 LeetCode 题。用户在 VS Code 里做题，直接在 py 文件里写注释和感悟。

## 工作流

用户会粘贴一道题（中文题面，含题号、标题、难度、描述等）。你要：

1. 使用 `leetcode-daily` skill 生成题目文件（格式见 `.claude/skills/leetcode-daily/SKILL.md`）。
2. 生成完后，和用户一起深入讨论这道题（思路、复杂度、易错点、其他解法）。

## 约定

- 题目按**专题分类**存放：`leetcode/{专题文件夹}/题号_英文名.py`。专题文件夹用英文小写下划线命名，例如 `leetcode/prefix_suffix_decomposition/135_candy.py`、`leetcode/linked_list/146_lru_cache.py`。**不要**把题目直接放在 `leetcode/` 根目录。
  - 文件名：`题号_英文名.py`，英文名用 LeetCode 官方 slug 的下划线形式。
  - 选专题：优先放进已有的专题文件夹（先 `ls leetcode/` 查看）；没有合适的再新建。归类依据是这道题的**核心解法 / 套路**，而不是官方标签。拿不准归到哪一类时，先问用户。
  - 某个专题下有多道题、且有共性时，可以在该文件夹放一个 `README.md`，对比各题的特性和易错点（参考 `leetcode/prefix_suffix_decomposition/README.md`）。
  - 现有专题：`prefix_suffix_decomposition`（前后缀分解）、`linked_list`（链表）。
- 题目描述、注释一律用中文；代码标识符（类名、函数名、变量）保持 LeetCode 原始英文签名。
- 默认只给出题目、函数签名（`pass`）和测试用例，**不写解答**，除非用户明确要求。用户自己写解答和感悟。
- 不要改动用户已经写过的「感悟」区和解答代码。
- 语言为 Python 3。类型注解用内置泛型（`list[int]`、`dict[str, int]`），不要 `from typing import List`（Ruff UP035 会报 deprecated）；需要 `Optional` 时才从 `typing` 导入。
