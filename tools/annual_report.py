from rag.query import query_annual_report_data 

def annual_report(query: str) -> str:
    try:
        results = query_annual_report_data(query)
        if not results:
            return "No relevant information found in the annual report."

        # Build response from relevant chunks
        response_parts = [f"Found {len(results)} relevant section(s) in the annual report:\n"]
        
        """
        RESPONSE EXAMPLE:
        {
            "source": "FastFeast Annual Report 2025.pdf",
            "chunk": 1,
            "total_chunks": 10,
            "doc_type": "annual_report"
        }
        """

        for i, result in enumerate(results, 1):
            content = result.page_content.strip()
            metadata = result.metadata
            chunk_num = metadata.get('chunk', '?')
            total_chunks = metadata.get('total_chunks', '?')
            
            response_parts.append(f"--- Section {i} (chunk {chunk_num}/{total_chunks}) ---")
            response_parts.append(content)
            response_parts.append("")
        
        return "\n".join(response_parts)
    
    except Exception as e:
        return f"Error searching annual report: {str(e)}"