from abc import ABC, abstractclassmethod

class Vector(ABC):
    def __init__(self):
        self.dtype = "abstract_vector"

    @abstractclassmethod
    def __del__(self):
        pass
        
    @abstractclassmethod
    def __len__(self):
        pass
    
    @abstractclassmethod
    def __getitem__(self, i):
        pass
    
    @abstractclassmethod
    def __iter__(self):
        pass

    @abstractclassmethod
    def __repr__(self):
        pass

    @abstractclassmethod
    def append(self, i):
        pass