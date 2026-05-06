from pathlib import Path
from tqdm import tqdm
from vector_store import db
from langchain_core.documents import Document
import fitz
from langchain_text_splitters import RecursiveCharacterTextSplitter

def index_pdf_chunked(pdf_filename: str, doc_type: str):
    pdf_path = Path(__file__).parent / pdf_filename
    
    if not pdf_path.exists():
        print(f"❌ File not found: {pdf_path}")
        return
    
    # Extract all text from PDF
    doc = fitz.open(pdf_path)
    full_text = ""
    for page in doc:
        full_text += page.get_text() + "\n\n"
    doc.close()
    
    
    # Chunk the text
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        separators=["\n\n", "\n", ". ", " "]
    )
    chunks = splitter.split_text(full_text)
    
    # Index chunks
    for i, chunk in enumerate(tqdm(chunks, desc=f"📦 Indexing {pdf_filename}")):
        metadata = {
            "source": pdf_filename,
            "chunk": i + 1,
            "total_chunks": len(chunks),
            "doc_type": doc_type
        }
        doc_id = f"{pdf_filename}_chunk_{i + 1}"
        db.add_documents(
            [Document(page_content=chunk, metadata=metadata)],
            ids=[doc_id]
        )
    
    print(f"✅ Finished indexing {pdf_filename} ({len(chunks)} chunks)")

if __name__ == "__main__":
    index_pdf_chunked("FastFeast Annual Report 2025.pdf", "annual_report_2025")