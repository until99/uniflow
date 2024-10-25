"""
This class aims to create a stable and resilient connection with diverse databases.
"""

from abc import ABC, abstractmethod
import oracledb
import psycopg2
from airflow.providers.oracle.hooks.oracle import OracleHook


class Connection(ABC):
    @abstractmethod
    def connect() -> None:
        """
        Abstract method to create a connection to a database.
        This method must be implemented by all subclasses.
        """
        pass


class OracleConnection(Connection):
    def __init__(
        self, username: str, password: str, service_name: str, host: str, port: int
    ):
        """
        Initializes an OracleConnection instance with the provided database credentials.

        - username (str): The username required to connect to the Oracle database.
        - password (str): The password associated with the given username.
        - service_name (str): The Oracle database service name.
        - host (str): The hostname or IP address of the Oracle database server.
        - port (int): The port on which the Oracle database is accessible.
        """
        self.username = username
        self.password = password
        self.service_name = service_name
        self.host = host
        self.port = port

    def connect(self):
        """
        Establishes and returns a connection to the Oracle database using the provided credentials.

        - Returns:
          oracledb.Connection: An active connection object to the Oracle database.
        """
        print("Initializing connection")

        con = oracledb.connect(
            user=self.username,
            password=self.password,
            service_name=self.service_name,
            host=self.host,
            port=self.port,
        )

        print("Successfully connected to:", con.dsn)

        return con


class PostgreSQLConnection(Connection):
    def __init__(
        self, username: str, password: str, database: str, host: str, port: int
    ):
        """
        Initializes a PostgreSQLConnection instance with the provided database credentials.

        - username (str): The username required to connect to the PostgreSQL database.
        - password (str): The password associated with the given username.
        - database (str): The name of the PostgreSQL database to connect to.
        - host (str): The hostname or IP address of the PostgreSQL database server.
        - port (int): The port on which the PostgreSQL database is accessible.
        """
        self.username = username
        self.password = password
        self.database = database
        self.host = host
        self.port = port

    def connect(self):
        """
        Establishes and returns a connection to the PostgreSQL database using the provided credentials.

        - Returns:
          psycopg2.Connection: An active connection object to the PostgreSQL database.
        """
        con = psycopg2.connect(
            database=self.database,
            user=self.username,
            host=self.host,
            password=self.password,
            port=self.port,
        )

        return con


class AirflowConnection(Connection):
    def __init__(self, connection_id: str):
        """
        Initializes an AirflowConnection instance with the specified Airflow connection ID.

        - connection_id (str): The Airflow connection ID for the configured database.
        """
        self.connection_id = connection_id

    def connect(self):
        """
        Establishes and returns a connection to the Oracle database using the Airflow connection ID.

        - Returns:
          oracledb.Connection: An active connection object to the Oracle database through Airflow's OracleHook.
        """
        oracle_hook = OracleHook(self.connection_id)
        con = oracle_hook.get_conn()

        return con
