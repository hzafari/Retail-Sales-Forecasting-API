import os
import joblib
from app.config import MODEL_DIR


class StoreForecaster:

    def __init__(self, store_id: int):
        self.store_id = store_id
        self.model_path = os.path.join(MODEL_DIR, f"store_{store_id}.pkl")

        if not os.path.exists(self.model_path):
            raise ValueError(f"No model found for store {store_id}")

        self.model = joblib.load(self.model_path)

    def forecast(self, horizon: int):
        if horizon <= 0:
            raise ValueError("Horizon must be positive")

        preds = self.model.forecast(steps=horizon)

         # Clamp negative values
        preds = [max(0, p) for p in preds]

        return preds
