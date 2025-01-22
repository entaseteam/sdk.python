"""Productions endpoint"""
from ..endpoint import Endpoint


class Productions(Endpoint):
    """Productions endpoint handler"""
    
    def __init__(self, client):
        super().__init__(client)
        self.endpoint_url = 'productions' 