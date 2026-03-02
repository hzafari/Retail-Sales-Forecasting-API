# Retail Sales Forecasting API

A production-ready retail sales forecasting system built with FastAPI, containerized using Docker, and designed with reproducibility and deployment in mind.

Provides store-level forecasts, sMAPE evaluation, and visualization.

---

## Features

- Store-level forecasting  
- sMAPE evaluation metric  
- CLI visualization tool  
- REST API interface  
- Dockerized deployment  
- Reproducible environment  

---

## Project Structure

```
forecasting-api/
│
├── app/
│   ├── main.py
│   ├── model.py
│   ├── schemas.py
│   └── config.py
│
├── training/
│   └── train.py
│
├── models/
├── data/
│   └── train.csv
│
├── docs/
├── Dockerfile
├── requirements.txt
├── .dockerignore
├── .gitignore
└── README.md
```

---

## How To Run (Local)

Create virtual environment:

```bash
python -m venv .venv
```

Activate it:

**Windows**
```bash
.venv\Scripts\activate
```

**Mac/Linux**
```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run API:

```bash
uvicorn app.main:app --reload
```

Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## How To Run With Docker

Build image:

```bash
docker build -t seso-forecast .
```

Run container:

```bash
docker run -p 8000:8000 seso-forecast
```

Then open:

```
http://localhost:8000/docs
```

---

## How To Use API

Example request:

```
GET /forecast?store=1&horizon=14
```

Example response:

```json
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
```

---

## Visualization

Run locally:

```bash
python -m app.visualization --store 1 --horizon 14
```

Run with Docker:

```bash
docker run -it seso-forecast python -m app.visualization --store 1 --horizon 14
```

---

## Author

Hasan Zafari