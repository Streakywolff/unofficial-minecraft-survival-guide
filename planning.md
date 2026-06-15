Domain
The domain for this project is minecraft surival tips. Many useful tips for how to survive the first night in a dangerous game where monsters come out of hiding at night. Many useful tips from community guides, forums, and player created resources. This project creates an guide for players to succed in their first night of minecraft

Documents

Sources include ten Minecraft survival guide documents covering:
Early game survival
Gathering resources
Mining strategies
Diamond mining
Food and farming
Mob combat and defense
Village strategies
Nether survival
Enchanting and equipment
Base building and exploration

Document files:

doc1.txt
doc2.txt
doc3.txt
doc4.txt
doc5.txt
doc6.txt
doc7.txt
doc8.txt
doc9.txt
doc10.txt

Chunking Strategy
Documents will be spilt into chunks of apporixmately 500 characters with 100 characters of overlap. The minecraft guide usally contain multiple tips in a paragraph, so medium-sized chunks help preserve context while still allowing specific information to be retrieved. this will help prevent information from being split.
Retrieval Approach
The project will use the all-MiniLM-L6-v2 embedding model from sentence-transformers. The vector database will be ChromaDB. For each query, the system will retrieve the top 5 most relevant chunks. While semantic search will allow users to find revelevent surival advice even when their wording differs from the documents.

Evaluation Plan
What should users do one the first day?
Gather resources, food, collect usefull tools, and build a shelter
How can players survive hostile mobs at night?
build sheleter,gather wool for a bed, sleep at night, or uses torches to prevent monsters from spawning.
how can players obtain reliable food?
kill animals, build a farm, or raid villages.

Anticiplated challenges
Different documents might provide different tips
Some documents are arranged differently
some unrelated advice might be shared
important information might be split too

AI tools
Claude and ChatGPT will be very useful inorder to determine what went wrong.

Architecture

Documents
↓
Chunking
↓
Embeddings (all-MiniLM-L6-v2)
↓
ChromaDB Vector Store
↓
Retrieval
↓
Groq LLM
↓
Answer + Sources