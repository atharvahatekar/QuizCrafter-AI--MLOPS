import os
import streamlit as st
from dotenv import load_dotenv
from src.utils.helpers import *
from src.generator.question_generator import QuestionGenerator
import time
import random
import matplotlib.pyplot as plt
import numpy as np
from static.css import load_css

load_dotenv()

def main():
    st.set_page_config(
        page_title="Quiz Crafter AI", 
        page_icon="🎓",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'About': "Quiz Crafter AI - An intelligent quiz generation tool"})
    
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
        st.markdown("#### 📚 Question Type")
        question_type = st.selectbox(
            "Select the type of questions you want",
            ["Multiple Choice", "True/False", "Fill in the Blank"],index=1)
        
        st.markdown("#### 🔍 Quiz Topic")
        topic = st.text_input(
            "Enter Topic",
            placeholder="E.G: World History, Geography, Python Programming")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 🎚️ Difficulty")
            difficulty = st.selectbox(
                "Choose level",
                ["Easy", "Medium", "Hard"],
                index=1)
        
        with col2:
            st.markdown("#### 🔢 Questions")
            num_questions = st.number_input(
                "How many?",
                min_value=1, 
                max_value=10,
                value=5)
        
        st.markdown("<br>", unsafe_allow_html=True)
        generate_button = st.button( "🚀 Generate Quiz", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
        

    
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
                - 📊 **Success rate**: {score_percentage}% """)

            with col2:

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

    # Add footer
    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    st.markdown("""
        <div style="text-align: center; margin-top: 30px; padding: 20px; color: #90A4AE;">
            <p>Made with ❤️ By - <strong>Atharva Hatekar</strong></p>
        </div>
    """, unsafe_allow_html=True)

if __name__=="__main__":
    main()
