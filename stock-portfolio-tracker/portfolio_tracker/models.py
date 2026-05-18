from dataclasses import dataclass, asdict
import json
from pathlib import Path

DATA_FILE = Path(__file__).parent.parent / "data" / "holdings.json"

@dataclass
class Holding:
    ticker: str
    shares: float
    avg_buy_price: float

def load_holdings() -> list[Holding]:
    if not DATA_FILE.exists():
        DATA_FILE.parent.mkdir(exist_ok=True)
        return []
    with open(DATA_FILE) as f:
        raw = json.load(f)
    return [Holding(**h) for h in raw]

def save_holdings(holdings: list[Holding]):
    with open(DATA_FILE, "w") as f:
        json.dump([asdict(h) for h in holdings], f, indent=2)        