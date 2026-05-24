from app.services.llm_service import llm

def ask_rag(vector_store, query):
    retriever = vector_store.as_retriever()
    
    # Change get_relevant_documents(query) to invoke(query)
    docs = retriever.invoke(query) 
    
    context = "\n".join([doc.page_content for doc in docs])
    
    prompt = f'''
    Answer the question using the context below.
    
    Context:
    {context}
    
    Question: {query}
    '''
    
    response = llm.invoke(prompt)
    return response.content