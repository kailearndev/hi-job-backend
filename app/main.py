from fastapi import Depends, FastAPI, Request
from fastapi.responses import JSONResponse
from sqlalchemy import text
from sqlalchemy.orm import Session
from app.database import Base, engine, get_db

# Import model modules so SQLAlchemy metadata includes their tables.
from app.modules.auth import models as auth_models

from app.modules.auth.router import router as auth_router

app = FastAPI(
    title="Job Board API",
    description="Hệ thống quản lý tin tuyển dụng",
    version="1.0.0"
)


@app.on_event("startup")
def on_startup() -> None:
    Base.metadata.create_all(bind=engine)

app.include_router(auth_router, prefix="/auth", tags=["Authentication"])

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    # Log lỗi ra terminal để lập trình viên xem
    print(f"Lỗi nghiêm trọng: {exc}") 
    return JSONResponse(
        status_code=500,
        content={"message": "Hệ thống đang bảo trì, vui lòng thử lại sau!"},
    )
@app.get("/health-check")
def health_check(db: Session = Depends(get_db)):
    try: 
        # Thử truy vấn đơn giản để kiểm tra kết nối
        query =  text("SELECT 1")
        db.execute(query)
        return {"status": "ok", "details": query}
    except Exception as e:
        return {"status": "error", "details": str(e)}