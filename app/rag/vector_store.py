from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.rag.embeddings import embedding_model

def create_vector_store(documents):

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    split_docs = text_splitter.split_documents(documents)

    vector_store = FAISS.from_documents(
        split_docs,
        embedding_model
    )

    return vector_store