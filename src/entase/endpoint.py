"""Base endpoint class for all API endpoints"""
from typing import Optional, Dict, Any


class Endpoint:
    """Base class for all API endpoints"""
    
    def __init__(self, client):
        """Initialize endpoint with client instance"""
        self.client = client
        self.endpoint_url = ''

    def get_all(self, data: Optional[Dict] = None) -> Any:
        """Get all resources for this endpoint"""
        return self.client.get(self.endpoint_url, data)

    def get_by_id(self, id_: str) -> Any:
        """Get resource by ID"""
        if ':' in id_:
            id_ = id_.split(':')[1]
        return self.client.get(f"{self.endpoint_url}/{id_}") 