import streamlit as st
import random
import json

with open("questions.json", "r") as f:
    questions = json.load(f)

st.set_page_config(
    page_title="Millionaire Game",
    page_icon="🪙",
    layout="centered"
)

@st.fragment
def quiz_fragment():
    st.title("Kaun Banega Carodpati")
    st.caption("(Amitabch bachan ko toh Rekha ka pati bnna tha 😔)")

    # Init state
    if "score" not in st.session_state:
        st.session_state.score = 0
    if "current_index" not in st.session_state:
        st.session_state.current_index = random.randint(0, len(questions) - 1)
    if "answered" not in st.session_state:
        st.session_state.answered = False
    if "feedback" not in st.session_state:
        st.session_state.feedback = ""
    
    # loading questions and options
    current_question = questions[st.session_state.current_index]
    question = current_question["question"]
    options = current_question["options"]
    correct = current_question["options"][current_question["answer_index"]]

    # Score 
    st.markdown(
        f"<div style='text-align: right; font-size: 18px;'>💯 Score: {st.session_state.score}</div>",
        unsafe_allow_html=True
    )

    # Display question
    st.markdown(f"<div style='font-size: 20px; font-weight: bold;'>Question : </div>", unsafe_allow_html=True)
    st.code(question)

    # Options
    selected_option = st.radio("Choose an option : ", options, key="selected_option")

    # columns
    col1, col2 = st.columns([3, 1])
    with col1:
        if st.button("Submit Answer", use_container_width=True, disabled=st.session_state.answered):
            if selected_option == correct:
                st.session_state.score += 1
                st.session_state.feedback = "🎉 Correct! You're one step closer to a million!"
                st.session_state.feedback_type = "success"
            else:
                st.session_state.feedback = f"❌ Wrong! Correct answer: **{correct}**"
                st.session_state.feedback_type = "error"
            st.session_state.answered = True

    with col2:
        if st.button("➡️ Next question", use_container_width=True):
            st.session_state.current_index = random.randint(0, len(questions) - 1)
            current_question = questions[st.session_state.current_index]
            st.session_state.answered = False
            st.session_state.feedback = ""
            st.session_state.feedback_type = ""
            st.rerun()


    # Display feedback in full width
    if st.session_state.get("feedback"):
        if st.session_state.feedback_type == "success":
            st.success(st.session_state.feedback)
        elif st.session_state.feedback_type == "error":
            st.error(st.session_state.feedback)
    
quiz_fragment()
