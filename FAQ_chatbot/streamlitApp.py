import streamlit as st
from faq_chatbot import FAQChatbot

# Initialize the chatbot
chatbot = FAQChatbot('university_faq.csv')

# Streamlit app
st.title("🤖 FAQs Chatbot")
st.write("Ask me anything related to this University 💬")

# Initialize session state
if 'conversation' not in st.session_state:
    st.session_state.conversation = []  
    st.session_state.proceed = True      

# previous conversation history with styled boxes
st.write("---") 
for idx, message in enumerate(st.session_state.conversation):
    if idx % 2 == 0:
        st.markdown(f"**👤 User:** {message}")
    else:
        st.markdown(f"**🤖 Bot:** {message}")

st.write("---")  

if st.session_state.proceed:
    with st.form(key="user_input_form"):
        user_input = st.text_input("Your Question:", placeholder="Type your question here and press Submit...")
        submit_button = st.form_submit_button(label="🚀 Submit")

    if submit_button and user_input.strip():
        try:
            response = chatbot.find_best_match(user_input)
            
            # user question and bot's response to the conversation
            st.session_state.conversation.append(user_input)
            st.session_state.conversation.append(response['answer'])
            
            # bot's answer
            st.success("Response received! Check above for the answer. ✅")
            
            # Clear input field for the next question
            st.experimental_rerun()
        except Exception as e:
            st.error(f"Something went wrong: {e}")
else:
    st.info("Thanks for chatting! You can restart the session below.")
    if st.button("🔄 Restart Chat"):
        st.session_state.conversation = []
        st.session_state.proceed = True
        st.experimental_rerun()
