# ======================================================
# 1. 构建阶段：安装依赖
# ======================================================
FROM python:3.12-slim AS builder

# 禁止 Poetry 创建虚拟环境。
# 我们将直接把包装在系统的 Python 路径中。
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry'

WORKDIR /app

# 安装 poetry 本身
RUN pip install poetry

# 只复制安装依赖所需的文件，以便利用 Docker 缓存
COPY poetry.lock pyproject.toml ./

# 将依赖安装到系统的 site-packages 中
RUN poetry install --no-root --only main

# 复制余下的应用源代码
COPY . .


# ======================================================
# 2. 运行阶段：创建最终的、干净的镜像
# ======================================================
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# 从构建阶段复制已安装的包
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages

# 从构建阶段复制应用代码
COPY --from=builder /app /app

EXPOSE 8000

# 直接运行应用。Uvicorn 现在位于系统的 PATH 中。
CMD ["uvicorn", "app.wsgi:app", "--host", "0.0.0.0", "--port", "8000"]