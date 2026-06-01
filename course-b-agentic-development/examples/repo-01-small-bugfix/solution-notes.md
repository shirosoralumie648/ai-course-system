# Solution Notes：Repo 01 Small Bugfix

## 参考答案用途

本文件供教师和助教批改使用。不要在实验开始前直接发给学生。

## 预期修改文件

只需要修改：

- `src/grade_utils.py`

不需要修改：

- `tests/test_grade_utils.py`
- `pyproject.toml`
- README 或教师说明

## 参考修复

```python
def average_score(scores):
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


def pass_rate(scores):
    if not scores:
        return 0.0
    passing = [score for score in scores if score >= 60]
    return len(passing) / len(scores)
```

## 验证命令

```bash
python -m unittest discover -s tests -v
```

修复后应看到 5 个测试通过。

## 可接受变体

- `average_score` 返回 `0` 也可接受，因为与 `0.0` 数值相等。
- `pass_rate` 可以使用生成器表达式实现，只要 60 分被计入及格即可。

## 不可接受做法

- 删除失败测试。
- 修改测试期望来适配错误代码。
- 新增依赖解决简单逻辑问题。
- 未提供测试日志却声称测试通过。
