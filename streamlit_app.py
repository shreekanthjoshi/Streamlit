
import streamlit as st
from langchain.llms import OpenAI
from streamlit_chat import chat

@st.cache(allow_output_mutation=True)
def get_chat():
    return chat()

st.title('🦜🔗 Quickstart App')

openai_api_key = st.sidebar.text_input('OpenAI API Key')

def generate_response(input_text):
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  st.info(llm(input_text))
  
col1, col2, col3 = st.columns([4,2,1])
with col1:
    chat = get_chat()
    chat.add_message("Hello, how can I help you today?", "bot")
    
with col2:
  with st.form('my_form'):
    text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
    submitted = st.form_submit_button('Submit')
    if not openai_api_key.startswith('sk-'):
      st.warning('Please enter your OpenAI API key!', icon='⚠')
    if submitted and openai_api_key.startswith('sk-'):
      generate_response(text)
