import os
from langchain_ollama import OllamaEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import CharacterTextSplitter

loader = TextLoader("Data/example.txt")
documents = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)

embeddings = OllamaEmbeddings(model="bge-m3")

vectorstore = FAISS.from_documents(texts, embeddings)

def query(keyword: str):
    return vectorstore.similarity_search(keyword)
