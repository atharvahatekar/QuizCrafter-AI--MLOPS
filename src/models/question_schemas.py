from typing import List
from pydantic import BaseModel, Field, validator

class MCQQuestion(BaseModel):
    question: str = Field(description="The question text")
    options: List[str] = Field(description="List of 4 options")
    correct_answer: str = Field(description="The correct answer from the options")

    # Validate that if LLM provide response in Dict format, it should be converted to string
    @validator('question', pre=True)
    def clean_question(cls, v):
        if isinstance(v, str):
            return v.get('description', str(v))
        return str(v)

class FillInTheBlankQuestion(BaseModel):
    question: str = Field(description="The question text with '____' for the user to fill")
    correct_answer: str = Field(description="The correct word or phrase to fill in the blank")

    # Validate that if LLM provide response in Dict format, it should be converted to string
    @validator('question', pre=True)
    def clean_question(cls, v):
        if isinstance(v, str):
            return v.get('description', str(v))
        return str(v)
    