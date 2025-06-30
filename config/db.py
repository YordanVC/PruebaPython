from sqlalchemy import create_engine, MetaData
# URL de conexión a Postgres:
# Formato: postgresql+psycopg2://usuario:password@host:puerto/nombre_base
DATABASE_URL = "postgresql+psycopg2://postgres:yordan123@localhost:5432/prueba"
engine = create_engine(DATABASE_URL)
meta = MetaData()
conn = engine.connect()
