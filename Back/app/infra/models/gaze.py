from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from .base import Base
from datetime import datetime

class GazePoint(Base):
    __tablename__ = 'gaze_points'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    x = Column(Float)
    y = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)
    session_id = Column(String)

    def __repr__(self):
        return f"<GazePoint(x={self.x}, y={self.y})>"

__all__ = ['GazePoint']