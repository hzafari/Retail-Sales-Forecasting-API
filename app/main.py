from fastapi import FastAPI, HTTPException
from app.schemas import ForecastRequest, ForecastResponse
from app.model import StoreForecaster
from app.config import MODEL_VERSION
import time


app = FastAPI(title="Store Forecasting API")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/forecast", response_model=ForecastResponse)
def forecast(request: ForecastRequest):

    start_time = time.time()

    try:
        forecaster = StoreForecaster(request.store_id)
        predictions = forecaster.forecast(request.horizon)

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    latency = time.time() - start_time
    print(f"Forecast latency: {latency:.4f} seconds")

    return ForecastResponse(
        store_id=request.store_id,
        forecast=predictions,
        model_version=MODEL_VERSION
    )
