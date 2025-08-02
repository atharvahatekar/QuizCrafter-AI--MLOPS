import os
import streamlit as st
import pandas as pd
from src.generator.question_generator import QuestionGenerator


def rerun():
    st.session_state['rerun_trigger'] = not st.session_state.get('rerun_trigger',False)


class QuizManager:
    def __init__(self):
        self.questions=[]
        self.user_answers=[]
        self.results=[]

    def generate_questions(self, generator:QuestionGenerator , topic:str , question_type:str , difficulty:str , num_questions:int):
        self.questions=[]
        self.user_answers=[]
        self.results=[]

        try:
            for _ in range(num_questions):
                if question_type == "Multiple Choice":
                    question = generator.generate_mcq(topic,difficulty.lower())

                    self.questions.append({
                        'type' : 'MCQ',
                        'question' : question.question,
                        'options' : question.options,
                        'correct_answer': question.correct_answer
                    })

                else:
                    question = generator.generate_fill_blank(topic,difficulty.lower())

                    self.questions.append({
                        'type' : 'Fill in the blank',
                        'question' : question.question,
                        'correct_answer': question.answer
                    })
        except Exception as e:
            st.error(f"Error generating question {e}")
            return False
        
        return True
    

    def attempt_quiz(self):
        # Clear previous answers when attempting the quiz again
        self.user_answers = [None] * len(self.questions)
        
        for i,q in enumerate(self.questions):
            st.markdown(f"**Question {i+1} : {q['question']}**")

            if q['type']=='MCQ':
                selected_option = st.radio(
                    f"Select and answer for Question {i+1}",
                    q['options'],
                    index=0,
                    key=f"mcq_{i}"
                )
                
                # Store the user's selected option at the specific index
                self.user_answers[i] = selected_option

            else:
                user_answer = st.text_input(
                    f"Fill in the blank for Question {i+1}",
                    key = f"fill_blank_{i}"
                )
                
                # Store the user's answer at the specific index
                self.user_answers[i] = user_answer

    def evaluate_quiz(self):
        self.results=[]

        for i, (q,user_ans) in enumerate(zip(self.questions,self.user_answers)):
            # Skip questions that weren't answered
            if user_ans is None:
                user_ans = ""
                
            result_dict = {
                'question_number' : i+1,
                'question': q['question'],
                'question_type' :q["type"],
                'user_answer' : user_ans,
                'correct_answer' : q["correct_answer"],
                "is_correct" : False
            }

            if q['type'] == 'MCQ':
                result_dict['options'] = q['options']
                # Exact string comparison for MCQ
                result_dict["is_correct"] = user_ans == q["correct_answer"]

            else:
                result_dict['options'] = []
                # Case-insensitive comparison for fill-in-the-blank questions
                result_dict["is_correct"] = user_ans.strip().lower() == q['correct_answer'].strip().lower()

            self.results.append(result_dict)

    def generate_result_dataframe(self):
        if not self.results:
            return pd.DataFrame()
        
        return pd.DataFrame(self.results)
    
    def save_to_csv(self, filename_prefix="quiz_results"):
        if not self.results:
            st.warning("No results to save !!")
            return None
        
        df = self.generate_result_dataframe()


        from datetime import datetime
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        unique_filename = f"{filename_prefix}_{timestamp}.csv"

        os.makedirs('results' , exist_ok=True)
        full_path = os.path.join('results' , unique_filename)

        try:
            df.to_csv(full_path,index=False)
            st.success("Results saved sucesfully....")
            return full_path
        
        except Exception as e:
            st.error(f"Failed to save results {e}")
            return None
            
