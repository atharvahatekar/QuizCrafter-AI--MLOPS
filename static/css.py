import streamlit as st
# Custom CSS to make the UI more attractive
def load_css():
    st.markdown("""
        <style>
        /* Dark Theme Base Styling */
        body {
            color: #E0E0E0;
        }
        .main-header {
            font-size: 3rem !important;
            color: #90CAF9;
            text-align: center;
            margin-bottom: 1rem;
            font-weight: 700;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        .sub-header {
            font-size: 1.8rem !important;
            color: #80DEEA;
            padding: 0.5rem;
            border-radius: 5px;
            margin: 1.5rem 0 1rem 0;
        }
        .question-card {
            background-color: #263238;
            padding: 1.5rem;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.3);
            margin-bottom: 1.5rem;
            border-left: 4px solid #42A5F5;
            border-right: 4px solid #42A5F5;
        }
        .results-card {
            padding: 1rem;
            border-radius: 8px;
            margin-bottom: 1rem;
            background-color: #1E1E1E;
        }
        .score-display {
            font-size: 2rem;
            text-align: center;
            padding: 1rem;
            margin: 1rem 0;
            border-radius: 10px;
            font-weight: bold;
        }
        .high-score {
            background-color: #1B5E20;
            color: #AEDCAE;
        }
        .medium-score {
            background-color: #E65100;
            color: #FFD180;
        }
        .low-score {
            background-color: #B71C1C;
            color: #FFCDD2;
        }
        .stButton>button {
            background-color: #42A5F5;
            color: white;
            border: none;
            padding: 0.5rem 1rem;
            border-radius: 5px;
            font-weight: bold;
            transition: all 0.3s;
        }
        .stButton>button:hover {
            background-color: #1976D2;
            box-shadow: 0 4px 8px rgba(0,0,0,0.4);
        }
        .sidebar-content {
            padding: 1rem;
            background-color: #263238;
            border-radius: 10px;
            border: 1px solid #37474F;
        }
        .emoji-icon {
            font-size: 2rem;
            margin-right: 0.5rem;
        }
        .divider {
            height: 3px;
            background-image: linear-gradient(to right, #42A5F5, #7E57C2, #42A5F5);
            margin: 1rem 0;
            border-radius: 2px;
        }
        /* Override Streamlit's default white backgrounds */
        .stApp {
            background-color: #121212;
        }
        div[data-testid="stVerticalBlock"] {
            background-color: transparent;
        }
        div[data-testid="stHorizontalBlock"] {
            background-color: transparent;
        }
        .stTextInput>div>div>input {
            background-color: #263238;
            color: #E0E0E0;
            border-color: #455A64;
        }
        .stSelectbox>div>div>div {
            background-color: #263238;
            color: #E0E0E0;
        }
        .stNumberInput>div>div>input {
            background-color: #263238;
            color: #E0E0E0;
        }
        /* Make text more readable on dark background */
        p, li, h1, h2, h3, h4 {
            color: #E0E0E0;
        }
        .stMarkdown {
            color: #E0E0E0;
        }
        /* Dark-themed info/success/error boxes */
        .element-container .stAlert {
            background-color: #263238;
            color: #E0E0E0;
        }
        </style>
    """, unsafe_allow_html=True)