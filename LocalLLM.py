from langchain_ollama import ChatOllama
from Prompts import Prompts

llm = ChatOllama(
    model="llama3.2",
    temperature=0.6,        
)


messages = [
    ("system", "You are a helpful translator. Translate the user sentence to marathi."),
    ("human", "I love programming."),
]

ai_msg = llm.invoke(messages)
print(ai_msg.content)

Text="My name is Piyush Prafulla Kulkarni. I like using python and flask for backend"
Prompt=Prompts(Text=Text)

ai_msg = llm.invoke(Prompt.Personal_Identifiers_Remover())
print(ai_msg.content)