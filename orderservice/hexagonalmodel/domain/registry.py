from typing import Optional
from .base.singleton import Singleton

class Registry(metaclass=Singleton):
    def __init__(self):
        from ..port.db import DBPort
        
        self.transaction: Optional[DBPort] = None
        self.rpc = None