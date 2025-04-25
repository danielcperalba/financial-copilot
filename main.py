import streamlit as st
from langchain_experimental.agents import create_csv_agent
from langchain.llms import OpenAI
from dotenv import load_dotenv
import os

def main():
    load_dotenv()

    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
        print("OPEN_AI_API_KEY is not set")
        exit(1)
    else:
        print("OPEN_AI_API_KEY is set")

    st.set_page_config(page_title="Ask your CSV")
    st.header("Ask your CSV")

    user_csv = st.file_uploader("Upload your CSV file", type=["csv"])

    if user_csv is not None:

        agent = create_csv_agent(
            OpenAI(temperature=0), user_csv, verbose=True)
        
        user_question = st.text_input("Ask a question about your CSV")

        if user_question is not None and user_question != "":
            with st.spinner(text="In progress..."):
                st.write(agent.run(user_question))
    
if __name__ == "__main__":
    main()