import streamlit as st

def faq():
    st.markdown(
        """
# FAQ
## What is finGPT?
finGPT is an AI-powered tool that makes stock recommendations based on live data from Google Finance. It uses the Meta-Llama/Meta-Llama-3.1-405B-Instruct model via Nebius AI Studio to analyze financial data and generate insights tailored to your queries.

## How does finGPT work?
When you input a query, finGPT retrieves the most relevant data from Google Finance, processes it using advanced language models, and provides a recommendation or insight. The process involves semantic search to locate relevant information and then a refined AI model to interpret the data and generate responses.

## Are finGPT’s stock recommendations 100% accurate?
No, AI models like Meta-Llama are highly capable but can occasionally make mistakes or miss context. Recommendations are based on data available at the time and may not account for real-time market shifts or complex financial events.

## Can I rely on finGPT’s recommendations for investment decisions?
finGPT provides useful insights, but it’s advised to use these recommendations as part of a broader research process. For significant investment decisions, consider consulting additional resources or a financial advisor to confirm finGPT’s insights.
"""
    )
