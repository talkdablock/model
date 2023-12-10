#!/usr/bin/env python

from dotenv import load_dotenv

from typing import List

from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import BaseOutputParser

from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from langserve import add_routes


origins = [
    # "http://localhost",
    "http://localhost:3001",
    "https://tdb-backend.up.railway.app"
]


class CSVOutputParser(BaseOutputParser[List[str]]):
    def parse(self, text: str) -> List[str]:
        print(text)
        return text.strip().split(", ")


load_dotenv()  # take environment variables from .env.
template = """You are a helpful assistant who generates comma separated lists.
A user will pass in an ethereum address, and you should analyze the spending behaviour of the provided address from data sources such as the etherscan.io, and make a guess of the character of the wallet owner in a comma separated list in the fashion a fortune teller.
ONLY return a comma separated list, and nothing more."""
human_template = "{address}"

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", template),
    ("human", human_template),
])

category_chain = chat_prompt | ChatOpenAI() | CSVOutputParser()

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )
]

app = FastAPI(
    title="LangChain Server",
    version="v0.0.1",
    description="APIs to query the ethereum blockchain on-chain data",
    middleware=middleware
)

add_routes(
    app,
    category_chain,
    path="/ethereum",
)

# if __name__ == '__main__':
#     import uvicorn
#     uvicorn.run(app, host="localhost", port=8080)
