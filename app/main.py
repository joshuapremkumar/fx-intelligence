from fastapi import FastAPI, HTTPException
from app.models.schema import RequestModel
from app.services.fx_service import get_rate
from app.services.tavily_service import get_news
from app.services.analysis import analyze_data

app = FastAPI(title="FX Intelligence API")

@app.get("/")
def home():
    return {"message": "FX Intelligence API Running"}

@app.post("/analyze")
def analyze(req: RequestModel):
    try:
        rate = get_rate(req.base, req.target)
        news = get_news(f"{req.base} {req.target} currency outlook")
        result = analyze_data(rate, news, req)

        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))