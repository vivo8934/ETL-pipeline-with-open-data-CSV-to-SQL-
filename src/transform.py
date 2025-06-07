def transform_weather_data(df):
    try: 
        df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_") 
        required_cols = ["starttime(utc)", "type"]
        for col in required_cols:
            if col not in df.columns:
                raise ValueError(f"Missing required column: '{col}'")
        df = df.dropna(subset=required_cols)
        df['type'] = df['type'].astype(str).str.strip().str.lower()
        return df
    except Exception as e:
        raise RuntimeError(f"Error during transformation: {e}")
