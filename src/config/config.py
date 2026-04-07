import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY") # Load the API key from environment variable
