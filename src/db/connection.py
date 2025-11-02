from sqlalchemy.engine import Connection
from sqlalchemy import create_engine

def get_connection(
        user : str, 
        password : str, 
        host : str, 
        dbname : str
    ) -> Connection:
    """
    Establishes and returns a connection to the PostgreSQL database.

    Args:
        user (str): Database username.
        password (str): Database password.
        host (str): Database host address.
        dbname (str): Database name.
    Returns:
        Connection: A SQLAlchemy Connection object to the PostgreSQL database.
    """
    db_url = f"postgresql://{user}:{password}@{host}:5432/{dbname}"
    engine = create_engine(db_url)

    return engine.connect()