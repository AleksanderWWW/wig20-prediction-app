import datetime

import streamlit as st
import matplotlib.pyplot as plt

from scraper import gpw
from models.prepare import split_data


st.title("WIG-20 Predictive Modeling")


today = datetime.date.today()
previous_date = today - datetime.timedelta(days=30)
start_date = st.date_input('Start date', previous_date)
end_date = st.date_input('End date', today)
if start_date >= end_date:
    st.error('Error: End date must fall after start date.')
    


scraper = gpw.Wig20Scraper(start_date, end_date)
data_raw = scraper.get_data()

dataframe = gpw.parse_data(data_raw)


st.write(f"""
## Source data

Line chart with data for the selected date range.

         """)


st.area_chart(dataframe)

st.header("Modeling")

column_chosen = st.selectbox("Choose column to model", [col.capitalize() for col in dataframe.columns]).lower()
test_size = st.slider("Choose test size [%]", 1, 100) / 100

train_df, test_df = split_data(dataframe, column_chosen, test_size)

col1, col2 = st.columns(2)

with col1:
    st.header("Train set")

    st.dataframe(train_df)

with col2:
    st.header("Test set")

    st.dataframe(test_df)

fig, ax=plt.subplots(figsize=(9, 4))
train_df.plot(style="o", ax=ax, label='train')
test_df.plot(style="o", ax=ax, label='test')
ax.legend()
st.pyplot(fig)

