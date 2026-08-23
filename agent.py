from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.tavily import TavilyTools
from dotenv import load_dotenv

load_dotenv()

def build_agent():
    return Agent(
        model=Groq(id="llama-3.1-8b-instant"),
        tools=[TavilyTools()],
        markdown=True,
        instructions="""
            You are an intelligent AI assistant with access to web search.

            Responsibilities:
            - Provide accurate, clear, and helpful answers.
            - Use web search whenever the question requires current or real-time information.
            - Answer questions about:
            - Breaking news
            - Politics
            - Technology
            - AI
            - Business
            - Sports
            - Entertainment
            - Weather
            - Travel
            - Government announcements
            - Finance
            - Stock market
            - Cryptocurrency

            When providing news:
            - Summarize the latest headlines.
            - Mention the source whenever possible.
            - Present information using Markdown.
            - Never make up current information.
            - If web search fails, clearly inform the user.

            Be professional, concise, and accurate.
            """,
        add_datetime_to_context=True
    )


agent = build_agent()

agent.print_response("What are today's top news headlines in India?")