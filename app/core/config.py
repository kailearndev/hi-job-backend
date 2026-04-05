from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # --- CÁC BIẾN CỦA MODULE AUTH ---
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # --- CÁC BIẾN CỦA DATABASE (Đã có sẵn trong file .env của bạn) ---
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432
    DATABASE_URL: str

    # Cấu hình đọc file .env và BỎ QUA các biến thừa (extra="ignore")
    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8",
        extra="ignore" # Dòng này chính là "thần chú" để fix lỗi của bạn
    )

# Khởi tạo instance dùng chung
settings = Settings()