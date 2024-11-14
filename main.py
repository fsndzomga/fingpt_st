import streamlit as st
from dotenv import load_dotenv
from search.data import respond_to_user, search_query
from components.sidebar import sidebar
from components.chart import chart

load_dotenv()

sidebar()

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    with st.spinner("Thinking..."):
        query_data = search_query(prompt)
        symbol = query_data["symbol"]

    chart(symbol)

    with st.spinner("Let's analyze the data..."):
        response = respond_to_user(prompt)
        st.session_state.messages.append({"role": "assistant", "content": response})

    st.chat_message("assistant").write_stream(response)
