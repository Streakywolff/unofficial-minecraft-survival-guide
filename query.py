#program summary: This program retrieves relevant Minecraft survival documents chunks from ChormaDB using sematic search, sends them to a grok AI model, and gives back
#a answer based on sources it recieved
import os
from dotenv import load_dotenv
from groq import Groq
from sentence_transformers import SentenceTransformer
import chromadb
##loads the variables from the .env file
load_dotenv()

model = SentenceTransformer("all-MiniLM-L6-v2")##loads the embedding model used for semantic search
client = chromadb.PersistentClient(path="chroma_db")##connects to the DB data base
collection = client.get_or_create_collection(name="minecraft_survival")#opens the collection containing minecraft documents 
#                                                                       embedding


groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))##creates a groq client using the API key 


def retrieve_chunks(question, top_k=5):##finds the most revelent document chunks for the user's question
    query_embedding = model.encode(question).tolist()##turns the users question into an embedding vector
    #searches ChromaDB for the most simliar document chunk
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    chunks = []

    for i in range(len(results["documents"][0])):
        chunks.append({#stores the retrieved chunk text, source file, and similar score
            "text": results["documents"][0][i],
            "source": results["metadatas"][0][i]["source"],
            "distance": results["distances"][0][i]
        })

    return chunks


def ask(question):##sends the retrieved chunk to the AI model to get an answer
    chunks = retrieve_chunks(question)##retrieves the most revelent chunk for the users question

    context = ""##builds a context string containing the retrieved documents
    sources = []

    for i, chunk in enumerate(chunks, start=1):
        context += f"\n[Source {i}: {chunk['source']}]\n{chunk['text']}\n"
        sources.append(chunk["source"])

    ##creates the prompt that will be sent, and answers the question with only the information provided
    prompt = f"""
Answer the question using only the information in the provided sources.
If the sources do not contain enough information, say:
"I do not have enough information from the documents to answer that."

Question:
{question}

Sources:
{context}
"""

    response = groq_client.chat.completions.create( ##sends the question and retrieved context to groq
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that only answers using the provided retrieved documents."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2##makes answers more focused
    )

    answer = response.choices[0].message.content #extracts the generated answer for the API respone

    return {##returns the answer
        "answer": answer,
        "sources": sorted(set(sources)),
        "chunks": chunks
    }


if __name__ == "__main__":##runs the chatbot in the terminal 
    question = input("Ask a Minecraft survival question: ")##gets question from the user
    result = ask(question)##runs the Rag pipeline

    print("\nAnswer:")
    print(result["answer"])#displays the generated answer

    print("\nSources:")##displays which documents where used
    for source in result["sources"]:
        print("-", source)