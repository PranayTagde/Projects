import streamlit as st
from dotenv import load_dotenv
import os
#import pandas as pd
from langchain.llms import OpenAI
from langchain_experimental.agents import create_csv_agent


load_dotenv()

if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
    print("OPENAI_API_KEY is not set")
    exit(1)
else:
    print("OPENAI_API_KEY is set")

st.set_page_config(layout='wide')
st.title("ChatCSV powered by STREAMLIT")
input_csv = st.file_uploader("Upload your csv file", type=['csv'])

if input_csv is not None:
    
    #data = pd.read_csv(input_csv)
    #st.write(data.head(6))

    agent = create_csv_agent(OpenAI(temperature=0), input_csv, verbose=True)

    prompt = st.text_area("Enter your Query in prompt:")

    if st.button("Generate"):
        if prompt:
            with st.spinner("Generating Response..."):
                st.write(agent.run(prompt))
        else:
            st.warning("Please Enter Query in prompt.")