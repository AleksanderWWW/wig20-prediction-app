import datetime

from src import extract

import streamlit as st


st.title("Extract data from GPW")


today = datetime.date.today()
previous_date = today - datetime.timedelta(days=30)
start_date = st.date_input('Start date', previous_date)
end_date = st.date_input('End date', today)
if start_date >= end_date:
    st.error('Error: End date must fall after start date.')
    


scraper = extract.Wig20Scraper(start_date, end_date)
data_raw = scraper.get_data()

dataframe = extract.parse_data(data_raw)

st.session_state["dataframe"] = dataframe

st.write(f"""
## Source data

Chart with data for the selected date range.

         """)


st.area_chart(dataframe)

num_obs_to_disp = st.slider("Display first: ", 1, len(dataframe))

st.table(dataframe.head(num_obs_to_disp))

st.write(f"Number of observations = {len(dataframe)}")


