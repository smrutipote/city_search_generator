import os
from langchain.llms import OpenAI
from langchain_community.llms import OpenAI
from langchain_openai import OpenAI
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain.prompts import PromptTemplate
os.environ['OPENAI_API_KEY'] = 'sk-'


def country_call(country):
    llm = OpenAI(temperature=0.2)
    prompt_country = PromptTemplate(
        input_variables=['country'],
        template='name a city inside {country} to visit for honeymoon'
    )

    city_chain = LLMChain(llm=llm, prompt=prompt_country, output_key='city')

    prompt_city = PromptTemplate(
        input_variables=['city'],
        template='name one place inside {city} for a romantic dinner date'
    )

    place_chain = LLMChain(llm=llm, prompt=prompt_city, output_key='place')

    cityplace = SequentialChain(chains=[city_chain, place_chain], input_variables=['country'], output_variables=['city', 'place'])

    result = cityplace({'country': country})
    return result
