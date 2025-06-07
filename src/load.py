from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from config import DATABASE_URI

engine = create_engine(DATABASE_URI)
def load_to_db(df, table_name="weather_events"):
    try:
        
        df.to_sql(
            table_name,
            engine,
            if_exists="append",
            index=False,
            chunksize=20_000,
            method="multi")
        print(f"Loaded {len(df)} records into {table_name}")
    except SQLAlchemyError as e:
        print(f"❌ Database error: {e}")
        raise
    except Exception as e:
        print(f"❌ Unexpected error during load: {e}")
        raise