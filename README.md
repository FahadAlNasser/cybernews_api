Terms:

AI = Artificical inteligence

LLMs = Large Language Models

FastAPI = it is a modern, high performance web framework for building APIs with Python

API = Application Programming Interface

ML = Machine Learning

Deepinfra = according to my search, I understand that Deepinfra act as a host to offer low cost ML models. 

LM Studo = is a software that allows you to run LLMs locally for testing and development

I have been continuing experimenting and learning about Python API, FastAPI. I searched about a few Artificial intelligence models. I discovered that each model's purpose and which AI API model is suitable for a specific Python program. What makes this complicated for learners is that the AI models' free version are all limited depending on tokens and limit rate. There is one free machine learner model. However, it is not completely accurate, such as transformers pipeline. There is also another free version called Ollama. However, you need a sufficient hardware resources. I experimented with OpenAI, DeepSeek, Gemini, Meta, and Mistral. For this code, I used Mistral, Meta, and Gemini. I noticed that Mistral and Meta like to explain things in detail where they do not follow the code structure lines. Gemini likes to be extremely brief, and sometimes the explanation does not make sense. Gemini will try to say only a word or incomplete sentence sometimes. Therefore, I tweaked my code to make both Mistral and Meta explain things briefly. As for Gemini, it remained the same. Furthermore, While I was searching for ways to experiment with AI models in a few Python programs, I eventurally discovered LM Studio which you can test code privately, but I will advice you to implement it carefully with FastAPI. The reason LM Studio runs locally and is not secured. So, you will be risking exposing your data. If you want to use LM Studio, please consider the packages and security methods that you will use. For this code, I struggled to understand FastAPI. For example, when I test my code a few times, I have exceeded my rate limit. Therefore, I needed to add a line to let me know that I exceeded my rate limit. Otherwise, it will make illogical errors about 'choice'(I removed that line of code). Despite this fact, I am satisfied with learning about FastAPI and implementing it with a few projects. I am starting to be familiar with FastAPI such as learning about how to properly include HTTP end point like @app.get, post, delete, put, or patch:

a) @app.get() is responsible for managing get requests
b) @app.post() is responsible for managing post requests
c) @app.delete() is responsible for managing delete requests
d) @app.patch() is responsible for managing patch requests
e) @app.put() is responsible for managing patch requests

In addition, my struggles are making mistakes within the code such as the habit to forget to include ":" or delete ")" by mistake. As well as the rate limit to experiment and learn about the difference with AI models. I did not use the LM Studio application for all my projects, so I had to create multiple accounts when needed to generate a key and start fresh because, and I will note that; not all AI models reset their limit such as Deepinfra.

### I would also like to note that when you write a proper sentence, the quality of AI-generated answers will improve.

### I have included screenshots on the documents/screenshots folder to show how the program response to error, questions, and answers.

### You can use http://127.0.0.1:8000/docs by inputting it in your browser, or you can use a free tool called Postman

### Disclaimer

I am learning, experimenting, and practicing with coding. I am exploring different tools, techniques, and programming languages to enhance my skills. This is code is experimental and intended for educational purposes only.
