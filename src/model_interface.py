#imports for abstract interfaces
from abc import ABC, abstractmethod

class BaseModel(ABC):
    #everyone that uses basemodel must use this method
    @abstractmethod
    def generate(self, system_prompt: str, input_txt: str) -> str:
        pass


class MockModel(BaseModel):
    def __init__(self):
        self.mock_responses = {
            "velocissimo"
        }