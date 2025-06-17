from bs4 import BeautifulSoup
import requests

def fetching_text_article(url: str, max_chars = 4000) -> str:
    """
    Please fetch and parse article main content text from the provided URL.
    This is basic example scraping the first <p> tags text.
    Please customize each news site accordingly"""
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        paragraphs = soup.find_all("p")
        text = ""
        for pag in paragraphs:
            text += pag.get_text() + "\n"
            if len(text) > max_chars:
                break
        return text[:max_chars]
    except Exception as e:
        return f"There is an error in fetching article text: {e}"