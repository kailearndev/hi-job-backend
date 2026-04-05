
from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.core.security import security
from app.modules.auth.schemas import UserCreate

# 1. IMPORT REPOSITORY VÀ MODEL Ở ĐÂY
from .repository import auth_repo

class AuthService:
    def register_user(self, db: Session, user_body: UserCreate):
        try:
            if auth_repo.get_by_email(db, user_body.email):
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email đã tồn tại")
            hashed_password = security.hash_password(user_body.password)

            user_data = {
                "email": user_body.email,
                "full_name": user_body.full_name,
                "hashed_password": hashed_password,
                "role": user_body.role,
                "is_active": user_body.is_active,
            }

            return auth_repo.create_user(db, user_data)
        except HTTPException:
            raise
        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
                detail="Lỗi hệ thống khi lưu trữ dữ liệu.")
        except Exception as e:
            # Các lỗi không lường trước được
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Đã xảy ra lỗi: {str(e)}"
            )
    def login(self, db: Session, email: str, password: str):
        user = auth_repo.get_by_email(db, email)
        if not user or not security.verify_password(password, user.hashed_password):
            return None  # Sai email hoặc mật khẩu
        # Tạo JWT Token (có thể thêm thông tin khác vào payload nếu cần)
        token = security.create_access_token({"sub": str(user.id), "email": user.email})
        return {"access_token": token, "token_type": "bearer", "user": {"id": user.id, "email": user.email , "full_name": user.full_name, "role": user.role}}
    
auth_service = AuthService()