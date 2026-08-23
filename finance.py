from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.tavily import TavilyTools
from agno.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()

def build_agent():
    return Agent(
        model=Groq(id="llama-3.1-8b-instant"),
        tools=[
            YFinanceTools(all=True), TavilyTools()],
        markdown=True,
        description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
        instructions=[
            "Use given tools when possible. Format your response using markdown and use tables where appropriate."
        ],
        add_datetime_to_context=True
        # debug_mode=True
    )

agent = build_agent()

agent.print_response("Share the MSFT stock price in INR and show the current exchange rate.")