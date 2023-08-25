import os
import openai
from dotenv import load_dotenv
from pprint import pprint as print
load_dotenv()

openai.api_key = os.environ['API_KEY']


def life_details(name):
    response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                    "role": "system",
                    "content": "You are very knowlegeble ai that helps people on witing a detailed essay about the given person and give information like date of birth, early life, education, occupation, spouses, children and life achievements and you article follows all the good practices"
                    },
                    {
                        "role": "user",
                        "content": f"Write an artile about {name}"
                    }
                ]
                )
    return response["choices"][0]["message"]["content"]


def language_assistant(message):
    response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                    "role": "system",
                    "content": "You are very knowlegeble ai who have waste knowledge about Hindi languages as well as English and you work as a language translator to traslate from English to Hindi"
                    },
                    {
                        "role": "user",
                        "content": f" Translate the following message : {message}"
                    }
                ]
                )
    return response["choices"][0]["message"]["content"]


def weather_check(query):
    response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                    "role": "system",
                    "content": "You are very knowlegeble ai who knows about current weather and temperature of all significant cities around the world"
                    },
                    {
                        "role": "user",
                        "content": f"Tell me the weather of {query}"
                    }
                ]
                )
    return response["choices"][0]["message"]["content"]



name = "Abraham Lincoln"
resposne = life_details(name)

print(resposne)