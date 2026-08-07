__version__ = "0.1.0"
__author__ = "DonLee"
__email__ = "li.dong.7951@gmail.com"

__all__ = ["PROJECT_ROOT", "DOCS_DIR", "MODELS_DIR"]

from .paths import PROJECT_ROOT
from .paths import DOCS_DIR
from .paths import MODELS_DIR
from dotenv import load_dotenv

# 加载虚拟环境变量
load_dotenv()

# from openai import OpenAI
# import os
#
# client = OpenAI(
#     api_key=os.getenv("DEEPSEEK_API_KEY"),
#     base_url=os.getenv("DEEPSEEK_BASE_URL"),
# )
#
# completion = client.chat.completions.create(
#     model=os.getenv("DEEPSEEK_MODEL_NAME"),
#     messages=[
#         {"role": "system",
#          "content": "你是 Kimi，由 deepseek AI 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。Moonshot AI 为专有名词，不可翻译成其他语言。"},
#         {"role": "user", "content": "你好，请问如何系统性的学习AIAgent开发？"}
#     ]
# )
#
# print(completion.choices[0].message.content)
