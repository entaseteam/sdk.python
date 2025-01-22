"""Partners endpoint"""
from typing import Optional, Dict, Any
from ..endpoint import Endpoint
from ..exceptions import RequestError


class Partners(Endpoint):
    """Partners endpoint handler"""
    
    def __init__(self, client):
        super().__init__(client)
        self.endpoint_url = 'partners'

    def get_all(self, data: Optional[Dict] = None) -> Any:
        """Get all method not supported for Partners endpoint"""
        raise RequestError('GetAll method not supported for Partners endpoint.')

    def me(self) -> Any:
        """Get current partner info"""
        return self.client.get(f"{self.endpoint_url}/me") 