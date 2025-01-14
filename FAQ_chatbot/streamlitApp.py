import streamlit as st
from faq_chatbot import FAQChatbot

# Initialize the chatbot
chatbot = FAQChatbot('university_faq.csv')

# Streamlit app
st.title("FAQ Chatbot")
st.write("Ask me anything related to the product!")

# User input
user_input = st.text_input("Enter your question:")

# Button to process the input
if st.button("Submit"):
    if user_input.strip() == "":
        st.warning("Please enter a question.")
    else:
        response = chatbot.find_best_match(user_input)
        st.write("**Matched Question:**", response['matched_question'])
        st.write("**Confidence Score:**", round(response['confidence'], 2))
        st.write("**Answer:**", response['answer'])
