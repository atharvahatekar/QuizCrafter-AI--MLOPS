from langchain.prompts import PromptTemplate

mcq_prompt_template = PromptTemplate(
    template=(
        "Generate the {difficulty} difficulty level multiple-choice unique and non-repetitive questions about {topic}.\n\n"
        "Return ONLY a JSON object with these exact fields:\n"
        "- 'question': A clear, specific question\n"
        "- 'options': An array of exactly 4 possible answers\n"
        "- 'correct_answer': One of the options that is the correct answer\n\n"
        "- 'explanation': A brief explanation of why the statement is true or false\n\n"
        "Example format:\n"
        '{{\n'
        '    "question": "What is the capital of France?",\n'
        '    "options": ["London", "Berlin", "Paris", "Madrid"],\n'
        '    "correct_answer": "Paris",\n'
        '    "explanation": "Paris is the capital city of France."\n'
        '}}\n\n'
        "Your response:"
    ),
    input_variables=["topic", "difficulty"]
)

fill_blank_prompt_template = PromptTemplate(
    template=(
        "Generate the {difficulty} difficulty level fill-in-the-blank unique and non-repetitive questions about {topic}.\n\n"
        "Return ONLY a JSON object with these exact fields:\n"
        "- 'question': A sentence with '_____' marking where the blank should be\n"
        "- 'answer': The correct word or phrase that belongs in the blank\n\n"
        "- 'explanation': A brief explanation of why the statement is true or false\n\n"
        "Example format:\n"
        '{{\n'
        '    "question": "The capital of France is _____.",\n'
        '    "answer": "Paris",\n'
        '    "explanation": "Paris is the capital city of France."\n'
        '}}\n\n'
        "Your response:"
    ),
    input_variables=["topic", "difficulty"]
)

true_false_prompt_template = PromptTemplate(
    template=(
        "Generate the {difficulty} difficulty level true/false unique and non-repetitive questions about {topic}.\n\n"
        "Return ONLY a JSON object with these exact fields:\n"
        "- 'question': A clear statement that is either true or false\n"
        "- 'correct_answer': A boolean value (true or false) indicating if the statement is correct\n"
        "- 'explanation': A brief explanation of why the statement is true or false\n\n"
        "Example format:\n"
        '{{\n'
        '    "question": "Paris is the capital of France.",\n'
        '    "correct_answer": true,\n'
        '    "explanation": "Paris is indeed the capital and largest city of France."\n'
        '}}\n\n'
        "Your response:"
    ),
    input_variables=["topic", "difficulty"]
)