import streamlit as st
import matplotlib.pyplot as plt

from src.model import train_lr


st.title("Create a model")


def run_page():
    try:
        train_df = st.session_state["train_df"]
        test_df = st.session_state["test_df"]

    except KeyError:

        st.markdown("## No data available for modelling")
        return

    
    model_type = st.selectbox("Select model type to train", ["Linear regression"])

    column_chosen = st.selectbox("Choose column to model", train_df.columns)

    lags = st.slider("Number of lags in the model", min_value=1, max_value=len(train_df) // 2 + 1)

    model = {
        "Linear regression": train_lr
    }[model_type]
    
    st.table(train_df.head())

    res = model(train_df, "close", lags)

    predicted = res.predict(steps=len(test_df))

    fig, ax = plt.subplots(figsize=(9, 4))
    train_df[column_chosen].plot(style="o", ax=ax, label='train')
    test_df[column_chosen].plot(style="o", ax=ax, label='test')
    predicted.plot(style="o", ax=ax, label='predictions')
    ax.legend()
    st.pyplot(fig)


run_page()

