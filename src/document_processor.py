"""
Document Processor for HR Assistant Agent
Handles loading and processing of HR documents into vector database
"""

import os
from typing import List
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document


class DocumentProcessor:
    """Processes HR documents and creates vector database"""
    
    def __init__(self, data_dir: str = "data", persist_dir: str = "faiss_index", use_gemini: bool = True):
        self.data_dir = data_dir
        self.persist_dir = persist_dir
        self.embeddings = GoogleGenerativeAIEmbeddings(
            model="models/embedding-001",
            google_api_key=os.getenv("GOOGLE_API_KEY")
        )
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len,
            separators=["\n\n", "\n", " ", ""]
        )
        
    def load_documents(self) -> List[Document]:
        """Load all documents from data directory"""
        loader = DirectoryLoader(
            self.data_dir,
            glob="**/*.txt",
            loader_cls=TextLoader,
            show_progress=True
        )
        documents = loader.load()
        print(f"Loaded {len(documents)} documents")
        return documents
    
    def split_documents(self, documents: List[Document]) -> List[Document]:
        """Split documents into chunks"""
        chunks = self.text_splitter.split_documents(documents)
        print(f"Split into {len(chunks)} chunks")
        return chunks
    
    def create_vector_store(self, chunks: List[Document]) -> FAISS:
        """Create and persist vector store"""
        vectorstore = FAISS.from_documents(
            documents=chunks,
            embedding=self.embeddings
        )
        # Save to disk
        vectorstore.save_local(self.persist_dir)
        print(f"Created vector store with {len(chunks)} chunks")
        return vectorstore
    
    def load_vector_store(self) -> FAISS:
        """Load existing vector store"""
        if not os.path.exists(self.persist_dir):
            raise FileNotFoundError(f"Vector store not found at {self.persist_dir}")
        
        vectorstore = FAISS.load_local(
            self.persist_dir,
            self.embeddings,
            allow_dangerous_deserialization=True
        )
        print("Loaded existing vector store")
        return vectorstore
    
    def process_and_store(self) -> FAISS:
        """Complete pipeline: load, split, and store documents"""
        # Check if vector store already exists
        if os.path.exists(self.persist_dir):
            print("Vector store already exists. Loading...")
            return self.load_vector_store()
        
        # Process documents
        print("Processing documents...")
        documents = self.load_documents()
        chunks = self.split_documents(documents)
        vectorstore = self.create_vector_store(chunks)
        
        return vectorstore


if __name__ == "__main__":
    # Test the document processor
    processor = DocumentProcessor()
    vectorstore = processor.process_and_store()
    
    # Test retrieval
    query = "How many sick leaves do I have?"
    results = vectorstore.similarity_search(query, k=3)
    print(f"\nTest query: {query}")
    print(f"Found {len(results)} relevant chunks")
    for i, doc in enumerate(results, 1):
        print(f"\nChunk {i}:")
        print(doc.page_content[:200])
