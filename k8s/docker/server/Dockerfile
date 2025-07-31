# ======================================================
# 1. 构建阶段 (builder): 安装工具并构建依赖
# ======================================================
FROM python:3.12-slim AS builder

# 设置工作目录
WORKDIR /app

# 安装构建工具 poetry
RUN pip install poetry

# 仅复制依赖定义文件，以利用 Docker 缓存
COPY poetry.lock pyproject.toml ./

# 配置 poetry 不创建虚拟环境，并将依赖安装到系统路径，且不安装项目本身。
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi --only main --no-root

# 复制剩余的源代码
COPY . .


# ======================================================
# 2. 运行阶段 (final): 创建干净的最终镜像
# ======================================================
FROM python:3.12-slim

# 设置工作目录
WORKDIR /app

# 设置 PYTHONPATH 环境变量
ENV PYTHONPATH=/app

# (之前的修复) 将Python脚本的安装路径添加到系统的PATH中
ENV PATH="/usr/local/bin:$PATH"

# 从 builder 阶段复制已安装的 Python 依赖包到最终镜像
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages

# 从 builder 阶段复制你的应用程序源代码
COPY --from=builder /app /app

# 暴露端口
EXPOSE 8000

# --- 最终修复：使用 shell 形式的 CMD 来确保工作目录正确 ---
# CMD ["sh", "-c", "python -m uvicorn app.wsgi:app --host 0.0.0.0 --port 8000"]
CMD ["sleep", "infinity"]