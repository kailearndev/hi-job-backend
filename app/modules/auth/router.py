from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db

# Import Schemas (khuôn dữ liệu) và Service (xử lý logic)
from .schemas import UserCreate, UserResponse
from .service import auth_service

router = APIRouter()

@router.post(
    "/register", 
    response_model=UserResponse, 
    status_code=status.HTTP_201_CREATED,
    summary="Đăng ký tài khoản mới"
)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    """
    Tạo tài khoản mới. Trả về thông tin User (đã được lọc mật khẩu thông qua UserResponse).
    Các lỗi như email trùng lặp sẽ do Service tự động ném ra.
    """
    return auth_service.register_user(db, user_in)


@router.post(
    "/login",
    summary="Đăng nhập để lấy JWT Token"
)
def login(user_in: UserCreate, db: Session = Depends(get_db)):
    """
    Kiểm tra email và mật khẩu. Nếu hợp lệ, trả về JWT Token và thông tin cơ bản.
    """
    # Giao cho Service xử lý xác thực
    result = auth_service.login(db, user_in.email, user_in.password)
    
    # Nếu Service trả về None (nghĩa là sai email hoặc pass)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Tài khoản hoặc mật khẩu không chính xác!",
            headers={"WWW-Authenticate": "Bearer"}, # Chuẩn Header cho lỗi 401 JWT
        )
        
    return result