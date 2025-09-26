# RAG-powered Webpage QA with Gemini

A simple **Retrieval-Augmented Generation (RAG)** application that lets you paste any webpage URL and interact with its content using natural language questions. The app uses **LangChain**, **Gemini embeddings/LLM**, and **ChromaDB** for document retrieval, with a clean **Streamlit** web interface.

---

## Features
-  Load and index any webpage by providing its URL  
-  Split webpage content into chunks for efficient retrieval  
-  Store and search embeddings with ChromaDB  
-  Ask questions and get context-aware answers powered by **Gemini**  
-  Chat-style interface with conversation history  

---

## Tech Stack
- [Streamlit](https://streamlit.io/) – Web UI  
- [LangChain](https://www.langchain.com/) – RAG framework  
- [Google Gemini](https://ai.google/) – LLM + Embeddings  
- [Chroma](https://www.trychroma.com/) – Vector database  

---

## Project Structure

```bash
webpage-rag-chatbot/
├── app.py                  # Streamlit entrypoint (UI)
├── rag_backend/            # Core functions
│   ├── config.py           # setup_env()
│   ├── loader.py           # load_and_split()
│   ├── embeddings.py       # create_vector_database()
│   └── rag_chain.py        # build_rag_chain()
├── requirements.txt
├── .env
└── README.md
```
##  Setup

### 1. Clone the Repository
```bash
git clone https://github.com/sriz99/webpage-rag-chatbot.git
cd webpage-rag-chatbot
```
### 2. Create and activate a virtual environment
```bash
# Virtual Environment
python -m rag_chatbot venv 
source rag_chatbot/bin/activate # On Linux
rag_chatbot\Scripts\activate # On Windows
```
### 3. Install the dependencies
```bash
pip install -r requirements.txt
```

### 4. Add API Key

Create a `.env` file in the project root directory and add the following:
```bash
GOOGLE_API_KEY=your_api_key_here
USER_AGENT=your_user_agent_here
```
The Google API Key can generated from [Google AI Studio](https://aistudio.google.com/api-keys)

### 5. Run the Application
```bash
streamlit run app.py
```
Then open the app in your browser at link generated in your terminal

