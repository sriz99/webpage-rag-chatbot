from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_and_split(url, chunk_size=1000, chunk_overlap=200):
    loader = WebBaseLoader(web_path=[url])
    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size,
                                                   chunk_overlap=chunk_overlap)
    return text_splitter.split_documents(docs)