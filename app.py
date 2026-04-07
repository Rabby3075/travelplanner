import streamlit as st
from src.core.planner import TravelPlanner
from dotenv import load_dotenv


st.set_page_config(page_title="Travel Planner", page_icon=":earth_americas:",layout="centered")
st.title("AI Travel Itinerary Planner")
st.write("Plan your day trip itinerary by entering your city and your interest.")

load_dotenv()
with st.form("travel_form"):
    city = st.text_input("Enter the city you want to visit")
    interests = st.text_input("Enter your interests (comma separated)")
    submit_button = st.form_submit_button(label="Generate Itinerary")
if submit_button:
    if city and interests:
        planner = TravelPlanner()
        planner.set_city(city)
        planner.set_interests(interests)
        itinerary = planner.create_itinerary()
        st.subheader("Your Day Trip Itinerary")
        st.write(itinerary)
    else:
        st.error("Please enter both city and interests to generate the itinerary.")