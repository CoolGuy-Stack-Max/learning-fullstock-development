from app.db.session import engine
from app.db.base import Base
from app.models import order  # noqa: F401  # 导入模型以便创建表


# def init_db() -> None:
#     Base.metadata.create_all(bind=engine)


# if __name__ == '__main__':
#     init_db()