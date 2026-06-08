import streamlit as st
import google.generativeai as genai
genai.configure(api_key="")
model=genai.GenerativeModel("gemini-2.5-flash")
st.title("Chatbot")
prompt =st.text_input("Enter a Questions",)
if st.button("submit"):
    res=model.generate_content(prompt+"Your are a blog except so give the output in the following manner: give the subtopic , content in simple words, use the relavent tone control for the topic")
    st.write(res.text)
