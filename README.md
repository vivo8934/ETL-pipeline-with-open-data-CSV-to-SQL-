
# 📊 Weather Events ETL Pipeline Project

This project implements a scalable ETL pipeline to ingest, clean, and store 8.6 million+ weather event records into a PostgreSQL database using Docker. It also includes a Streamlit dashboard for data exploration and pgAdmin for database inspection.



## ✅ Project Goals

- 🚀 Efficiently handle large CSV files with chunked loading.
- 🧹 Clean and normalize weather event data.
- 🗃️ Store structured data in PostgreSQL.
- 🧪 Ensure quality with testing and validation.
- 📊 Expose a dashboard for real-time exploration (Streamlit).
- 🛠️ Provide easy database access (pgAdmin).

## 🧱 Tech Stack

- Python, Pandas
- PostgreSQL (via Docker)
- SQLAlchemy
- Streamlit
- pgAdmin
- Docker + Docker Compose

# 🚀 How to start the project locally 

- 👉 git clone - https://github.com/vivo8934/ETL-pipeline-with-open-data-CSV-to-SQL-.git
- 👉 navigate to the folder **ETL-pipeline-with-open-data-CSV-to-SQL**
- 👉 pip install -r requirements.txt

## 🗃️ Dataset Setup (External Download)

This project processes a large CSV file (~1GB) containing historical weather events. Due to GitHub's 100MB file size limit, we **do not include the CSV file in the Git repository**.

### 📥 Download the CSV File

Download the dataset programmatically using the following options below:

1. Download from this link:  
   👉 [Google Drive - WeatherEvents_Jan2016-Dec2022.csv](https://drive.google.com/file/d/1LucwOt_ez1-yT5dUMxr-uwPdt-4iLa3F/view?usp=drive_link)

2. Download Package to get the file on the project Folder on your PC 
    👉 pip install gdown
    👉 gdown --id 1LucwOt_ez1-yT5dUMxr-uwPdt-4iLa3F -O /YOUR_PROJECT_PATH/WeatherEvents_Jan2016-Dec2022.csv

3. Don't Track the CSV File in Git 
    👉 echo "WeatherEvents_Jan2016-Dec2022.csv" >> .gitignore
    👉 git rm --cached WeatherEvents_Jan2016-Dec2022.csv
    👉 git commit -m "Remove large CSV file from repo"
    👉 git push origin main

## 🛠️ PostgreSQL Setup with Docker

This project uses **PostgreSQL** as the target database for loading transformed weather data. A Dockerized PostgreSQL instance is used for ease of development and isolation.

### 📦 Step 1: Environment Configuration

Create a `.env` file in the project root with the following:

```env
DB_USER=etl_user
DB_PASSWORD=etl_pass
DB_HOST=localhost
DB_PORT=5432
DB_NAME=weather_db

# Optional: CSV file path (default is shown below)
CSV_PATH=data/WeatherEvents_Jan2016-Dec2022.csv

docker compose -f docker/docker-compose.yml up -d

- Make sure the file WeatherEvents_Jan2016-Dec2022.csv is not tracked in Git, but is placed manually into the data/ directory (see earlier section on dataset download).



