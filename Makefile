# Biến số để dễ thay đổi nếu cần
APP_MODULE = app.main:app
PORT = 8000

# Lệnh chạy server phát triển
run:
	poetry run uvicorn $(APP_MODULE) --host 0.0.0.0 --port $(PORT) --reload

# Lệnh liên quan đến Migration (Alembic)
# Cách dùng: make migrate msg="tên_bản_chỉnh_sửa"
migrate-gen:
	poetry run alembic revision --autogenerate -m "$(msg)"

migrate-up:
	poetry run alembic upgrade head

migrate-down:
	poetry run alembic downgrade -1

# Lệnh dọn dẹp Docker và bật lại (Dành cho Postgres)
db-up:
	docker-compose up -d

db-down:
	docker-compose down

# Cài đặt toàn bộ môi trường từ đầu
install:
	poetry install