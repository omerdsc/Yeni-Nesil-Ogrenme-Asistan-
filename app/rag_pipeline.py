# app/rag_pipeline.py

from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.document_loaders import TextLoader



import os
from dotenv import load_dotenv
load_dotenv()  # .env dosyasını yükle

openai_api_key = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = openai_api_key


def load_documents(file_path: str):
    loader = TextLoader(file_path)
    documents = loader.load()
    return documents


def create_vectorstore(documents):
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(docs, embeddings)
    return vectorstore


def get_qa_chain(vectorstore):
    retriever = vectorstore.as_retriever()
    llm = ChatOpenAI(model_name="gpt-3.5-turbo")
    chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return chain


def ask_with_rag(question: str):
    docs = load_documents("app/data/sample_notes.txt")
    vectorstore = create_vectorstore(docs)
    qa_chain = get_qa_chain(vectorstore)

    result = qa_chain.run(question)
    return result
