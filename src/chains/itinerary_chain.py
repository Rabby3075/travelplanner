from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from src.config.config import GROQ_API_KEY

#initializing llm model
llm = ChatGroq(api_key=GROQ_API_KEY, model="llama-3.1-8b-instant")
iterary_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful travel asssistant. Create a day trip itineary for {city} based on user's interest : {interests}. Provide a brief , bulleted itineary"),

    ("human", "Create a itineary for my day trip")
])

def generate_itinerary(city:str, interests:list[str])->str:
    response = llm.invoke(
        iterary_prompt.format_messages(city=city, interests=", ".join(interests))
    )
    return response.content