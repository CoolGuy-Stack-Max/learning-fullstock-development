FROM python:3.12-slim AS builder
WORKDIR /app
COPY . .
RUN pip install poetry
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi --only main

FROM python:3.12-slim
WORKDIR /app
COPY --from=builder /app /app
RUN pip install uvicorn
EXPOSE 8000
CMD ["uvicorn", "app.wsgi:app", "--host", "0.0.0.0", "--port", "8000"]