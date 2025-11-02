from sqlalchemy.engine import Connection
import pandas as pd

def fetch_data(
        connection : Connection, 
        query : str
    ) -> pd.DataFrame:
    """
    Fetches data based on a SQL query in the database.
    
    Args:
        connection (Connection): Database connection object.
        query (str): SQL query to execute.
    Returns:
        pd.DataFrame: DataFrame containing the data.
    """
    df = pd.read_sql_query(query, connection)

    return df