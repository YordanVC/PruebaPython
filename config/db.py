from sqlalchemy import create_engine, MetaData
# URL de conexión a Postgres:
# Formato: postgresql+psycopg2://usuario:password@host:puerto/nombre_base
user = "postgres"
password = "yordan123"
host = "localhost"
port = "5432"
db = "pruebaPython"

DATABASE_URL = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}"

engine = create_engine(DATABASE_URL)
meta = MetaData()
conn = engine.connect()
