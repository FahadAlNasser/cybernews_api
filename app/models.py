from pydantic import BaseModel

# This file acts as a validation input data for the API endpoints
# The code will expect two fields from the user:
# 1- TheCompany: The mapped ID of the article source such as 1, 2, or 3.
# 2- TheQuestion: The user's question is supposedly to be related to the article content
class QuestionAsked(BaseModel):
    TheCompany: str
    TheQuestion: str