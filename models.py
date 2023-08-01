from sqlalchemy import Column, Integer, String, Float, Boolean
from settings import Base
from pydantic import BaseModel


class Products(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    price = Column(Float)
    is_offer = Column(Boolean, default=False)
    

class Product(BaseModel):
    id: int
    title:  str
    price: float
    is_offer: bool 
    
    