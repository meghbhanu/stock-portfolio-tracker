import argparse
from tabulate import tabulate
from portfolio_tracker.models import load_holdings, save_holdings, Holding
from portfolio_tracker.portfolio import get_portfolio_summary

def cmd_add(args):
    holdings = load_holdings()
    tickers = [h.ticker.upper() for h in holdings]
    if args.ticker.upper() in tickers:
        print(f"  {args.ticker.upper()} already exists. Use 'update' to change it.")
        return
    holdings.append(Holding(
        ticker=args.ticker.upper(),
        shares=args.shares,
        avg_buy_price=args.avg_price
    ))
    save_holdings(holdings)
    print(f"  Added {args.ticker.upper()} — {args.shares} shares @ {args.avg_price}")

def cmd_view(args):
    rows = get_portfolio_summary(mock=args.mock)
    if not rows:
        print("  Portfolio is empty. Use 'add' to get started.")
        return

    def fmt_pnl(val):
        if val == "N/A":
            return val
        return f"+{val}" if val >= 0 else str(val)

    display = [{
        "Ticker": r["ticker"],
        "Shares": r["shares"],
        "Avg Buy": r["avg_buy"],
        "Current": r["current_price"],
        "Invested": r["invested"],
        "Value": r["current_value"],
        "P&L": fmt_pnl(r["pnl"]) if r["pnl"] != "N/A" else "N/A",
        "P&L %": f"{fmt_pnl(r['pnl_pct'])}%" if r["pnl_pct"] != "N/A" else "N/A"
    } for r in rows]

    print(tabulate(display, headers="keys", tablefmt="rounded_outline"))

    valid = [r for r in rows if r["pnl"] != "N/A"]
    if valid:
        total_invested = round(sum(r["invested"] for r in valid), 2)
        total_value = round(sum(r["current_value"] for r in valid), 2)
        total_pnl = round(total_value - total_invested, 2)
        total_pct = round((total_pnl / total_invested) * 100, 2)
        sign = "+" if total_pnl >= 0 else ""
        print(f"\n  Total invested : {total_invested}")
        print(f"  Current value  : {total_value}")
        print(f"  Overall P&L    : {sign}{total_pnl} ({sign}{total_pct}%)")

def main():
    parser = argparse.ArgumentParser(prog="portfolio")
    sub = parser.add_subparsers(dest="command")

    p_add = sub.add_parser("add", help="Add a holding")
    p_add.add_argument("ticker")
    p_add.add_argument("shares", type=float)
    p_add.add_argument("avg_price", type=float)

    p_view = sub.add_parser("view", help="View portfolio with live P&L")
    p_view.add_argument("--mock", action="store_true", help="Use mock prices (no internet needed)")

    args = parser.parse_args()
    if args.command == "add":
        cmd_add(args)
    elif args.command == "view":
        cmd_view(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()