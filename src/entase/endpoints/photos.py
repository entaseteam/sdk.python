"""Photos endpoint"""
from typing import Optional, Dict, Any
from ..endpoint import Endpoint


class Photos(Endpoint):
    """Photos endpoint handler"""
    
    def __init__(self, client):
        super().__init__(client)
        self.endpoint_url = 'photos'

    def get_by_object(self, objref: str, data: Optional[Dict] = None) -> Any:
        """Get photos by object reference"""
        return self.client.get(f"{self.endpoint_url}/object/{objref}", data) 