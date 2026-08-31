import os
import json
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# Load Config

with open("config.json", "r") as f:
    config = json.load(f)
provider = config["provider"]

# Initialise the LLM

def get_llm():
    if provider == "openai":
        llm = ChatOpenAI(
            model = config["openai"]["model"],
            temperature = config["openai"]["temperature"],
            max_tokens = config["openai"]["max_token"],
            api_key = os.getenv("OPENAI_API_KEY")
        )
        return llm
    elif provider == "gemini":
        llm = ChatGoogleGenerativeAI(
            model = config["gemini"]["model"],
            temperature = config["gemini"]["temperature"],
            max_tokens = config["gemini"]["max_token"],
            api_key = os.getenv("GEMINI_API_KEY")
        )
        return llm
    else:
        raise ValueError("Invalid provider in config.json (It must be openai or gemini only)")