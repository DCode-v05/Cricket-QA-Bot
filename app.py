# Importing Dependencies
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

# Cricket Information in Document
cricket_document_data="""
Cricket is a bat-and-ball game played between two teams of eleven players each. 
The game is played on an oval field with a 22-yard-long pitch at the center. 
Each team alternates between batting and bowling/fielding. The batting team tries to score runs by hitting the ball and running between the wickets, 
while the bowling team aims to dismiss the batsmen by bowling them out, catching the ball, or hitting the wickets.

Cricket matches are played in various formats:
Test matches: Played over five days with two innings per team.
One Day Internationals (ODIs): Each team plays a maximum of 50 overs.
T20 matches: Each team plays 20 overs, making the game fast-paced and exciting.

Each player has a specialized role:
Batsman: Focuses on scoring runs.
Bowler: Delivers the ball to get batsmen out.
All-rounder: Can bat and bowl effectively.
Wicketkeeper: Stands behind the stumps to catch the ball and perform stumpings.

Some famous cricket players include Sachin Tendulkar, Virat Kohli, Rohit Sharma, MS Dhoni, and Suresh Raina.
Teams are known for their strategic combinations of batsmen, bowlers, and fielders.

Major cricket tournaments include:
ICC Cricket World Cup - The international championship for 50-over matches, held every four years.
ICC T20 World Cup - International T20 tournament.
Indian Premier League (IPL) - A professional T20 league in India featuring franchises and international players.
Big Bash League (BBL) - T20 league in Australia.

Other interesting facts:
A run is scored when batsmen successfully run between the wickets.
A boundary scores 4 runs if the ball touches the ground before crossing the boundary, and 6 runs if it crosses without touching the ground.
A bowler can deliver a legal over consisting of 6 balls.
Cricket has many strategies like field placements, batting order, bowling variations, and powerplays that make it a highly tactical game.
"""

# Convert Raw Text to Document - Langchain expect Document format
cricket_document=Document(page_content=cricket_document_data)

# Temperature - Control the Creativity of the model's responses
model=ChatGoogleGenerativeAI(model="models/gemini-2.0-flash", temperature=0, google_api_key=os.getenv("GEMINI_API_KEY")) # 0 - focused responses, 1 - creative responses

# Prompt Tuning to Guide the Model to Focus on the Cricket
qa_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Answer the question using only the provided context.\n\nContext:\n{context}"),
    ("human", "{input}"),
])

# Function to format context documents
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# Creating the Chain for Question Answering - Context -> Input -> Tuned Prompt
stuff_chain = (
    {
        "context": lambda x: format_docs(x["context"]),
        "input": lambda x: x["input"]
    } | qa_prompt | model | StrOutputParser()
)

questions = [
    "What are the different formats of cricket?",
    "Who are some famous cricket players mentioned in the document?",
    "What is the role of a bowler in cricket?",
    "What is the Indian Premier League (IPL)?",
    "How is a boundary scored in cricket?"
]

for question in questions:
    answer=stuff_chain.invoke({"input": question, "context": [cricket_document] }) # Starting the Chain with Context and Input
    print(f"Q: {question}")
    print(f"A: {answer}\n")