import os
import pandas as pd
import joblib
from statsmodels.tsa.holtwinters import ExponentialSmoothing


DATA_PATH = "data/train.csv"
MODEL_DIR = "models"
SEASONAL_PERIODS = 7  # weekly seasonality


def prepare_data(df: pd.DataFrame):
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values(["Store", "Date"])
    return df


def train_store_model(store_df: pd.DataFrame):
    series = store_df["Sales"].values

    model = ExponentialSmoothing(
        series,
        trend="add",
        seasonal="add",
        seasonal_periods=SEASONAL_PERIODS
    ).fit()

    return model


def main():
    os.makedirs(MODEL_DIR, exist_ok=True)

    df = pd.read_csv(DATA_PATH)
    df = prepare_data(df)

    stores = df["Store"].unique()

    for store_id in stores:
        store_df = df[df["Store"] == store_id]

        if len(store_df) < SEASONAL_PERIODS * 2:
            print(f"Skipping store {store_id} (not enough data)")
            continue

        model = train_store_model(store_df)

        model_path = os.path.join(MODEL_DIR, f"store_{store_id}.pkl")
        joblib.dump(model, model_path)

        print(f"Saved model for store {store_id}")


if __name__ == "__main__":
    main()
