import streamlit as st

import matplotlib.pyplot as plt

from src.prepare import split_data


st.title("Prepare data for modelling")

if "test_size" not in st.session_state:

    st.session_state["test_size"] = 20


st.markdown("## Split data to train-test sets")

if "dataframe" in st.session_state:

    dataframe = st.session_state["dataframe"]

    test_size = st.slider("Choose test size [%]", 1, 100, value=st.session_state["test_size"], step=1) / 100
    
    st.session_state["test_size"] = int(test_size * 100)

    train_df, test_df = split_data(dataframe, test_size)

    st.session_state["train_df"] = train_df
    st.session_state["test_df"] = test_df

    column_chosen = st.selectbox("Choose column to display", dataframe.columns)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Train set")

        st.write(f"(obs. = {len(train_df)})")

        st.table(train_df[column_chosen].head())

    with col2:
        st.markdown("### Test set")

        st.write(f"(obs. = {len(test_df)})")

        st.table(test_df[column_chosen].head())

    st.markdown(f"### Train-test split for column '{column_chosen}'")

    fig, ax=plt.subplots(figsize=(9, 4))
    train_df[column_chosen].plot(style="o", ax=ax, label='train')

    if len(test_df) > 0:
        test_df[column_chosen].plot(style="o", ax=ax, label='test')
    ax.legend()
    st.pyplot(fig)

else:
    st.markdown("## No data has been loaded yet.")