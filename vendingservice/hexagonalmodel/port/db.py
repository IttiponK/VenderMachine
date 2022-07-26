from abc import ABC,abstractmethod

class DBPort(ABC):
    @abstractmethod
    def get_all_cash(self) -> list:
        pass 
    
    @abstractmethod
    def update_from_dict(self,changeObjupdate:dict):
        pass 