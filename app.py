import streamlit as st
from rag_backend.config import setup_env
from rag_backend.loader import load_and_split
from rag_backend.embeddings import create_vector_database
from rag_backend.rag_chain import build_rag_chain

# Initialize environment variables
if "api_key" not in st.session_state:
    st.session_state.api_key = setup_env()

if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title(" Webpage RAG Chatbot")
st.sidebar.title("How to use")
st.sidebar.markdown(
    """
    1. Paste a webpage URL in the input box.  
    2. Click **Process URL**.  
    3. Ask questions about the content.  
    """
)

# URL input
url = st.text_input("Enter a URL:")

# Process URL
if st.button("Process URL") and url:
    with st.spinner("Processing URL..."):
        splits = load_and_split(url)
        st.session_state.vectorstore = create_vector_database(
            splits, api_key=st.session_state.api_key
        )
    st.success(" URL processed successfully! You can now ask questions.")
    st.session_state.messages = []  # clear old chat history

# Chat interface
if st.session_state.vectorstore:
    # Display chat history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Ask a question about the webpage..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.spinner("Thinking..."):
            rag_chain = build_rag_chain(
                st.session_state.vectorstore, st.session_state.api_key
            )
            response = rag_chain.invoke(prompt)

        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})