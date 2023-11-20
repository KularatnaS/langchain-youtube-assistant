import langchain_helper as lch
import streamlit as st
import textwrap

st.title("Youtube Assistant")

with st.sidebar:
    with st.form(key="my_form"):
        youtube_url = st.sidebar.text_area(
            label="Youtube URL:",
            max_chars=100
        )
        query = st.sidebar.text_area(
            label="Ask me about the video:",
            max_chars=100
        )

        openai_api_key = st.sidebar.text_area(
            label="OpenAI API Key:",
            max_chars=100
        )

        submit_button = st.form_submit_button(label="Submit")

if query and youtube_url and openai_api_key:
    response = lch.get_response_from_query(youtube_url, query, openai_api_key)
    st.subheader("Answer:")
    st.text(textwrap.fill(response, width=80))
