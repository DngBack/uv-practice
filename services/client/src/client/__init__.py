from base import BaseModel
from abc import ABC

class ClientInput(BaseModel):
    """Input model for client operations"""

    client_id: str = "123456789"
    client_secret: str = "my_client_secret"
    
class ClientOutput(BaseModel):
    """Output model for client operations"""

    access_token: str = "my_access_token"
    refresh_token: str = "my_refresh_token"
    
class Client(ABC):
    """Abstract base class for client operations"""

    def process(self, input: ClientInput) -> ClientOutput:
        """Process the input and return the output"""
        print("Processing client input...")
        return ClientOutput(access_token="processed_access_token", refresh_token="processed_refresh_token")
