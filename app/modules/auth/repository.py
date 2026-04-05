from sqlalchemy.orm import Session
from typing import Any


from .models import User

class AuthRepository:
    def get_by_email(self, db: Session, email: str) -> User | None:
        # // Truy vấn để lấy người dùng theo email
        return db.query(User).filter(User.email == email).first()
    def get_by_id(self, db: Session, user_id: str) -> User | None:
        # // Truy vấn để lấy người dùng theo ID
        return db.query(User).filter(User.id == user_id).first()
    
    def create_user(self, db: Session, user_data: dict[str, Any]) -> User:
        # // Tạo một đối tượng User mới từ dữ liệu đã được xác thực
        user = User(**user_data)
        db.add(user)  # Thêm người dùng mới vào session
        db.commit()  # Lưu thay đổi vào database
        db.refresh(user)  # Làm mới đối tượng để lấy ID đã được tạo
        return user  # Trả về người dùng mới tạo

auth_repo = AuthRepository()