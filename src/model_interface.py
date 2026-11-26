#imports for abstract interfaces
from abc import ABC, abstractmethod

class BaseModel(ABC):
    #everyone that uses basemodel must use this method
    @abstractmethod
    def generate(self, system_prompt: str, input_txt: str) -> str:
        pass


class MockModel(BaseModel):
    def __init__(self):
        #mock dictionary for tests
        self.mock_responses = {
            "tall": "Positive",
            "short": "Negative",
            "average": "Neutral"
        }

    def generate(self, system_prompt: str, input_txt: str) -> str:
        if "expert prompt engineer" in input_txt.lower():
            return "Classify sentiment as Positive, Negative, or Neutral. Pay extra attention to customer service feedback."

        #looking for a key word to return a mocked sentiment
        for key, value in self.mock_responses.items():
            if key in input_txt.lower():
                return value
        return "Positive"