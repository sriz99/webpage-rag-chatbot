import os, shutil
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma

def create_vector_database(splits, api_key, persist_directory="./chroma_db"):
    if os.path.exists(persist_directory):
        shutil.rmtree(persist_directory)

    embeddings = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-001", google_api_key=api_key
    )
    return Chroma.from_documents(
        documents=splits,
        embedding=embeddings,
        persist_directory=persist_directory,
    )
