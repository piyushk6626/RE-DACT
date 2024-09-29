from langchain_ollama import ChatOllama
from Prompts import Prompts2

llm = ChatOllama(
    model="llama3.2",
    temperature=0.3,        
)


def Sensitive_Personal_Information_Remover(
    Text,
    Personal_Idenitty_status=True,
    Financial_Information_status=False,
    Health_Information_status=False,
    Employment_Information_status=False,
    Online_Account_Information_status=False,
    Demographic_Information_status=False
    ):
    Prompt=Prompts2(Text=Text)
    
    Message=Text
    if Personal_Idenitty_status :
        Message=llm.invoke(Prompt.Personal_Identifiers_Remover()).content
        Prompt=Prompts2(Text=Message)
    print(Message) 
    print()   
    if Financial_Information_status :
        Message=llm.invoke(Prompt.Financial_Information_Remover()).content
        Prompt=Prompts2(Text=Message)
    
    return Message

Text="My name is Piyush Prafulla Kulkarni. I like using python and flask for backend. my account no is 123456789"


print(Sensitive_Personal_Information_Remover(Text=Text,Financial_Information_status=True))