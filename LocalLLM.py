from langchain_ollama import ChatOllama
from Prompts import Prompts

llm = ChatOllama(
    model="llama3.2",
    temperature=0.5,        
)


def Sensitive_Personal_Information_Remover(
    Text,
    Personal_Identity_status=False,
    Financial_Information_status=False,
    Health_Information_status=False,
    Employment_Information_status=False,
    Online_Account_Information_status=False,
    Demographic_Information_status=False
):
    # Create initial prompt with the input text
    Prompt = Prompts(Text=Text)
    
    Message = Text  # Original text as the starting point
    
    # Remove personal identifiers
    if Personal_Identity_status:
        Message = llm.invoke(Prompt.Personal_Identifiers_Remover()).content
        Prompt = Prompts(Text=Message)  # Update prompt with new message
    
    # Remove financial information
    if Financial_Information_status:
        Message = llm.invoke(Prompt.Financial_Information_Remover()).content
        Prompt = Prompts(Text=Message)  # Update prompt
    
    # Remove health information
    if Health_Information_status:
        Message = llm.invoke(Prompt.Health_Information_Remover()).content
        Prompt = Prompts(Text=Message)
    
    # Remove employment information
    if Employment_Information_status:
        Message = llm.invoke(Prompt.Employment_Information_Remover()).content
        Prompt = Prompts(Text=Message)
    
    # Remove online account information
    if Online_Account_Information_status:
        Message = llm.invoke(Prompt.Online_Account_Information_Remover()).content
        Prompt = Prompts(Text=Message)
    
    # Remove demographic information
    if Demographic_Information_status:
        Message = llm.invoke(Prompt.Demographic_Information_Remover()).content
        Prompt = Prompts(Text=Message)
    
    return Message


# Sample text for testing
Text = "My name is Piyush Prafulla Kulkarni. I like using python and flask for backend. my account no is 123456789"

# Call the function with financial information removal enabled
print(Sensitive_Personal_Information_Remover(Text=Text, Financial_Information_status=True))
