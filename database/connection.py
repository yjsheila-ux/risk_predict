from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

# pip install aiosqlite
#sqlite 를 사용하겠다. -> 파일형태의 데이터베이스
DATABASE_URL = "sqlite+aiosqlite:///./db.sqlite"

engine = create_async_engine(DATABASE_URL)

AsyncSessionFactory = async_sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
)

async def get_session():
    session = AsyncSessionFactory()
    try:
        yield session
    finally:
        await session.close()