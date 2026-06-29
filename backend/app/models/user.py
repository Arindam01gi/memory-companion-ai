from  app.core.database import Base
from sqlalchemy import Column,Boolean,Integer,String,Enum as SqlEnum,DateTime
from sqlalchemy.sql import func
from enum import Enum


class UserRole(str,Enum):
    PATIENT = "patient"
    DOCTOR = "doctor"
    CAREGIVER = "caregiver"


class UserStatus(str,Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)

    email = Column(String(255), unique=True, nullable=False)

    password_hash = Column(String(255), nullable=False)

    role = Column(SqlEnum(UserRole), nullable=False)

    status = Column(
        SqlEnum(UserStatus),
        nullable=False,
        default=UserStatus.ACTIVE
    )

    profile_image_url = Column(String(500), nullable=True)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )