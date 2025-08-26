import os
from langchain_ollama import OllamaEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain.schema import Document  

loader = TextLoader("Data/example.txt")
documents = loader.load()

manual_documents = []
for doc in documents:
    if hasattr(doc, 'page_content'):
        paragraphs = doc.page_content.split('\n\n')  
        for para in paragraphs:
            manual_documents.append(Document(page_content=para, metadata=doc.metadata))

embeddings = OllamaEmbeddings(model="bge-m3")

vectorstore = FAISS.from_documents(manual_documents, embeddings)
def query(keyword: str):
    return (vectorstore.similarity_search(keyword, k=1))[0]

if __name__ == "__main__":
    pass
