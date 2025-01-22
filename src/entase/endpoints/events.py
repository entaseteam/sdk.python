"""Events endpoint"""
from ..endpoint import Endpoint


class Events(Endpoint):
    """Events endpoint handler"""
    
    def __init__(self, client):
        super().__init__(client)
        self.endpoint_url = 'events' 