import csv
from datetime import datetime
from pathlib import Path

def export_to_csv(rows: list[dict], out_path: str = "report.csv"):
    if not rows:
        print("  Nothing to export - portfolio is empty.")
        return
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    fieldnames = ["ticker", "shares", "avg_buy", "current_price", 
                  "invested", "current_value", "pnl", "pnl_pct", "exported_at"]
    
    path = Path(out_path)
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in rows:
            writer.writerow({**r, "exported_at": timestamp})

    print(f"  Exported {len(rows)} holdings to {path.resolve()}")