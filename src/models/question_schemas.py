from typing import List
from pydantic import BaseModel,Field,validator

class MCQQuestion(BaseModel):

    question: str = Field(description="The question text")

    options: List[str] = Field(description="List of 4 options")

    correct_answer: str = Field(description="The correct answer from the options")

    explanation: str = Field(description="Brief explanation of why the option is correct")

    @validator('question' , pre=True)
    def clean_question(cls,v):
        if isinstance(v,dict):
            return v.get('description' , str(v))
        return str(v)
    

class FillBlankQuestion(BaseModel):

    question: str = Field(description="The question text with '___' for the blank")

    answer : str = Field(description="The correct word or phrase for the blank")

    explanation: str = Field(description="Brief explanation of why the answer is correct")

    @validator('question' , pre=True)
    def clean_question(cls,v):
        if isinstance(v,dict):
            return v.get('description' , str(v))
        return str(v)
        
        
class TrueFalseQuestion(BaseModel):

    question: str = Field(description="The statement to be judged as true or false")

    correct_answer: bool = Field(description="Whether the statement is true (True) or false (False)")
    
    explanation: str = Field(description="Brief explanation of why the statement is true or false")

    @validator('question' , pre=True)
    def clean_question(cls,v):
        if isinstance(v,dict):
            return v.get('description' , str(v))
        return str(v)
