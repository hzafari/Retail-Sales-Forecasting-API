from pydantic import BaseModel


class ForecastRequest(BaseModel):
    store_id: int
    horizon: int


class ForecastResponse(BaseModel):
    store_id: int
    forecast: list
    model_version: str
