# one-punch：每日一道 LeetCode

这个项目用来每天练一道 LeetCode 题。用户在 VS Code 里做题，直接在 py 文件里写注释和感悟。

## 工作流

用户会粘贴一道题（中文题面，含题号、标题、难度、描述等）。你要：

1. 使用 `leetcode-daily` skill 生成题目文件（格式见 `.claude/skills/leetcode-daily/SKILL.md`）。
2. 生成完后，和用户一起深入讨论这道题（思路、复杂度、易错点、其他解法）。

## 约定

- 文件放在项目根目录下的 `leetcode/` 文件夹，命名为 `题号_英文名.py`，英文名用 LeetCode 官方 slug 的下划线形式，例如 `leetcode/135_candy.py`、`leetcode/146_lru_cache.py`。
- 题目描述、注释一律用中文；代码标识符（类名、函数名、变量）保持 LeetCode 原始英文签名。
- 默认只给出题目、函数签名（`pass`）和测试用例，**不写解答**，除非用户明确要求。用户自己写解答和感悟。
- 不要改动用户已经写过的「感悟」区和解答代码。
- 语言为 Python 3。
