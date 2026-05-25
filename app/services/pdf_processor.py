from langchain_text_splitters import RecursiveCharacterTextSplitter
from pypdf import PdfReader
import os

class PDFProcessorService:
    def __init__(self, chunk_size: int = 500, chunk_overlap: int = 50):
        # Production Standard: Initialize splitting strategies with strict parameters
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
            separators=["\n\n", "\n", " ", ""]  # Smart falling back to preserve structural paragraphs
        )

    async def extract_and_chunk(self, file_path: str) -> list[dict]:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Target document artifact not found at: {file_path}")

        try:
            # 1. Initialize PyPDF stream reader
            reader = PdfReader(file_path)
            processed_chunks = []

            # 2. Extract textual strings per individual page layer
            for page_idx, page in enumerate(reader.pages):
                page_text = page.extract_text() or ""
                if not page_text.strip():
                    continue

                # 3. Compute structural semantic boundaries via Recursive Character Splitting
                chunks = self.text_splitter.split_text(page_text)

                for chunk_idx, chunk_content in enumerate(chunks):
                    processed_chunks.append({
                        "metadata": {
                            "source_file": os.path.basename(file_path),
                            "page_number": page_idx + 1,
                            "chunk_index": chunk_idx
                        },
                        "page_content": chunk_content
                    })

            return processed_chunks

        except Exception as e:
            raise RuntimeError(f"Failed to execute RAG data parsing sequence: {str(e)}")