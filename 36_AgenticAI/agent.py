from agno.agent import Agent  # Learn to use AGNO ,its easy and will help as a subsystem at many places

#from agno.models.openai import OpenAIResponses
from agno.models.groq import Groq

from dotenv import load_dotenv

from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.baidusearch import BaiduSearchTools

load_dotenv()

def build_agent():
    return Agent(
        model=Groq(id="qwen/qwen3.6-27b"),
        #tools=[DuckDuckGoTools()], # no this agent can search on web using this agno tool duckduckgo
        tools=[BaiduSearchTools()],
        description="You are a search agent that helps users find the most relevant information using Baidu.",

        markdown=True, # ans in formatted way
        instructions="You are a helpful and expert travel agent.",
        add_datetime_to_context=True # to add the context of current time , so it returns relevent ans 
    )

agent = build_agent()

agent.print_response("Is it safe to travel to UAE today?")