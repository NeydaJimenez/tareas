import mysql.connector
from mysql.connector import Error, pooling

class Database:
    """Gestor de conexión a MySQL usando pool de conexiones."""

    _pool = None

    CONFIG = {
        "host": "localhost",
        "port": 3306,
        "user": "root",
        "password": "tu_password_mysql",
        "database": "tareas_db",
        "charset": "utf8mb4",
    }

    @classmethod
    def init_pool(cls):
        if cls._pool is None:
            try:
                cls._pool = pooling.MySQLConnectionPool(
                    pool_name="tareas_pool",
                    pool_size=5,
                    **cls.CONFIG,
                )
                print("✓ Pool de conexiones MySQL creado")
            except Error as e:
                print(f"✗ Error al conectar a MySQL: {e}")
                raise

    @classmethod
    def get_connection(cls):
        if cls._pool is None:
            cls.init_pool()
        return cls._pool.get_connection()

    @classmethod
    def execute(cls, query: str, params: tuple = (), fetch: bool = False):
        """Ejecuta una query. Si fetch=True devuelve resultados como lista de dicts."""
        conn = cls.get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute(query, params)
            if fetch:
                result = cursor.fetchall()
            else:
                conn.commit()
                result = cursor.lastrowid
            return result
        except Error as e:
            conn.rollback()
            print(f"✗ Error en query: {e}")
            raise
        finally:
            cursor.close()
            conn.close()
