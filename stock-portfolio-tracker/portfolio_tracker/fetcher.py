import yfinance as yf
import socket

def get_current_price(ticker: str) -> float | None:
    try:
        info = yf.Ticker(ticker).fast_info
        price = info.last_price
        if price is None or price == 0:
            return None
        return round(price, 2)
    except socket.gaierror:
        print("  No internet connection. Try running with --mock flag.")
        return None
    except Exception as e:
        print(f"  Could not fetch price for {ticker}: {e}")
        return None