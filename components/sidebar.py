import streamlit as st
from components.faq import faq
from dotenv import load_dotenv

load_dotenv()


def sidebar():
    with st.sidebar:
        st.set_page_config(page_title="FinGPT", page_icon="📈📉", layout="wide")
        st.header("🏦 FinGPT")
        st.subheader("Where finance meets AI")
        st.markdown("LLMs can hallucinate, this is not financial advice.")

        faq()
