from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_react_agent
from langchain.tools import Tool
from langsmith import Client
from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup
from googlesearch import search
import time

# Load environment variables
load_dotenv()

def download_page(url: str) -> str:
    """Download and save a webpage."""
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
        os.makedirs('downloads', exist_ok=True)
        filename = url.replace('https://', '').replace('http://', '').replace('/', '_')
        with open(f'downloads/{filename}.html', 'w', encoding='utf-8') as f:
            f.write(response.text)
        return f"Downloaded {url}"
    except Exception as e:
        return f"Error: {str(e)}"

def search_topics(topic: str) -> list:
    """Search for topics."""
    try:
        urls = []
        # Use the provided topic in search queries
        queries = [
            f"{topic} paper",
            f"{topic} tutorial",
            f"{topic} implementation"
        ]
        for query in queries:
            urls.extend(list(search(query, num_results=2)))
            time.sleep(2)
        return urls
    except Exception as e:
        return [f"Error: {str(e)}"]

# Create tools and agent
tools = [
    Tool(name="SearchTopics", func=search_topics, description="Search for topics. Input should be a topic string."),
    Tool(name="DownloadPage", func=download_page, description="Download a webpage")
]

# Initialize LangSmith client
client = Client(api_key=os.getenv("LANGSMITH_API_KEY"))

# Pull the prompt from LangSmith
prompt = client.pull_prompt("hwchase17/react", include_model=True)

# Initialize the language model
llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")  # Changed back to gpt-3.5-turbo as it's more stable

# Create the ReAct agent
agent = create_react_agent(llm, tools, prompt)
executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

if __name__ == "__main__":
    print("RAG Research Assistant")
    print("=====================")
    result = executor.invoke({
        "input": "Find and download high-quality content about Retrieval Augmented Generation (RAG)"
    })
    print("\nResults:")
    print(result["output"]) 