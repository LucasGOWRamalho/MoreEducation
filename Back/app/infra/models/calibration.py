from sqlalchemy import Column, Integer, Float, ForeignKey
from .base import Base

class Calibration(Base):
    __tablename__ = 'calibrations'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    accuracy = Column(Float)
    matrix_data = Column(String)  # Ou use JSON/ARRAY para dados complexos

    def __repr__(self):
        return f"<Calibration(id={self.id}, user={self.user_id})>"

__all__ = ['Calibration']