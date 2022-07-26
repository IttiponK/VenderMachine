from .base.singleton import Singleton 
from typing import Optional

class Registry(metaclass=Singleton):
    def __init__(self):
        from ..port.db import DBPort
        self.stock:Optional[DBPort] = None 