from langchain.output_parsers import PydanticOutputParser
from src.models.question_schemas import MCQQuestion, FillInTheBlankQuestion
from src.prompts.templates import mcq_prompt_template, fill_blank_prompt_template
from src.llm.groq_client import get_groq_llm
from src.config.settings import settings
from src.common.logger import get_logger
from src.common.custom_exception import CustomException


class QuestionGenerator:
    def __init__(self):
        self.llm = get_groq_llm()
        self.logger = get_logger(self.__class__.__name__)
           
    def _retry_and_parse(self, prompt,parser, topic, difficulty):
        for attempt in range(settings.MAX_RETRIES):
            try:
                self.logger.info(f"Generating question for topic '{topic}' with difficulty '{difficulty}'")
                
                response = self.llm.invoke(prompt.format(topic=topic, difficulty=difficulty))
                
                parsed = parser.parse(response.content)
                
                self.logger.info(f"Successfully parsed the question")
            
            except Exception as e:
                self.logger.error(f"Error Coming : {str(e)}")
                if attempt == settings.MAX_RETRIES - 1:
                    raise CustomException(f"Generation failed after {settings.MAX_RETRIES} attempts: {str(e)}")
    
    def generate_mcq(self, topic: str, difficulty: str= 'medium') -> MCQQuestion:
        try:
            parser = PydanticOutputParser(pydantic_object=MCQQuestion)
            
            question = self._retry_and_parse(mcq_prompt_template, parser, topic, difficulty)

            if len(question.options) != 4 or question.correct_answer not in question.options:
                raise ValueError("Generated MCQ does not have exactly 4 options or the correct answer is not among them.")
            self.logger.info(f"Generated a valid MCQ Question")
            return question
        except Exception as e:
            self.logger.error(f"Failed to generate MCQ: {str(e)}")
            raise CustomException(f"Failed to generate MCQ: {str(e)}")
    
    def generate_fill_in_the_blank(self, topic: str, difficulty: str = 'medium') -> FillInTheBlankQuestion:
        try:
            parser = PydanticOutputParser(pydantic_object=FillInTheBlankQuestion)
            
            question = self._retry_and_parse(fill_blank_prompt_template, parser, topic, difficulty)

            if not question.answer or not question.question:
                raise ValueError("Generated fill-in-the-blank question is invalid.")
            self.logger.info(f"Generated a valid Fill-in-the-Blank Question")
            return question
        except Exception as e:
            self.logger.error(f"Failed to generate Fill-in-the-Blank Question: {str(e)}")
            raise CustomException(f"Failed to generate Fill-in-the-Blank Question: {str(e)}")