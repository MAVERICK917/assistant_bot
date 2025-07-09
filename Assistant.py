import streamlit as st
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint ,HuggingFaceEmbeddings


from dotenv import load_dotenv


load_dotenv()
llm=HuggingFaceEndpoint(  
    repo_id="meta-llama/Llama-3.1-8B-Instruct",  
    task="text-generation"
)
model=ChatHuggingFace(llm=llm)  
# result=model.invoke("hello")

# print(result)
st.header(" Mero Assistant")
user_input=st.text_input("Enter your Prompt")



if st.button("Summarize"):
    result=model.invoke(user_input)
    st.write(result.content)

  

  


