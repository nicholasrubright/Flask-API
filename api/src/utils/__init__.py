def get_connection_str(host: str, database: str, username: str, password: str) -> str:
    return f"postgresql+psycopg2://{username}:{password}@{host}/{database}"