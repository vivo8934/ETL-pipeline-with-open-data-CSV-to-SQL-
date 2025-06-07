import time
import logging
import traceback

from extract import extract_weather_data
from transform import transform_weather_data
from load import load_to_db

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("etl.log"),
        logging.StreamHandler()
    ]
)

def run_pipeline():
    start_time = time.time()
    total_rows = 0
    chunks_processed = 0
    failed_chunks = 0

    try:
        logging.info("🚀 Starting ETL pipeline.....")
        data_iterator = extract_weather_data()

        for i, chunk in enumerate(data_iterator, start=1):
            logging.info(f"🔄 Processing chunk {i}....")

        try:
            transformed_chunk = transform_weather_data(chunk)
            load_to_db(transformed_chunk)
            row_count = len(transformed_chunk)
            total_rows += row_count
            chunks_processed += 1
            logging.info(f"✅ Chunk {i} processed: {row_count} rows")
        except Exception as e:
            failed_chunks += 1
            logging.error(f"❌ Failed to process chunk {i}: {e}")
            logging.debug(traceback.format_exc())

    except Exception as pipeline_err:
        logging.critical(f"💥 Pipeline failed: {pipeline_err}")
        logging.debug(traceback.format_exc())
    finally:
        elapsed = time.time() - start_time
        logging.info("📊 ETL Pipeline Summary")
        logging.info(f"✅ Total rows processed: {total_rows}")
        logging.info(f"📦 Chunks successfully processed: {chunks_processed}")
        logging.info(f"❌ Chunks failed: {failed_chunks}")
        logging.info(f"⏱️ Total time taken: {elapsed:.2f} seconds")
        logging.shutdown()

if __name__ == "__main__":
    run_pipeline()
    logging.shutdown()
