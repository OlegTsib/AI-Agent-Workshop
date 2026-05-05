from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

db_location = "./chrome_db"
embeddings = OllamaEmbeddings(model="mxbai-embed-large")
db = Chroma(collection_name="annual_report_2025", persist_directory=db_location, embedding_function=embeddings)
top_k = 5
retriever = db.as_retriever(search_kwargs={"k": top_k})
