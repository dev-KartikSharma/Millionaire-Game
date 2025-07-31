import streamlit as st
import random

st.set_page_config(
    page_title="Millionaire_Game",
    page_icon="🪙",
    layout="centered"
)

questions = [

    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Venus", "Mars", "Jupiter"],
        "answer_index": 2
    },
    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "options": ["Charles Dickens", "William Shakespeare", "George Orwell", "Leo Tolstoy"],
        "answer_index": 1
    },
    {
        "question": "What is the chemical symbol for Gold?",
        "options": ["Au", "Ag", "Pb", "Fe"],
        "answer_index": 0
    },
    {
        "question": "Which country hosted the 2016 Summer Olympics?",
        "options": ["Brazil", "China", "UK", "Russia"],
        "answer_index": 0
    },
    {
        "question": "What is the capital of Canada?",
        "options": ["Toronto", "Vancouver", "Ottawa", "Montreal"],
        "answer_index": 2
    },
    {
        "question": "Which language is the most widely spoken in the world?",
        "options": ["English", "Mandarin Chinese", "Spanish", "Hindi"],
        "answer_index": 1
    },
    {
        "question": "What is the hardest natural substance on Earth?",
        "options": ["Iron", "Diamond", "Quartz", "Obsidian"],
        "answer_index": 1
    },
    {
        "question": "In computing, what does CPU stand for?",
        "options": ["Central Processing Unit", "Computer Power Unit", "Control Processing Utility", "Computer Performance Unit"],
        "answer_index": 0
    },
    {
        "question": "How many bones are there in the human body?",
        "options": ["206", "201", "210", "196"],
        "answer_index": 0
    },
    {
        "question": "Who is the founder of SpaceX?",
        "options": ["Steve Jobs", "Elon Musk", "Jeff Bezos", "Mark Zuckerberg"],
        "answer_index": 1
    },
    {
        "question": "Which country invented tea?",
        "options": ["India", "China", "England", "Japan"],
        "answer_index": 1
    },
    {
        "question": "What gas do plants absorb from the atmosphere?",
        "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"],
        "answer_index": 2
    },
    {
        "question": "Which film won Best Picture at the 2020 Oscars?",
        "options": ["Parasite", "Joker", "1917", "Ford v Ferrari"],
        "answer_index": 0
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Arctic Ocean"],
        "answer_index": 2
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "options": ["Osmium", "Oxygen", "Oganesson", "Oxide"],
        "answer_index": 1
    },
    {
        "question": "What is the capital city of Australia?",
        "options": ["Sydney", "Melbourne", "Canberra", "Brisbane"],
        "answer_index": 2
    },
    {
        "question": "Which instrument has keys, pedals, and strings?",
        "options": ["Violin", "Piano", "Flute", "Guitar"],
        "answer_index": 1
    },
    {
        "question": "Which part of the plant conducts photosynthesis?",
        "options": ["Roots", "Stem", "Flowers", "Leaves"],
        "answer_index": 3
    },
    {
        "question": "What year did the Titanic sink?",
        "options": ["1912", "1905", "1920", "1898"],
        "answer_index": 0
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["Vincent van Gogh", "Leonardo da Vinci", "Michelangelo", "Pablo Picasso"],
        "answer_index": 1
    },
    {
        "question": "Which country gifted the Statue of Liberty to the USA?",
        "options": ["Germany", "Canada", "France", "England"],
        "answer_index": 2
    },
    {
        "question": "Which gas is most abundant in Earth's atmosphere?",
        "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
        "answer_index": 2
    },
    {
        "question": "What’s the smallest prime number?",
        "options": ["1", "2", "3", "0"],
        "answer_index": 1
    },
    {
        "question": "Which company developed the Windows operating system?",
        "options": ["Apple", "Google", "Microsoft", "IBM"],
        "answer_index": 2
    },
    {
        "question": "How many players are there in a football (soccer) team?",
        "options": ["9", "10", "11", "12"],
        "answer_index": 2
    }
]

if "q_index" not in st.session_state:
    st.session_state.q_index = 0
if "score" not in st.session_state:
    st.session_state.score = 0

st.title("💸 Who Wants to Be a Millionaire")
current_q = questions[st.session_state.q_index]

# st.button("Start")
# st.write(