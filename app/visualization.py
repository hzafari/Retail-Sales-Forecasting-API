import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import argparse
from sklearn.metrics import mean_absolute_error
from app.model import StoreForecaster

DATA_PATH = "data/test.csv"

def calc_smape(y, q):
    score = np.where(y + q > 0, np.absolute((y - q)/(y + q)) * 200,0)
    return score


def plot_store_forecast(store_id: int, horizon:int):
    """
    Loads train.csv for model training reference,
    loads test.csv for evaluation,
    generates forecast aligned with test period,
    and plots actual vs forecast using sMAPE.
    """

    TEST_PATH = "data/test.csv"

    # Load test data (ground truth for evaluation)
    test_df = pd.read_csv(TEST_PATH, low_memory=False)
    test_df["Date"] = pd.to_datetime(test_df["Date"])
    test_df = test_df[test_df["Store"] == store_id].sort_values("Date")

    if len(test_df) == 0:
        raise ValueError(f"No test data found for store {store_id}")


    # Load trained model
    forecaster = StoreForecaster(store_id)
    forecast = forecaster.forecast(horizon)

    actuals = test_df["Sales"].values[:horizon]
    dates = test_df["Date"].values[:horizon]

    # ---- sMAPE ----
    actuals = np.array(actuals)
    forecast = np.array(forecast)

    smape = calc_smape(actuals, forecast).mean()

    # ---- Plot ----
    fig, ax = plt.subplots(figsize=(12,6))

    ax.plot(dates, actuals, label="Actual", marker="o")
    ax.plot(dates, forecast, label="Forecast", marker="x")

    ax.set_title(f"Store {store_id} Forecast vs Actuals", pad=20)
    ax.set_xlabel("Date")
    ax.set_ylabel("Sales")
    ax.grid(True, alpha=0.3)
    ax.legend()

    ax.annotate(
        f"sMAPE: {smape:.2f}%",
        xy=(0.5, 1.02),
        xycoords="axes fraction",
        ha="center",
        fontsize=12,
        fontweight="bold"
    )

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    print(f"sMAPE for store {store_id}: {smape:.2f}%")




# CLI support
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Plot store forecast vs actuals")
    parser.add_argument("--store", type=int, required=True, help="Store ID")
    parser.add_argument("--horizon", type=int, default=14, help="Forecast horizon in days")
    args = parser.parse_args()

    plot_store_forecast(store_id=args.store, horizon=args.horizon)
