import uuid

from sqlalchemy import Column, String, Boolean, Enum

from sqlalchemy.dialects.postgresql import UUID
from app.database import Base
import enum

class UserRole (str, enum.Enum):
    JOB_SEEKER = "job_seeker"
    EMPLOYER = "employer"
    ADMIN = "admin"

class User(Base):
    __tablename__ = "users"
    #  Sử dụng UUID làm khóa chính thay vì Integer để tăng tính bảo mật và phân tán
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True) 
    email = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String, nullable=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    role = Column(Enum(UserRole), default=UserRole.EMPLOYER)