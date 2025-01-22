"""
Main client class for Entase API communication
"""
import json
import requests
from typing import Optional, Dict, Any, Union

from .env import env
from .exceptions import CURLError, RequestError, APIError
from .endpoints import (
    Productions,
    Events,
    Photos,
    Partners,
    BookingOrders
)
from .object_collection import ObjectCollection


class Client:
    """Main client class for interacting with Entase API"""
    
    def __init__(self, secret_key: str):
        """Initialize client with secret API key"""
        self._secret_key = secret_key
        
        # Initialize endpoints
        self.productions = Productions(self)
        self.events = Events(self)
        self.photos = Photos(self)
        self.partners = Partners(self)
        self.booking_orders = BookingOrders(self)

    def get(self, endpoint: str, data: Optional[Dict] = None) -> Any:
        """Make GET request to API endpoint"""
        return self._query(endpoint, data, 'get')

    def post(self, endpoint: str, data: Optional[Dict] = None) -> Any:
        """Make POST request to API endpoint"""
        return self._query(endpoint, data, 'post')

    def _query(self, endpoint: str, data: Optional[Dict], method: str) -> Any:
        """Make HTTP request to API endpoint"""
        # Build URL
        url = endpoint if endpoint.startswith('https://') else f"{env.API_URL}{endpoint}"
        
        # Add query params for GET requests
        if method == 'get' and data:
            glue = '&' if '?' in endpoint else '?'
            url = f"{url}{glue}{self._dict_to_query(data)}"

        # Set up headers
        headers = {
            'Authorization': f'Bearer {self._secret_key}'
        }

        try:
            # Make request
            if method == 'get':
                response = requests.get(url, headers=headers, verify=not env.DEBUG_MODE)
            else:
                response = requests.post(
                    url, 
                    headers=headers,
                    data=self._dict_to_query(data) if data else None,
                    verify=not env.DEBUG_MODE
                )

            # Parse response
            result = response.json()

            # Handle errors
            if response.status_code != 200:
                msg = result.get('msg', 'General request error.')
                err_code = result.get('code', '')
                error_msg = f"{msg}{f' Code: {err_code}' if err_code else ''}"
                raise RequestError(error_msg, response.status_code)

            if result.get('status') != 'ok':
                msg = result.get('msg', 'General API error.')
                err_code = result.get('code', '')
                error_msg = f"{msg}{f' Code: {err_code}' if err_code else ''}"
                raise APIError(error_msg, response.status_code)

            # Handle response
            resource = result.get('resource')
            if resource and resource.get('::') == 'ObjectCollection':
                collection = ObjectCollection.cast(resource)
                collection.set_client(self)
                return collection
            return resource

        except requests.exceptions.RequestException as e:
            raise CURLError(str(e))

    @staticmethod
    def _dict_to_query(data: Dict, wrap: Optional[str] = None) -> str:
        """Convert dictionary to URL query string"""
        parts = []
        wrap_prefix = wrap or ''
        
        for key, value in data.items():
            if isinstance(value, dict):
                parts.append(Client._dict_to_query(
                    value,
                    f"{wrap_prefix}[{key}]" if wrap_prefix else key
                ))
            else:
                key_str = f"{wrap_prefix}[{key}]" if wrap_prefix else key
                parts.append(f"{key_str}={requests.utils.quote(str(value))}")
                
        return '&'.join(parts) 