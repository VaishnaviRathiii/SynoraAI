from textwrap import dedent
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.youtube import YouTubeTools
from dotenv import load_dotenv

load_dotenv()

def build_youtube_agent():
    return Agent(
        name="YouTube Agent",
        model=Groq(id="openai/gpt-oss-120b"),
        tools=[YouTubeTools()],
        instructions=dedent("""
            You are an expert YouTube content analyst with a keen eye for detail! 🎓

            Follow these steps for comprehensive video analysis:

            1. Video Overview
            - Check video length and basic metadata.
            - Identify the video type.
            - Summarize the overall purpose.

            2. Timestamp Creation
            - Create accurate timestamps.
            - Highlight major topic transitions.
            - Format:
                [Start Time - End Time] Summary

            3. Content Organization
            - Group related segments.
            - Identify main themes.
            - Highlight key learning points.
            - Mention practical demonstrations.

            Guidelines:
            - Never hallucinate timestamps.
            - Base your analysis on the transcript and metadata.
            - Use Markdown formatting.
            - Be concise, accurate, and well-structured.
        """),
        add_datetime_to_context=True,
        markdown=True,
    )

# youtube_agent.print_response(
#     "Analyze this video: https://www.youtube.com/watch?v=Z-pT0XDYvDM",
#     stream=True,
# )