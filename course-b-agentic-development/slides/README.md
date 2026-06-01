# 课程 B 完整 PPT 文件

本目录存放 12 周课程的可编辑 PPT 文件和生成脚本。

## 文件结构

- `pptx/`：生成后的 `.pptx` 文件，每周一个。
- `generate_course_b_pptx.py`：PPT 生成脚本，使用 LibreOffice UNO，不引入额外 Python 包。

## 生成方式

在仓库根目录运行：

```bash
/usr/bin/python3 ai-course-system/course-b-agentic-development/slides/generate_course_b_pptx.py
```

脚本会启动 headless LibreOffice，生成 `pptx/week-01.pptx` 至 `pptx/week-12.pptx`。

## 教学使用说明

这些 PPT 文件是授课版课件，不是宣传页。每周课件都围绕概念、演示、课堂活动、实验交付、测试 / Review / Human Gate 展开。教师可根据学校课时压缩页面，但不建议删除安全、权限、测试、Review 和复盘相关页面。

