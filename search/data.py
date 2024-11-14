from pydantic import BaseModel, Field
from openai import OpenAI
from dotenv import load_dotenv
import os
import json
from serpapi.google_search import GoogleSearch

load_dotenv()

client = OpenAI(
        base_url="https://api.studio.nebius.ai/v1/",
        api_key=os.environ.get("NEBIUS_API_KEY"),
)


class SearchRequest(BaseModel):
    "Parameters for search request on google finance"
    query: str = Field(..., title="Search query, e.g. 'GOOG:NASDAQ'")
    symbol: str = Field(..., title="Stock symbol, e.g. 'GOOG' Should be in format 'SYMBOL:EXCHANGE' for trading view charts")


def search_query(user_input: str) -> dict:
    messages = [
        {
            "role": "user",
            "content": f"Generate search request parameters for '{user_input}'"
        }
    ]

    completion = client.chat.completions.create(
        model="meta-llama/Meta-Llama-3.1-405B-Instruct",
        messages=messages,
        extra_body={
            'guided_json': SearchRequest.model_json_schema()
        }
    )

    return json.loads(completion.choices[0].message.content)


def get_financial_data(user_input: str) -> dict:

    generated_json = search_query(user_input)

    params = {
        "engine": "google_finance",
        "q": generated_json["query"],
        "api_key": os.environ.get("SERPAPI_API_KEY")
    }

    search = GoogleSearch(params)

    return search.get_dict(), generated_json["query"]


def interpret_data(search_results: dict, user_input: str) -> str:
    messages = [
        {
            "role": "user",
            "content": f"Here is the initial user request '{user_input}'"
        },
        {
            "role": "assistant",
            "content": f"I should use these results from Google:{search_results}"
        },
        {
            "role": "assistant",
            "content": """Let's interpret the data and generate some insights
            Start by presenting the key metrics
            Talk about the company's financial health, income statement,
            balance sheet, casflow, growth prospects, and potential risks
            Talk about recent news and what it might mean for the company
            Always be precise and mention the numbers when possible
            """
        }
    ]

    final_response = client.chat.completions.create(
        model="meta-llama/Meta-Llama-3.1-405B-Instruct",
        messages=messages,
        stream=True
    )

    for chunk in final_response:
        yield chunk.choices[0].delta.content


def respond_to_user(user_input: str) -> str:
    data = get_financial_data(user_input)

    return interpret_data(data, user_input)
