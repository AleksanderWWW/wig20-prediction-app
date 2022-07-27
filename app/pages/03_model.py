import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.metrics import mean_squared_error

from src.model import train_lr


st.title("Create a model")


def run_page():
    try:
        train_df = st.session_state["train_df"]
        test_df = st.session_state["test_df"]

    except KeyError:

        st.markdown("## No data available for modelling")
        return

    
    model_type = st.selectbox("Select model type to use as regressor", ["Linear regression"])

    column_chosen = st.selectbox("Choose column to model", train_df.columns)

    lags = st.slider("Number of lags in the model", min_value=1, max_value=len(train_df) // 2)

    model = {
        "Linear regression": train_lr
    }[model_type]
    
    

    res = model(train_df, "close", lags)

    predicted = res.predict(steps=len(test_df))

    mse = mean_squared_error(test_df[column_chosen], predicted)

    st.dataframe(pd.merge(test_df[column_chosen], predicted, left_index=True, right_index=True))

    st.markdown(f"### Model MSE: {mse}")

    fig, ax = plt.subplots(figsize=(9, 4))
    train_df[column_chosen].plot(style="o", ax=ax, label='train')
    test_df[column_chosen].plot(style="o", ax=ax, label='test')
    predicted.plot(style="o", ax=ax, label='predictions')
    ax.legend()
    st.pyplot(fig)


run_page()

