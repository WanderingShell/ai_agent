from ai_agent import DOCS_DIR

# PDF文件路径
pdf_path = DOCS_DIR / "rag.pdf"

from unstructured.partition.auto import partition

# 使用unstructured加载并解析PDF文档
elements = partition(
    filename=pdf_path.as_posix(),
    content_type="application/pdf",
)

print(f"解析完成：{len(elements)} 个元素，{sum(len(str(e)) for e in elements)} 字符")

# 统计元素类型
from collections import Counter

types = Counter(e.category for e in elements)
print(f"元素类型：{dict(types)}")

# 显示所有元素
print("\n所有元素：")
for i, element in enumerate(elements, start=1):
    print(f"Element {i} ({element.category}):")
    print(element)
    print("=" * 60)
