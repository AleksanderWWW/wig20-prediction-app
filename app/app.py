from datetime import date

import streamlit as st

from scraper import gpw


start = date(2021, 7, 5)
end = date(2022, 7, 5)

scraper = gpw.Wig20Scraper(start, end)
data_raw = scraper.get_data()

dataframe = gpw.parse_data(data_raw)

item = dataframe.iloc[3, 4]


st.title("Dummy title")

st.write(f"""
# Dummy heading

Dummy content.

{item}
         """)