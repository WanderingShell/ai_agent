import os
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"

from ai_agent import DOCS_DIR
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_experimental.text_splitter import SemanticChunker

embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-zh-v1.5",
    model_kwargs={'device': 'cpu'},
    encode_kwargs={'normalize_embeddings': True}
)

# 初始化 SemanticChunker
text_splitter = SemanticChunker(
    embeddings,
    breakpoint_threshold_type="percentile"  # 断点识别方法
)

loader = TextLoader(DOCS_DIR / "蜂医.txt")
documents = loader.load()

docs = text_splitter.split_documents(documents)

print(f"文本被切分为 {len(docs)} 个块。\n")
print("--- 全部内容如下 ---")
for i, doc in enumerate(docs):
    print("=" * 60)
    # doc 是一个 Document 对象，需要访问它的 .page_content 属性来获取文本
    print(f'块 {i + 1} (长度: {len(doc.page_content)}): "{doc.page_content}"')
