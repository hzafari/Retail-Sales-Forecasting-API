# SESO FastAPI – Retail Sales Forecasting API

A production-ready retail sales forecasting system built with FastAPI, containerized using Docker, and designed with reproducibility and deployment in mind.

Provides store-level forecasts, sMAPE evaluation, and visualization.

======== Features =================
Store-level forecasting
sMAPE evaluation
CLI visualization
REST API interface
Dockerized deployment
Reproducible environment

============== Project Structure ==============
app/
training/
data/
models/
docs/
Dockerfile
requirements.txt

============ How To Run (Local) ===============
python -m venv .venv
pip install -r requirements.txt
uvicorn app.main:app --reload

http://127.0.0.1:8000/docs


================= How To Run With Docker ================
docker build -t seso-forecast .
docker run -p 8000:8000 seso-forecast

================= How To Use API ==================
Example request:
GET /forecast?store=1&horizon=14

Example response JSON:
{
  "store": 1,
  "horizon": 10,
  "forecast_start": "2015-07-01",
  "forecast_end": "2015-07-10",
  "forecast": [
    5783.6568970825,
    5317.484546633362,
    5700.196458591089,
    4661.102096590676,
    4474.3959962138215,
    2906.4914175387103,
    17.401166450166784,
    5792.3806212638865,
    5326.208270814747,
    5708.9201827724755
  ]
}


================ How To Run Visualization ===================
python -m app.visualization --store 1 --horizon 14
If Docker:
docker run -it seso-forecast python -m app.visualization --store 1 --horizon 14

================ Author =====================
Hasan Zafari
