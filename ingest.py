#builds a vector database for retrieval-augmented generation application, it loads textfiles from the local folder and removes uncessary junk from it, and splits
#document into smaller overlapping chunks. each chunk is converted into a numerical embedding using sentenceTransformer allowing semantic meaning to be captured. then 
#finally embeddings, chunktext, and source data are stored into ChormaDB collection
#
#
from pathlib import Path
from sentence_transformers import SentenceTransformer
import chromadb

# this holds the address of all text documents
DOCUMENTS_DIR = Path("documents")

#loads the AI embedding model and turns text into numbers so ChormaDB can read it
model = SentenceTransformer("all-MiniLM-L6-v2")


def load_documents():##loads all the text files into memory and cleans them up
    documents = []##stores all documents we load
    #words we do not want in the document
    junk_phrases = [
        "View User Profile",
        "View Posts",
        "Send Message",
        "Join Date:",
        "Discord:",
        "Minecraft:",
        "PMC:"
    ]

    for file_path in DOCUMENTS_DIR.glob("*.txt"):##iterates through every document file
        ##reads text inside, also prevents crashes
        text = file_path.read_text(
            encoding="utf-8",
            errors="ignore"
        )

        ##removes the junk from the text
        for phrase in junk_phrases:
            text = text.replace(phrase, "")

        ##saves the document and file name
        documents.append({
            "source": file_path.name,
            "text": text
        })

    return documents


def chunk_text(text, chunk_size=500, overlap=100):##breaks down larger chunks into smaller pieces
    ##stores the smaller piece of data
    chunks = []
    start = 0

    ##makes chunks until we reacch the end
    while start < len(text):
        end = start + chunk_size ##the end of the chunk is 500 characters from the start
        chunk = text[start:end].strip()

        if chunk:##only saves the chunk if its not empty
            chunks.append(chunk)
        ##moves forward by 400 characters which creates a 100 character overlap
        start += chunk_size - overlap

    return chunks


def build_database():##creates the vector data base used for retrival
    ##opens or creates a saved ChromaDB database folder
    client = chromadb.PersistentClient(path="chroma_db")

    ##opens or creates a collection inside chormaDB
    collection = client.get_or_create_collection(
        name="minecraft_survival"
    )

    documents = load_documents()
    ##provides an ID for the chunk
    chunk_id = 0

    for doc in documents:##loops through every  document
        chunks = chunk_text(doc["text"])##splits the chunks

        for chunk in chunks:##turns chunks into embeddings(numbers)
            embedding = model.encode(chunk).tolist()

            ##stores the chunk, embeddings, ID, and source files in ChromaDB
            collection.add(
                ids=[str(chunk_id)],
                embeddings=[embedding],
                documents=[chunk],
                metadatas=[
                    {
                        "source": doc["source"]
                    }
                ]
            )
            ##increments the id
            chunk_id += 1
    ##prints the amount of chunks
    print(f"Stored {chunk_id} chunks in ChromaDB")

##makes sure the build_database only runs when this file is run directly
if __name__ == "__main__":
    build_database()