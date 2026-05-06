from rag.vector_store import retriever

def query_annual_report_data(query: str):
    results = retriever.invoke(query)
    return results