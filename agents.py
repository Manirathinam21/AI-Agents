import os
from crewai import Agent
from tools import yt_tool
from dotenv import load_dotenv


load_dotenv()
OPENAI_API_KEY=os.getenv('OPENAI_API_KEY')
os.environ['OEAN_API_KEY']= OPENAI_API_KEY
os.environ['']



