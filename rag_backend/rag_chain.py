from langchain import hub
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

def build_rag_chain(vectorstore, api_key):
    retriever = vectorstore.as_retriever()
    prompt = hub.pull('rlm/rag-prompt')
    llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash', google_api_key=api_key)

    def format_docs(docs):
        return '\n'.join(doc.page_content for doc in docs)

    return (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
