from agno.agent import Agent
from agno.models.groq import Groq
from agno.db.sqlite import SqliteDb
from rich.pretty import pprint
from dotenv import load_dotenv
import sqlite3

load_dotenv()

db = SqliteDb(db_file="agno.db")
db.clear_memories()

def build_agent():
    return Agent(
        db=db,
        model=Groq(id="openai/gpt-oss-120b"),
        markdown=True,
        add_history_to_context=True,
        enable_user_memories=True
    )

agent = build_agent()

user_id = "user_1"
agent.print_response(
    "Remember that my favorite city is Pune.",
    user_id=user_id
)

agent.print_response(
    "What is my favorite city?",
    user_id=user_id
)

print("MEMORIES : ")
memories = db.get_user_memories(user_id=user_id)
pprint(memories)