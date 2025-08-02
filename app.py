import os
import streamlit as st
from dotenv import load_dotenv
from src.utils.helpers import *
from src.generator.question_generator import QuestionGenerator
import time
import random
try:
    import matplotlib.pyplot as plt
    import numpy as np
    matplotlib_available = True
except ImportError:
    matplotlib_available = False
load_dotenv()

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

def main():
    st.set_page_config(
        page_title="Quiz Crafter AI", 
        page_icon="🎓",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'About': "Quiz Crafter AI - An intelligent quiz generation tool"
        }
    )
    # Set dark theme
    st.markdown("""
        <script>
            var elements = window.parent.document.querySelectorAll('.stApp');
            elements[0].style.backgroundColor = '#121212';
        </script>
    """, unsafe_allow_html=True)
    
    load_css()

    if 'quiz_manager' not in st.session_state:
        st.session_state.quiz_manager = QuizManager()

    if 'quiz_generated' not in st.session_state:
        st.session_state.quiz_generated = False

    if 'quiz_submitted' not in st.session_state:
        st.session_state.quiz_submitted = False

    if 'rerun_trigger' not in st.session_state:
        st.session_state.rerun_trigger = False
    
    emojis = ["🧠", "📚", "💡", "🔍", "🎯", "🏆"]
        
    st.markdown(f"<h1 class='main-header'>Quiz Crafter AI {random.choice(emojis)}</h1>", unsafe_allow_html=True)

    st.sidebar.markdown("<h2 style='text-align: center; color: #90CAF9;'>⚙️ Quiz Settings</h2>", unsafe_allow_html=True)
    
    with st.sidebar.container():
        st.markdown("<div class='sidebar-content'>", unsafe_allow_html=True)
        
        st.markdown("#### 📋 Question Format")
        question_type = st.selectbox(
            "Select the type of questions you want",
            ["Multiple Choice", "True/False", "Fill in the Blank"],
            index=0,
            help="Choose the format of questions for your quiz"
        )
        
        st.markdown("#### 🔍 Quiz Topic")
        topic = st.text_input(
            "Enter Topic",
            placeholder="E.g., World History, Quantum Physics, Python Programming",
            help="Be specific for more focused questions"
        )
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 🎚️ Difficulty")
            difficulty = st.selectbox(
                "Choose level",
                ["Easy", "Medium", "Hard"],
                index=1,
                help="Select based on your expertise level"
            )
        
        with col2:
            st.markdown("#### 🔢 Questions")
            num_questions = st.number_input(
                "How many?",
                min_value=1, 
                max_value=10,
                value=5,
                help="1-20 questions allowed"
            )
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        generate_button = st.button(
            "🚀 Generate Quiz", 
            use_container_width=True,
            help="Click to create your custom quiz!"
        )
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Quiz tips in the sidebar
        st.markdown("<br>", unsafe_allow_html=True)
        with st.expander("💡 Quiz Tips"):
            st.markdown("""
                - Be specific with your topic for better questions
                - Try different question types for variety
                - Save your results to track your progress
                - Challenge yourself with harder difficulties
            """)
    
    if generate_button:
        st.session_state.quiz_submitted = False

        with st.spinner("🧠 Generating your personalized quiz questions..."):
            generator = QuestionGenerator()
            success = st.session_state.quiz_manager.generate_questions(
                generator,
                topic, question_type, difficulty, num_questions
            )
        
        if success:
            st.toast("✅ Quiz generated successfully!", icon="🎉")
        else:
            st.toast("❌ Failed to generate quiz. Please try again.", icon="⚠️")
            
        st.session_state.quiz_generated = success
        rerun()

    if st.session_state.quiz_generated and st.session_state.quiz_manager.questions:
        st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
        st.markdown("<h2 class='sub-header'>📝 Your Quiz</h2>", unsafe_allow_html=True)
        
        # Progress tracker
        col1, col2, col3 = st.columns([2, 3, 2])
        with col2:
            total_q = len(st.session_state.quiz_manager.questions)
            st.progress(1.0, f"Question Progress: {total_q}/{total_q}")
        
        # Quiz container
        with st.container():
            st.session_state.quiz_manager.attempt_quiz()
            
            st.markdown("<br>", unsafe_allow_html=True)
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                submit_button = st.button(
                    "📤 Submit Quiz", 
                    use_container_width=True,
                    help="Click to check your answers"
                )
            
            if submit_button:
                with st.spinner("🔍 Evaluating your answers..."):
                    time.sleep(1)  # Small delay for better UX
                    st.session_state.quiz_manager.evaluate_quiz()
                    st.session_state.quiz_submitted = True
                    rerun()

    if st.session_state.quiz_submitted:
        st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
        st.markdown("<h2 class='sub-header'>🏁 Quiz Results</h2>", unsafe_allow_html=True)
        
        results_df = st.session_state.quiz_manager.generate_result_dataframe()

        if not results_df.empty:
            correct_count = results_df["is_correct"].sum()
            total_questions = len(results_df)
            score_percentage = round((correct_count/total_questions)*100, 1)
            
            # Determine score class and message based on percentage
            if score_percentage >= 80:
                score_class = "high-score"
                message = "🏆 Excellent work!"
            elif score_percentage >= 60:
                score_class = "medium-score"
                message = "👍 Good job!"
            else:
                score_class = "low-score"
                message = "💪 Keep practicing!"
                
            # Display score with visual styling
            st.markdown(f"""
                <div class='score-display {score_class}'>
                    {message}<br>
                    Your Score: {score_percentage}%<br>
                    ({correct_count} out of {total_questions} correct)
                </div>
            """, unsafe_allow_html=True)
            
            # Add a summary chart
            col1, col2 = st.columns([2, 3])
            with col1:
                st.markdown("### Question Summary")
                st.markdown(f"""
                - ✅ **Correct**: {correct_count}
                - ❌ **Incorrect**: {total_questions - correct_count}
                - 📊 **Success rate**: {score_percentage}%
                """)
            
            with col2:
                # Simple chart visualization using Streamlit's native charts if matplotlib is not available
                if matplotlib_available:
                    fig, ax = plt.subplots(figsize=(2, 2), facecolor='#121212')
                    labels = ['Correct', 'Incorrect']
                    sizes = [correct_count, total_questions - correct_count]
                    colors = ['#66BB6A', '#EF5350']
                    explode = (0.1, 0)
                    
                    ax.pie(sizes, explode=explode, labels=labels, colors=colors,
                          autopct='%1.1f%%', shadow=True, startangle=90, 
                          textprops={'color': 'white'})
                    ax.axis('equal')
                    fig.patch.set_alpha(0.0)
                    st.pyplot(fig)
                else:
                    # Fallback to Streamlit charts if matplotlib is not available
                    chart_data = {
                        'Category': ['Correct', 'Incorrect'],
                        'Value': [correct_count, total_questions - correct_count]
                    }
                    st.bar_chart(
                        data=chart_data, 
                        x='Category',
                        y='Value',
                        color=['#66BB6A', '#EF5350']
                    )
            
            # Detailed results for each question
            st.markdown("### Detailed Breakdown")
            for _, result in results_df.iterrows():
                question_num = result['question_number']
                
                with st.container():
                    st.markdown(f"<div class='question-card'>", unsafe_allow_html=True)
                    
                    # Question header with result icon
                    if result['is_correct']:
                        st.markdown(f"<h3 style='color:#66BB6A'>✅ Question {question_num}</h3>", unsafe_allow_html=True)
                    else:
                        st.markdown(f"<h3 style='color:#EF5350'>❌ Question {question_num}</h3>", unsafe_allow_html=True)
                    
                    # Question text
                    st.markdown(f"<p style='font-size: 1.1rem; color:#E0E0E0;'>{result['question']}</p>", unsafe_allow_html=True)
                    
                    # Answer details
                    if not result['is_correct']:
                        st.markdown(f"<p style='color:#EF5350'><b>Your answer:</b> {result['user_answer']}</p>", unsafe_allow_html=True)
                        
                    st.markdown(f"<p style='color:#66BB6A'><b>Correct answer:</b> {result['correct_answer']}</p>", unsafe_allow_html=True)
                    
                    # Display explanation for questions if available
                    if 'explanation' in result and result['explanation']:
                        st.info(f"💡 **Explanation:** {result['explanation']}")
                    
                    st.markdown("</div>", unsafe_allow_html=True)
            
            # Actions section
            col1, col2 = st.columns(2)
            with col1:
                if st.button("💾 Save Results", use_container_width=True):
                    with st.spinner("Saving your results..."):
                        saved_file = st.session_state.quiz_manager.save_to_csv()
                        if saved_file:
                            with open(saved_file,'rb') as f:
                                st.download_button(
                                    label="📥 Download Results",
                                    data=f.read(),
                                    file_name=os.path.basename(saved_file),
                                    mime='text/csv',
                                    use_container_width=True
                                )
                        else:
                            st.warning("⚠️ No results available to save")
            
            with col2:
                if st.button("🔄 Create New Quiz", use_container_width=True):
                    st.session_state.quiz_generated = False
                    st.session_state.quiz_submitted = False
                    rerun()
    
    # Add footer with information and help
    if not st.session_state.quiz_generated:
        st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
        
        # Tips and information cards
        st.markdown("<h3 class='sub-header'>📚 Learning Resources</h3>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div style="padding: 15px; border-radius: 10px; background-color: #01579B; height: 200px; border: 1px solid #0288D1;">
                <h4 style="color: #81D4FA;">🧠 How to Study Effectively</h4>
                <ul style="color: #E1F5FE;">
                    <li>Take regular quizzes to test your knowledge</li>
                    <li>Study in short, focused sessions</li>
                    <li>Teach concepts to others to solidify understanding</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
        with col2:
            st.markdown("""
            <div style="padding: 15px; border-radius: 10px; background-color: #1B5E20; height: 200px; border: 1px solid #388E3C;">
                <h4 style="color: #A5D6A7;">💡 Question Types</h4>
                <ul style="color: #E8F5E9;">
                    <li><b>Multiple Choice</b>: Test recognition and differentiation</li>
                    <li><b>True/False</b>: Quick assessment of factual knowledge</li>
                    <li><b>Fill in the Blank</b>: Test recall and terminology</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
        with col3:
            st.markdown("""
            <div style="padding: 15px; border-radius: 10px; background-color: #BF360C; height: 200px; border: 1px solid #E64A19;">
                <h4 style="color: #FFCCBC;">🔍 Quiz Topic Ideas</h4>
                <ul style="color: #FFF3E0;">
                    <li>Historical events and figures</li>
                    <li>Scientific concepts and discoveries</li>
                    <li>Programming languages and frameworks</li>
                    <li>Geography, arts, and literature</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

    # Add footer
    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    st.markdown("""
        <div style="text-align: center; margin-top: 30px; padding: 20px; color: #90A4AE;">
            <p>Made with ❤️ By - <strong>Atharva Hatekar</strong> | © 2025</p>
        </div>
    """, unsafe_allow_html=True)

if __name__=="__main__":
    main()
