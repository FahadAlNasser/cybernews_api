from fastapi import FastAPI, Query
from app.services import clients_ai, scraping_article
from app.models import QuestionAsked

app = FastAPI()

# Articles in a dictionary method to IDs cybersecurity news websites. 
# You can experiment by including different articles or change the method as needed.
Articles = {
    "1": "https://thehackernews.com/",
    "2": "https://cybersecuritynews.com/",
    "3": "https://www.bleepingcomputer.com/"
}

# These are fastapi endpoint functions. 
# It uses Mistral AI to answer a question relying on a content within the chosen article source.
@app.get("/questioning-mistral-article")
def questioning_mistral_article(TheCompany: str = Query(...), TheQuestion: str = Query(...)):
    if TheCompany not in Articles:
        return {"error": "This is invalid article source. Please choose from: 1, 2, or 3"}
    url = Articles[TheCompany]
    articles_text = scraping_article.fetching_text_article(url)
    ans = clients_ai.questioning_mistral(TheQuestion, articles_text)
    return {"Model": "Mistral", "Source": TheCompany, "Question": TheQuestion, "Answer": ans}


@app.get("/questioning-meta-article")
def questioning_meta_article(TheCompany: str = Query(...), TheQuestion: str = Query(...)):
    if TheCompany not in Articles:
        return {"error": "This is invalid article source. Please choose from: 1, 2, or 3"}
    url = Articles[TheCompany]
    articles_text = scraping_article.fetching_text_article(url)
    ans = clients_ai.questioning_meta(TheQuestion, articles_text)
    return {"Model": "Meta", "Source": TheCompany, "Question": TheQuestion, "Answer": ans}

@app.get("/questioning-gemini-article")
def questioning_gemini_article(TheCompany: str = Query(...), TheQuestion: str = Query(...)):
    if TheCompany not in Articles:
        return {"error": "This is invalid article source. Please choose from: 1, 2, or 3"}
    url = Articles[TheCompany]
    articles_text = scraping_article.fetching_text_article(url)
    ans = clients_ai.questioning_gemini(TheQuestion, articles_text)
    return {"Model": "Gemini", "Source": TheCompany, "Question": TheQuestion, "Answer": ans}

