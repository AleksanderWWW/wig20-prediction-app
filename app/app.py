import datetime
from datetime import date

import streamlit as st

from scraper import gpw


st.title("WIG-20 Predictive Modeling")


today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)
start_date = st.date_input('Start date', today)
end_date = st.date_input('End date', tomorrow)
if start_date >= end_date:
    st.error('Error: End date must fall after start date.')
    


scraper = gpw.Wig20Scraper(start_date, end_date)
data_raw = scraper.get_data()

dataframe = gpw.parse_data(data_raw)


st.write(f"""
# Source data

Line chart with data for the selected date range.

         """)


st.area_chart(dataframe["close"])

