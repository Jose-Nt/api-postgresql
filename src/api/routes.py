from services.data_formatter import format_dataframe
from db.connection import get_connection
from db.queries import fetch_data
from flask import Blueprint, jsonify

routes = Blueprint('routes', __name__)

@routes.route('/query/<user>/<password>/<host>/<dbname>/<query>', methods=['GET'])
def get_data_with_sql_query(
        user: str, 
        password: str, 
        host: str, 
        dbname: str, 
        query: str
    ) -> jsonify:
    """
    Retrieve data from a specific database based on a SQL query and return it as JSON.

    Args:
        user (str): Database username.
        password (str): Database user's password.
        host (str): Host address of the database server.
        dbname (str): Name of the database.
        query (str): Query to execute in database.
    Returns:
        Response: JSON response containing formatted data.
    """
    connection = get_connection(user, password, host, dbname)
    df = fetch_data(connection, query)
    result = format_dataframe(df)

    return jsonify(result)