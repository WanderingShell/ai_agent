import os
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"
from visual_bge.visual_bge.modeling import Visualized_BGE
import torch
from ai_agent import DOCS_DIR, MODELS_DIR


model = Visualized_BGE(model_name_bge="BAAI/bge-base-en-v1.5",
                       model_weight=  MODELS_DIR / "bge" / "Visualized_base_en_v1.5.pth")
model.eval()

with torch.no_grad():
    text_emb = model.encode(text="blue whale")
    img_emb_1 = model.encode(image=DOCS_DIR / "datawhale01.png")
    multi_emb_1 = model.encode(
        image=DOCS_DIR / "datawhale01.png",
        text="blue whale"
    )
    img_emb_2 = model.encode(image=DOCS_DIR / "datawhale02.png")
    multi_emb_2 = model.encode(
        image=DOCS_DIR / "datawhale02.png",
        text="blue whale"
    )

# 计算相似度
sim_1 = img_emb_1 @ img_emb_2.T  # type: ignore
sim_2 = img_emb_1 @ multi_emb_1.T  # type: ignore
sim_3 = text_emb @ multi_emb_1.T  # type: ignore
sim_4 = multi_emb_1 @ multi_emb_2.T  # type: ignore

print("=== 相似度计算结果 ===")
print(f"纯图像 vs 纯图像: {sim_1}")
print(f"图文结合1 vs 纯图像: {sim_2}")
print(f"图文结合1 vs 纯文本: {sim_3}")
print(f"图文结合1 vs 图文结合2: {sim_4}")

# 向量信息分析
print("\n=== 嵌入向量信息 ===")
print(f"多模态向量维度: {multi_emb_1.shape}")  # type: ignore
print(f"图像向量维度: {img_emb_1.shape}")  # type: ignore
print(f"多模态向量示例 (前10个元素): {multi_emb_1[0][:10]}")  # type: ignore
print(f"图像向量示例 (前10个元素):   {img_emb_1[0][:10]}")  # type: ignore
