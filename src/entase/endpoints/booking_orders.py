"""Booking orders endpoint"""
from typing import Any
from ..endpoint import Endpoint


class BookingOrders(Endpoint):
    """Booking orders endpoint handler"""
    
    def __init__(self, client):
        super().__init__(client)
        self.endpoint_url = 'bookingorders'

    def get_by_code(self, order_code: str) -> Any:
        """Get booking order by code"""
        return self.get_by_id(order_code)

    def get_all_tickets_by_order(self, order_id_or_code: str) -> Any:
        """Get all tickets for a booking order"""
        return self.client.get(f"{self.endpoint_url}/{order_id_or_code}/tickets")

    def get_ticket_by_order(self, order_id_or_code: str, ticket_id_or_code: str) -> Any:
        """Get specific ticket from a booking order"""
        return self.client.get(
            f"{self.endpoint_url}/{order_id_or_code}/tickets/{ticket_id_or_code}"
        ) 