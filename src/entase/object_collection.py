"""Collection class for handling paginated results"""
from typing import List, Any, Optional, Iterator

from .object_base import ObjectBase


class ObjectCursor(ObjectBase):
    """Cursor for paginated results"""
    
    def __init__(self):
        super().__init__()
        self.nextURL = None
        self.hasMore = False


class ObjectCollection(ObjectBase):
    """Collection of objects with pagination support"""
    
    def __init__(self):
        super().__init__()
        self.data: List[Any] = []
        self.cursor: Optional[ObjectCursor] = None
        self._client = None
        self._current_index = 0

    def set_client(self, client):
        """Set client instance for making additional requests"""
        self._client = client

    @classmethod
    def cast(cls, obj: dict) -> 'ObjectCollection':
        """Cast dictionary to ObjectCollection instance"""
        instance = super().cast(obj)
        
        # Cast cursor if it exists
        if isinstance(instance.cursor, dict):
            cursor = ObjectCursor()
            cursor.nextURL = instance.cursor.get('nextURL')
            cursor.hasMore = instance.cursor.get('hasMore', False)
            instance.cursor = cursor
            
        return instance

    def has_more(self) -> bool:
        """Check if there are more results available"""
        if not self.cursor:
            return False
            
        if self.cursor.hasMore and self.cursor.nextURL:
            next_page = self._client.get(self.cursor.nextURL)
            if next_page and isinstance(next_page, ObjectCollection):
                self.data.extend(next_page.data)
                self.cursor = next_page.cursor
            return True
            
        return False

    def __iter__(self) -> Iterator[Any]:
        """Make collection iterable"""
        return iter(self.data)

    def __getitem__(self, key: str) -> Any:
        """Allow dictionary-style access"""
        if hasattr(self, key):
            return getattr(self, key)
        return None

    def __setitem__(self, key: str, value: Any):
        """Allow dictionary-style setting"""
        setattr(self, key, value) 