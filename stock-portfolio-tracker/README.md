# Stock Portfolio Tracker CLI

Track your stock portfolio from the terminal. Live prices via Yahoo Finance, P&L per holding, CSV export.

## Setup

```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Commands

| Command | Description |
|---|---|
| `python main.py add TICKER SHARES AVG_PRICE` | Add a holding |
| `python main.py view` | View live P&L table |
| `python main.py view --mock` | View with mock prices (offline) |
| `python main.py update TICKER SHARES AVG_PRICE` | Update a holding |
| `python main.py remove TICKER` | Remove a holding |
| `python main.py export` | Export to report.csv |
| `python main.py export --out myfile.csv` | Export to custom path |

## Example

```bash
$ python main.py add INFY.NS 50 1400
  Added INFY.NS — 50.0 shares @ 1400.0

$ python main.py view
╭──────────┬────────┬─────────┬─────────┬──────────┬──────────┬─────────┬────────╮
│ Ticker   │ Shares │ Avg Buy │ Current │ Invested │ Value    │ P&L     │ P&L %  │
├──────────┼────────┼─────────┼─────────┼──────────┼──────────┼─────────┼────────┤
│ INFY.NS  │   50.0 │  1400.0 │  1583.2 │  70000.0 │  79160.0 │ +9160.0 │+13.09% │
╰──────────┴────────┴─────────┴─────────┴──────────┴──────────┴─────────┴────────╯

  Total invested : 70000.0
  Current value  : 79160.0
  Overall P&L    : +9160.0 (+13.09%)
  Best performer : INFY.NS (+13.09%)
```

## Notes
- For Indian stocks (NSE), append `.NS` to the ticker — e.g. `INFY.NS`, `RELIANCE.NS`
- Use `--mock` flag if you're demoing without internet