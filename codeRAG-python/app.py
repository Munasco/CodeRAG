# app.py
import streamlit as st
from retrieval import simple_search
from mistral_client import call_mistral

st.title("Slack Error Log Analyzer (Mock Data)")

user_query = st.text_input("Describe your error problem:")

if st.button("Analyze Error"):
    if user_query:
        search_results = simple_search(user_query)
        if search_results:
            prompt = f"User asked: {user_query}\n\n"
            prompt += "Relevant error logs:\n"
            for timestamp, message_text in search_results:
                prompt += f"- [{timestamp}] {message_text}\n"
            prompt += "\nBased on the above logs, provide a solution or suggestion."

            answer = call_mistral(prompt)
            st.subheader("Mistral Suggestion:")
            st.write(answer)
        else:
            st.write("No relevant error logs found. This error might be new.")
