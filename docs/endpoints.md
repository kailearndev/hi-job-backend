# API Endpoints

Tài liệu này mô tả các endpoint đang có trong project ở thời điểm hiện tại.

## Base URL

- Local: http://127.0.0.1:8000

## 1. Health Check

### GET /health-check

Kiểm tra trạng thái API và kết nối database.

- Success response 200:

```json
{
  "status": "ok",
  "details": "SELECT 1"
}
```

- Error response:

```json
{
  "status": "error",
  "details": "<error_message>"
}
```

## 2. Auth

Prefix của module auth: /auth

### POST /auth/register

Đăng ký tài khoản mới.

- Request body:

```json
{
  "email": "user@example.com",
  "password": "12345678",
  "full_name": "Demo User",
  "role": "job_seeker",
  "is_active": true
}
```

- Ghi chú field role khi đăng ký:
- Chỉ hỗ trợ: job_seeker, employer
- Mặc định: job_seeker

- Success response 201:

```json
{
  "id": "7e5d0c58-8b70-4b6a-b3cf-f72867f68d2d",
  "email": "user@example.com",
  "full_name": "Demo User",
  "role": "job_seeker",
  "is_active": true
}
```

- Error response:

```json
{
  "detail": "Email đã tồn tại"
}
```

### POST /auth/login

Đăng nhập và nhận JWT access token.

- Request body hiện tại dùng UserCreate schema:

```json
{
  "email": "user@example.com",
  "password": "12345678",
  "full_name": "Demo User",
  "role": "job_seeker",
  "is_active": true
}
```

- Success response 200:

```json
{
  "access_token": "<jwt_token>",
  "token_type": "bearer",
  "user": {
    "id": "7e5d0c58-8b70-4b6a-b3cf-f72867f68d2d",
    "email": "user@example.com",
    "full_name": "Demo User",
    "role": "job_seeker"
  }
}
```

- Error response 401:

```json
{
  "detail": "Tài khoản hoặc mật khẩu không chính xác!"
}
```

## 3. Tài liệu interactive

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## 4. Nguồn định nghĩa endpoint

- Router auth: app/modules/auth/router.py
- App entrypoint: app/main.py
- Schema request/response: app/modules/auth/schemas.py
