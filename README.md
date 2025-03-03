# Agent Scraper

A simple AI agent that uses the ReAct pattern to search for and download web content about specific topics. Built with LangChain and OpenAI.

## Features

- **Topic-based Web Search**: Finds relevant web pages for any given topic
- **Automatic Content Download**: Saves web pages as HTML files
- **ReAct Pattern Implementation**: Uses reasoning and acting to complete tasks
- **LangSmith Integration**: Uses LangSmith for prompt management
- **Rate Limiting**: Built-in delays to avoid search API issues

## Prerequisites

- Python 3.8+
- OpenAI API key
- LangSmith API key

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd agent-scraper
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root with your API keys:
```
OPENAI_API_KEY=your_openai_api_key
LANGSMITH_API_KEY=your_langsmith_api_key
```

## Usage

Run the script:
```bash
python react.py
```

The script will:
1. Search for relevant web pages about the specified topic
2. Download the found pages as HTML files
3. Save the files in the `downloads` directory

## Project Structure

```
agent-scraper/
├── react.py              # Main script with agent implementation
├── requirements.txt      # Project dependencies
├── .env                 # Environment variables (create this)
└── downloads/           # Directory for downloaded web pages
```

## How It Works

The agent uses the ReAct (Reasoning and Acting) pattern:
1. **Reasoning**: The agent thinks about how to research the topic
2. **Acting**: The agent performs actions (searching and downloading)
3. **Observing**: The agent analyzes the results
4. **Repeating**: The process continues until sufficient information is gathered

## Tools

The agent has access to two main tools:
1. **SearchTopics**: Finds relevant URLs for a given topic
2. **DownloadPage**: Downloads and saves web pages as HTML files

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details. 
