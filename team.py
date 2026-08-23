from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.tavily import TavilyTools
from agno.tools.yfinance import YFinanceTools
from agno.team import Team
from dotenv import load_dotenv

load_dotenv()

english_agent = Agent(
    name="English Agent",
    role="You answer questions in English"
)

hindi_agent = Agent(
    name="Hindi Agent",
    role="You answer questions in Hindi"
)

marathi_agent = Agent(
    name="Marathi Agent",
    role="You answer questions in Marathi"
)

team_leader = Team(
    name="Answer & Translation Team",
    members=[english_agent, hindi_agent, marathi_agent],
    model=Groq(id="llama-3.1-8b-instant"),
    markdown=True,
    show_members_responses=True,
    instructions="All agents must respond ro answer the query in their specific language. Do not route to just one agent. Output the response of all agents. "
)

team_leader.print_response("What is Capital of India?")