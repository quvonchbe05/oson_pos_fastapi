from api.db.base import Base
from sqlalchemy import Column, UUID, String, Integer, ForeignKey, Boolean, TIMESTAMP
from uuid import uuid4
from sqlalchemy.orm import relationship
from datetime import datetime




class User(Base):
    __tablename__ = 'user'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name: str = Column(String(155), nullable=True)
    username: str = Column(String(155), nullable=False, unique=True)
    email: str = Column(String(155), nullable=False, unique=True)
    password: str = Column(String, nullable=False)
    is_admin: bool = Column(Boolean, default=False)
    
    
    def __repr__(self):
        return f"{self.username}"


class Category(Base):
    __tablename__ = 'category'
    
    id = Column(Integer, primary_key=True)
    name: str = Column(String(155), nullable=True, unique=True)
    
    products = relationship("Product", back_populates="category")
    
    
    def __repr__(self) -> str:
        return f"{self.name}"

class Product(Base):
    __tablename__ = 'product'
    
    id = Column(Integer, primary_key=True)
    name: str = Column(String(155), nullable=True)
    amount: int = Column(Integer)
    price: str = Column(String(155))
    sale_price: str = Column(String(155))
    bar_code: str = Column(String(155), nullable=True, unique=True)
    category_id = Column(Integer, ForeignKey("category.id"))
    
    category = relationship("Category", back_populates="products")
    
    
    def __repr__(self) -> str:
        return f"{self.name}"
    
    
    
class Basket(Base):
    __tablename__ = 'basket'
    
    id = Column(Integer, primary_key=True)
    name: str = Column(Integer, ForeignKey('product.id'))
    count: int = Column(Integer)
    price: str = Column(String(155))
    total_price: str = Column(String(155))
    user = Column(ForeignKey('user.id'))
    
    
class Saled(Base):
    __tablename__ = 'saled'
    
    id = Column(Integer, primary_key=True)
    name: str = Column(String(255))
    count: int = Column(Integer)
    price: str = Column(String(155))
    total_price: str = Column(String(155))
    user = Column(ForeignKey('user.id'))
    date = Column(TIMESTAMP, default=datetime.now())