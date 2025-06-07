import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import os
import plotly.express as px

# ---- Page config ----
st.set_page_config(page_title="Weather Events Dashboard", layout="wide")

# ---- Database connection ----
engine = create_engine(
    f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)

# ---- Title ----
st.title("🌦️ US Weather Events Dashboard")

# ---- Load data ----
@st.cache_data
def load_data():
    query = "SELECT * FROM weather_events LIMIT 100000"
    return pd.read_sql(query, engine)

df = load_data()

# ---- Sidebar filters ----
st.sidebar.header("🔍 Filter Options")

cities = df['city'].dropna().unique()
types = df['type'].dropna().unique()

selected_city = st.sidebar.multiselect("City", options=sorted(cities), default=[])
selected_type = st.sidebar.multiselect("Event Type", options=sorted(types), default=[])

df['starttime(utc)'] = pd.to_datetime(df['starttime(utc)'], errors='coerce')
date_range = st.sidebar.date_input("Date Range", [])

# ---- Apply filters ----
if selected_city:
    df = df[df['city'].isin(selected_city)]
if selected_type:
    df = df[df['type'].isin(selected_type)]
if len(date_range) == 2:
    df = df[(df['starttime(utc)'] >= pd.to_datetime(date_range[0])) & (df['starttime(utc)'] <= pd.to_datetime(date_range[1]))]

st.write(f"Filtered Events: {len(df):,}")

# ---- KPIs ----
st.subheader("📈 Key Metrics")
col1, col2, col3 = st.columns(3)

col1.metric("Total Events", len(df))
col2.metric("Unique Cities", df['city'].nunique())
col3.metric("Event Types", df['type'].nunique())

# ---- Charts ----
tab1, tab2, tab3 = st.tabs(["📊 Type Distribution", "📅 Events Over Time", "🗺️ Map"])

with tab1:
    type_counts = df['type'].value_counts().reset_index()
    type_counts.columns = ['type', 'count']
    fig = px.bar(type_counts, x='type', y='count', title="Event Type Frequency")
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    df['date'] = df['starttime(utc)'].dt.date
    date_counts = df.groupby('date').size().reset_index(name='count')
    st.line_chart(date_counts.set_index('date'))

with tab3:
    if 'locationlat' in df.columns and 'locationlng' in df.columns:
        st.map(df.rename(columns={'locationlat': 'latitude', 'locationlng': 'longitude'})[['latitude', 'longitude']].dropna())
    else:
        st.info("Latitude and Longitude not found in dataset.")

# ---- Data Preview ----
st.subheader("🧾 Sample Data")
st.dataframe(df.head(100))

# ---- Download ----
st.download_button(
    label="📥 Download Filtered Data as CSV",
    data=df.to_csv(index=False),
    file_name='filtered_weather_events.csv',
    mime='text/csv'
)

# ---- Footer ----
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit by Mfundo Ngqanekana | [GitHub](https://github.com/vivo8934/ETL-pipeline-with-open-data-CSV-to-SQL-)")
