from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from src.models.base import BaseModel

class Artwork(BaseModel):
    __tablename__ = "artworks"

    id = Column(Integer, primary_key=True)
    author = Column(String, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String)
    series = Column(String)
    size = Column(String)
    style = Column(String)
    price = Column(Float)
    link = Column(String)

    images = relationship("ArtworkImage", back_populates="artwork", cascade="all, delete")

class ArtworkImage(BaseModel):
    __tablename__ = "artwork_images"

    id = Column(Integer, primary_key=True)
    image_name = Column(String, nullable=False)
    artwork_id = Column(Integer, ForeignKey("artworks.id"), nullable=False)

    artwork = relationship("Artwork", back_populates="images")
