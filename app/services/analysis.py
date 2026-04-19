def analyze_data(rate, news, req):
    headlines = [n["title"] for n in news]

    trend = "stable"
    signal = "hold"

    if rate > 80:
        trend = "uptrend"
        signal = "buy"
    elif rate < 70:
        trend = "downtrend"
        signal = "sell"

    return {
        "pair": f"{req.base}/{req.target}",
        "rate": rate,
        "trend": trend,
        "signal": signal,
        "news": headlines,
        "insight": headlines[0] if headlines else "No major news"
    }