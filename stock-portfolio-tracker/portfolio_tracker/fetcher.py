import yfinance as yf

def get_current_price(ticker) -> float | None:
    try:
        info = yf.Ticker(ticker).fast_info
        price = info.last_price
        if price is None or price == 0:
            return None
        return round(price, 2)
    except Exception:
        return None