from langchain_core.messages import HumanMessage, AIMessage
from src.chains.itinerary_chain import generate_itinerary
from src.utils.logger import get_logger
from src.utils.custom_exception import CustomException

logger = get_logger(__name__)
class TravelPlanner:
    def __init__(self):
        self.messages = []
        self.city = ""
        self.interests = []
        self.itinerary = ""
        logger.info("TravelPlanner initialized.")

    def set_city(self, city: str):
        try:
            self.city = city
            self.messages.append(HumanMessage(content=f"City: {city}"))
            logger.info(f"City set to: {city}")
        except Exception as e:
            logger.error(f"Error setting city: {e}")
            raise CustomException("Failed to set city", e)
        
    def set_interests(self, interests: str):
        try:
            self.interests = [interest.strip() for interest in interests.split(",")]
            self.messages.append(HumanMessage(content=f"Interests: {interests}"))
            logger.info("Interests are set successfully")
        except Exception as e:
            logger.error(f"Error setting interests: {e}")
            raise CustomException("Failed to set interests", e)
    
    def create_itinerary(self):
        try:
            logger.info(f"Generating itinerary for city: {self.city} with interests: {self.interests}")
            itinerary = generate_itinerary(self.city, self.interests)
            self.itinerary = itinerary
            self.messages.append(AIMessage(content=itinerary))
            logger.info("Itinerary generated successfully")
            return itinerary
        except Exception as e:
            logger.error(f"Error generating itinerary: {e}")
            raise CustomException("Failed to generate itinerary", e)