import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
import prompts
st.title("🦜🔗 Prompt Writer")

openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")


def generate_prompt(topic):
    # Instantiate LLM model
    llm = OpenAI(model_name="text-davinci-003", openai_api_key=openai_api_key, max_tokens=1024)
    # Prompt
    template = prompts.prompt_guide
    prompt = PromptTemplate(input_variables=["topic"], template=template)
    prompt_query = prompt.format(topic=topic)
    # Run LLM model
    response = llm(prompt_query)
    # Print results
    return st.info(response)


with st.form("myform"):
    topic_text = st.text_input("Enter prompt:", "")
    submitted = st.form_submit_button("Submit")
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
    elif submitted:
        generate_prompt(topic_text)