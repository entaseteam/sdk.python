"""Base class for all Entase objects"""
from typing import Any, Dict, Type, TypeVar

T = TypeVar('T', bound='ObjectBase')


class ObjectBase:
    """Base class for all Entase objects with casting functionality"""

    def __init__(self):
        """Initialize with type identifier"""
        self._data = {}
        self._data['::'] = self.__class__.__name__

    @classmethod
    def cast(cls: Type[T], obj: Dict[str, Any]) -> T:
        """Cast dictionary to object instance"""
        instance = cls()
        
        for property_name, value in obj.items():
            if property_name == '::':
                instance._data['::'] = value
            elif hasattr(instance, property_name):
                if value is not None and (isinstance(value, dict) or isinstance(value, list)):
                    subcast_type = value.get('::', None) if isinstance(value, dict) else None
                    
                    if subcast_type and hasattr(instance, f'_{subcast_type}'):
                        subcast_class = getattr(instance, f'_{subcast_type}')
                        setattr(instance, property_name, subcast_class.cast(value))
                    else:
                        setattr(instance, property_name, value)
                else:
                    setattr(instance, property_name, value)
                    
        return instance

    def __getitem__(self, key: str) -> Any:
        """Allow dictionary-style access"""
        return self._data.get(key)

    def __setitem__(self, key: str, value: Any):
        """Allow dictionary-style setting"""
        self._data[key] = value 