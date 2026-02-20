from sqlmodel import SQLModel, create_engine, Session

# 1. Define the name and connection string
sqlite_file_name = "ticks.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

# 2. Configure connection arguments for SQLite
connect_args = {"check_same_thread": False}

# 3. Create the Database Engine
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)


# 4. Create a function to initialize the database
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


# 5. Dependency function to get a database session
def get_session():
    with Session(engine) as session:
        yield session
