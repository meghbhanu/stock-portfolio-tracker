from portfolio_tracker.models import load_holdings
from portfolio_tracker.fetcher import get_current_price

def get_portfolio_summary(mock:bool=False) -> list[dict]:
    holdings = load_holdings()
    if not holdings:
        return []
    
    MOCK_PRICES = {
        "INFY.NS": 1580.0,
        "RELIANCE.NS": 2910.0,
        "AAPL": 213.0
    }

    rows = []
    for h in holdings:
        price = MOCK_PRICES.get(h.ticker, 1500.0) if mock else get_current_price(h.ticker)
        
        if price is None:
            rows.append({
                "ticker": h.ticker,
                "shares": h.shares,
                "avg_buy": h.avg_buy_price,
                "current_price": "N/A",
                "invested": round(h.shares * h.avg_buy_price, 2),
                "current_value": "N/A",
                "pnl": "N/A",
                "pnl_pct": "N/A"
            })
            continue

        invested = round(h.shares * h.avg_buy_price, 2)
        current_value = round(h.shares * price, 2)
        pnl = round(current_value - invested, 2)
        pnl_pct = round((pnl / invested) * 100, 2) 

        rows.append({
            "ticker": h.ticker,
            "shares": h.shares,
            "avg_buy": h.avg_buy_price,
            "current_price": price,
            "invested": invested,
            "current_value": current_value,
            "pnl": pnl,
            "pnl_pct": pnl_pct
        })
    return rows    