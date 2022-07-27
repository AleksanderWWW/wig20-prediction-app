import pandas as pd

# Modeling and Forecasting
# ==============================================================================
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

from skforecast.ForecasterAutoreg import ForecasterAutoreg
from skforecast.ForecasterAutoregCustom import ForecasterAutoregCustom
from skforecast.ForecasterAutoregMultiOutput import ForecasterAutoregMultiOutput
from skforecast.model_selection import grid_search_forecaster
from skforecast.model_selection import backtesting_forecaster

from src.model_choice import choose_best_from_grid



def train_auto_regressor(train_data: pd.DataFrame, col, lags, random_state, steps):
    forecaster = ForecasterAutoreg(
                    regressor = LinearRegression(),
                    lags      = lags # This value will be replaced in the grid search
                )

    # Lags used as predictors
    lags_grid = [5, 15]

    # Regressor's hyperparameters
    param_grid = {'n_estimators': [100, 500],
                'max_depth': [3, 5, 10]}

    results_grid = grid_search_forecaster(
                            forecaster         = forecaster,
                            y                  = train_data[col],
                            param_grid         = param_grid,
                            lags_grid          = lags_grid,
                            steps              = steps,
                            refit              = True,
                            metric             = 'mean_squared_error',
                            initial_train_size = int(len(train_data)*0.5),
                            fixed_train_size   = False,
                            return_best        = True,
                            verbose            = False
                )

    best_model = choose_best_from_grid(results_grid)

    return best_model


def predict_values(train_data, col, steps: int, reggressor_type, lags: int, **reg_params):
    regressor = reggressor_type(**reg_params)
    forecaster = ForecasterAutoreg(
                regressor = regressor,
                lags      = lags
             )

    forecaster.fit(y=train_data[col])

    return forecaster.predict(steps=steps)


def train_lr(train_data, col, lags):
    forecaster = ForecasterAutoreg(
                    regressor = LinearRegression(),
                    lags      = lags # This value will be replaced in the grid search
                )
    forecaster.fit(train_data[col])
    return forecaster
