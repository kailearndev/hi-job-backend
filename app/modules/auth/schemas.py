import uuid
from enum import Enum
from typing import Optional

from pydantic import BaseModel, EmailStr

class UserRole(str, Enum):
    JOB_SEEKER = "job_seeker"
    EMPLOYER = "employer"
    ADMIN = "admin"

# // Nếu bạn muốn có một enum riêng cho việc đăng ký (chỉ cho phép job_seeker và employer), bạn có thể tạo thêm một enum khác như sau:
class RegistrationRole(str, Enum):
    JOB_SEEKER = "job_seeker"
    EMPLOYER = "employer"

class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None  # Thêm trường này vì bạn có dùng ở Service

class UserCreate(UserBase):
    password: str
    role: RegistrationRole = RegistrationRole.JOB_SEEKER 
    full_name: str
    is_active: bool = True

class UserResponse(UserBase):
    id: uuid.UUID
    role: UserRole
    is_active: bool

    class Config:
        from_attributes = True