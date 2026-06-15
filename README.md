<<<<<<< ours
doc1.txt – Reddit Minecraft survival discussion
doc2.txt – Minecraft forum survival tips
doc3.txt – Minecraft mining and exploration guide
doc4.txt – Minecraft survival Q&A
doc5.txt – Minecraft tips collection
doc6.txt – Expert Minecraft survival guide
doc7.txt – Basic Minecraft survival tips
doc8.txt – Minecraft survival walkthrough
doc9.txt – Winter biome survival guide
doc10.txt – Minecraft survival strategies

Chunking strategy
Documents were spilt into 500 characters with 100 characters of overlap. these numbers were picked because Minecraft guides often include multiple tips within a paragraph. which helps keep context for retrieval and also helps information from not being split.

Source: doc1.txt
Chunk number: 1
==============================
So I'm not a complete amateur, in that I know all the basic survival stuff - don't dig straight down, get sheep so you can sleep for the night, blah blah blah.But what I'm stuck on is all the stuff that comes after figuring out the basics - tips for easy map traversal, more sophisticated combat potential, not being afraid of nighttime anymore. What are some things I should know, as somebody who usually plays creative mode, that are basic but not "Day One" basic?
Build an at least 2 high wall ar

==============================
Source: doc1.txt
Chunk number: 2
==============================
sually plays creative mode, that are basic but not "Day One" basic?
Build an at least 2 high wall around your base, put fences on the very bottom so that spiders can’t climb.

Light up the inside of your base so that every block has a light level of 8 or higher in the night so that no mobs can spawn.

Start a massive sugarcane, cow and a wheat farm inside your safe space asap.

Make yourself a mine for yourself. Make sure to put stairs on the floor and the roof of your staircase to y 12.

For th

==============================
Source: doc1.txt
Chunk number: 3
==============================
e for yourself. Make sure to put stairs on the floor and the roof of your staircase to y 12.

For the majority of your day, stay underground and look for diamonds and lava, make sure to increase your render distance so that your crops can still grow when you are underground, don’t strip mine in a straight line, make sure to stay around your base so that your crops can grow while you are mining, make sure to come back up and collect your sugarcane and wheat and feed your cows until you have at le

==============================
Source: doc1.txt
Chunk number: 4
==============================
ke sure to come back up and collect your sugarcane and wheat and feed your cows until you have at least 3 stacks of sugarcane and leather, and you should have diamonds by now, so make a diamond pick and mine 4 obby and make at least 15 bookshelves and craft an enchanting table and surround it with 15 bookshelves.now you should have enough lapis lazuli and more than 30 levels from mining. Now try all your tools and armour and see which enchantments you can get ALWAYS GET THE MOST BOTTOM ENCHANTME

==============================
Source: doc1.txt
Chunk number: 5
==============================
ll your tools and armour and see which enchantments you can get ALWAYS GET THE MOST BOTTOM ENCHANTMENT look out for these enchantments: efficiency 4 for your tools or sharpness 4 or fire aspect 2 or looting 3 for your sword and fortune 3 or efficiency 4 for your pickaxe and make sure to get nothing but protection for your armour. Now you should be at least 3x stronger than you were before and now you don’t have to stay inside all night since you have your own safe space outside to build on.

Vector Store and semantic searching
The project uses the all-MiniLM-L6-v2 embedding model from sentence-transformers.Embeddings are stored in ChromaDB. User questions are embedded using the same model, and ChromaDB retrieves the five most semantically similar chunks. trade offs are
larger embedding models provide better retriveal quality,less accurate, and very slow

Retrieval Test Results
Query 1
Question: How can I survive the first night

To survive the first night, you should:

1. Build a shelter to protect yourself from monsters and other dangers. A simple dirt or cobblestone structure will suffice for the first night.
2. Explore your surroundings to gather resources such as coal, iron, and diamonds, and find animals to hunt for food.
3. Craft a door to protect yourself from creepers.
4. Gather essential resources like wood, stone, and coal.
5. If possible, craft a bed to skip the night and set your respawn point.
6. Before sunset, make sure you have a shelter, stone tools, a food supply, a light source, and preferably a bed.
7. Stay inside your shelter at night unless you are prepared to fight hostile mobs.
8. Use the night time to organize your inventory, craft useful items, cook food, and begin mining.
Revelent because it tells you to build shelther, what to do before the night

Query 2
Question: How can I get food quick?

To get food quickly, you can try the following options:

1. Slaughter animals, such as cows or pigs, and cook their meat in a furnace. This will restore more hunger than eating raw meat.
2. Harvest crops, such as carrots, potatoes, and beetroot, using a Fortune pickaxe to increase your yield.
3. Mine melon blocks and sweet berries using a Fortune pickaxe to get more food.
4. Craft recipes from wheat, sugar cane, and other ingredients using a crafting table.
Revelent 

Query 3
Question:where can i get good resources





Test results

What should I do on my first day in Minecraft?
Sucessfull it retrieved information revelent to building shelter
How do I survive mobs at night?
sucessfull, it retrieved information revelent to surving at night
How do I find food early game?
sucessfull, it retrieved information revelent to finding food.
=======
# unofficial-minecraft-survival-guide
>>>>>>> theirs
