import os
from dotenv import load_dotenv
import asyncio

load_dotenv()
API_KEY=os.getenv("API_KEY")

from Agent.agent import run_agent

run_agent(input("input your query:\n"))