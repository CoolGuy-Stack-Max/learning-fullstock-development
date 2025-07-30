# ===== 1. Build stage =====
FROM python:3.12-slim AS builder

WORKDIR /app

# 复制源代码
COPY . .

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_HOME=/opt/poetry \
    POETRY_VERSION=2.1.3

# 安装基本依赖
RUN apt-get update && apt-get install -y curl build-essential && rm -rf /var/lib/apt/lists/*

# 安装 Poetry
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s $POETRY_HOME/bin/poetry /usr/local/bin/poetry


RUN poetry config virtualenvs.create true && poetry install --no-interaction --no-ansi --only main


# ===== 2. Runtime stage =====
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# 再次安装 poetry
ENV POETRY_HOME=/opt/poetry POETRY_VERSION=2.1.3

RUN curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s $POETRY_HOME/bin/poetry /usr/local/bin/poetry

ENV PATH="/opt/poetry/bin:$PATH"

COPY --from=builder /app /app

EXPOSE 8000
CMD ["poetry", "run", "uvicorn", "app.wsgi:app", "--host", "0.0.0.0", "--port", "8000"]