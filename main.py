from langchain_experimental.agents import create_csv_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
import streamlit as st
import tempfile

def main():
    load_dotenv()

    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        print("OPENAI_API_KEY is not set")
        exit(1)
    else:
        print("OPENAI_API_KEY is set")

    llm = ChatOpenAI(
        openai_api_key=openai_api_key,
        model="gpt-4",
    )

    st.set_page_config(page_title="Ask your CSV")
    st.header("Ask your CSV")

    user_csv = st.file_uploader("Upload your CSV file", type=["csv"])

    if user_csv is not None:
        
        with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmp_file:
            tmp_file.write(user_csv.getvalue())
            tmp_file_path = tmp_file.name

        agent = create_csv_agent(
            llm, 
            tmp_file_path, 
            verbose=True,
            allow_dangerous_code=True,
        )
        
        user_question = st.text_input("Ask a question about your CSV")

        if user_question:
            with st.spinner(text="In progress..."):
                st.write(agent.run(user_question))
    
if __name__ == "__main__":
    main()