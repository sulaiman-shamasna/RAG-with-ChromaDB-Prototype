import os
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings
from chromadb.utils import embedding_functions

def populate_chromadb(doc_dir):
    # Initialize ChromaDB
    client = chromadb.Client(Settings(
        chroma_db_impl="duckdb+parquet",
        persist_directory="chromadb_store"
    ))

    embed_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )

    # Create a collection
    collection = client.create_collection("documents", embedding_function=embed_fn)

    # Iterate through documents and add to ChromaDB ...
    for filename in os.listdir(doc_dir):
        if filename.endswith('.txt') or filename.endswith('.md'):
            with open(os.path.join(doc_dir, filename), 'r', encoding='utf-8') as f:
                text = f.read()
                # Add to ChromaDB
                collection.add(
                    documents=[text],
                    metadatas=[{"source": filename}],
                    ids=[filename]
                )
    
    client.persist()
    print("ChromaDB has been populated with documents.")

if __name__ == "__main__":
    populate_chromadb('documents')
