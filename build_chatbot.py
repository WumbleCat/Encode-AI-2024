import os
import chainlit as cl
from langchain import HuggingFaceHub, PromptTemplate, LLMChain

from getpass import getpass
HUGGINGFACEHUB_API_TOKEN = getpass()
os.environ["HUGGINGFACEHUB_API_TOKEN"] = HUGGINGFACEHUB_API_TOKEN