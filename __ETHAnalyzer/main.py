import ccxt
import pandas as pd
import numpy as np
from datetime import datetime, timedelta, timezone
from tabulate import tabulate
import argparse

# Fetch Coin data from Binance
def fetch_data(coin):
    binance = ccxt.binance()
    since = binance.parse8601((datetime.now(timezone.utc) - timedelta(days=730)).isoformat())
    ohlcv = binance.fetch_ohlcv(coin+'/USDT', timeframe='1d', since=since, limit=1000)
    
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    return df

# Perform extended analysis
def analyze_data(df):
    close_prices = df['close'].values
    returns = np.diff(close_prices) / close_prices[:-1]  # Daily returns

    # Basic Stats
    mean = np.mean(close_prices)
    std_dev = np.std(close_prices, ddof=1)
    variance = np.var(close_prices, ddof=1)
    minimum = np.min(close_prices)
    maximum = np.max(close_prices)
    percentile_25 = np.percentile(close_prices, 25)
    percentile_50 = np.percentile(close_prices, 50)
    percentile_75 = np.percentile(close_prices, 75)
    skewness = np.mean(((close_prices - mean) / std_dev)**3)
    kurtosis = np.mean(((close_prices - mean) / std_dev)**4) - 3
    
    # Additional Calculations
    coef_variation = std_dev / mean  # Coefficient of Variation
    cagr = (close_prices[-1] / close_prices[0]) ** (1 / (len(close_prices) / 365)) - 1  # CAGR assuming 1-day candles
    rolling_volatility = np.std(returns[-30:]) * np.sqrt(30)  # 30-day rolling volatility

    # Maximum Drawdown (MDD)
    peak = np.maximum.accumulate(close_prices)
    drawdown = (close_prices - peak) / peak
    max_drawdown = np.min(drawdown)

    # Sharpe Ratio (assuming risk-free rate = 0 for crypto)
    sharpe_ratio = np.mean(returns) / std_dev

    # Sortino Ratio (only downside deviation)
    downside_returns = returns[returns < 0]
    downside_std = np.std(downside_returns) if len(downside_returns) > 0 else 0
    sortino_ratio = np.mean(returns) / downside_std if downside_std > 0 else np.nan

    stats = {
        'Mean Price': mean,
        'Standard Deviation': std_dev,
        'Variance': variance,
        'Minimum Price': minimum,
        'Maximum Price': maximum,
        '25th Percentile': percentile_25,
        '50th Percentile': percentile_50,
        '75th Percentile': percentile_75,
        'Skewness': skewness,
        'Kurtosis': kurtosis,
        'Coefficient of Variation': coef_variation,
        'CAGR (Annualized Return)': cagr,
        'Max Drawdown': max_drawdown,
        'Sharpe Ratio': sharpe_ratio,
        'Sortino Ratio': sortino_ratio,
        'Rolling 30-Day Volatility': rolling_volatility
    }

    return stats

def make_trade_decision(stats, balance, current_price):
    decision = "HOLD"  # Default decision
    reasons = []

    # Thresholds for decision-making
    CAGR_THRESHOLD = 0.1  # 10% growth = bullish
    MDD_THRESHOLD = -0.3  # -30% drawdown = risk level
    SHARPE_THRESHOLD = 1.0
    SORTINO_THRESHOLD = 1.0
    VOLATILITY_THRESHOLD = 0.2  # 20% is high volatility
    BUY_ZONE = stats["25th Percentile"]
    SELL_ZONE = stats["75th Percentile"]

    # Extracting values
    cagr = stats.get("CAGR (Annualized Return)", 0)
    mdd = stats.get("Max Drawdown", 0)
    sharpe = stats.get("Sharpe Ratio", 0)
    sortino = stats.get("Sortino Ratio", 0)
    rolling_vol = stats.get("Rolling 30-Day Volatility", 0)
    
    # BUY Criteria
    if cagr > CAGR_THRESHOLD and current_price < BUY_ZONE:
        decision = "BUY"
        reasons.append(f"Coin shows {cagr:.2%} annual growth and is trading near a historical low ({current_price} < {BUY_ZONE}).")

    elif mdd < MDD_THRESHOLD and current_price < BUY_ZONE:
        decision = "BUY"
        reasons.append(f"Coin has suffered a {mdd:.2%} max drawdown, indicating a potential dip-buying opportunity.")

    elif sharpe > SHARPE_THRESHOLD and sortino > SORTINO_THRESHOLD and rolling_vol < VOLATILITY_THRESHOLD:
        decision = "BUY"
        reasons.append(f"Coin has strong risk-adjusted returns (Sharpe {sharpe:.2f}, Sortino {sortino:.2f}) and stable volatility.")

    # SELL Criteria
    elif current_price > SELL_ZONE and balance > 0.5:  # Sell only if user holds Coin
        decision = "SELL"
        reasons.append(f"Coin price ({current_price}) is near the high range ({SELL_ZONE}). Selling now could lock in profits.")

    elif sharpe < 0.5 and sortino < 0.5:
        decision = "SELL"
        reasons.append(f"Coin has poor risk-adjusted returns (Sharpe {sharpe:.2f}, Sortino {sortino:.2f}), indicating potential downside risk.")

    elif rolling_vol > VOLATILITY_THRESHOLD:
        decision = "SELL"
        reasons.append(f"Coin is highly volatile ({rolling_vol:.2%}), suggesting a risky environment for holding.")

    # HOLD Criteria
    else:
        reasons.append("Coin is trading within a stable range, and no strong buy/sell signals are present.")

    # Include Coin balance in reasoning
    reasons.append(f"Your Coin balance: {balance:.4f} Coin.")

    return decision, reasons

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Trade Decision System")
    parser.add_argument("--coin", type=str, required=True, help="Your coin")
    parser.add_argument("--coin_balance", type=float, required=True, help="Your holdings")
    parser.add_argument("--current_price", type=float, required=True, help="Current market price")

    args = parser.parse_args()


    df = fetch_data(args.coin)
    stats = analyze_data(df)

    # Print results in tabular format
    print(f"\nCoin ({args.coin}/USDT) Advanced Statistical Analysis:\n")
    print(tabulate(stats.items(), headers=["Metric", "Value"], tablefmt="pretty"))

    balance = 1.5  # User's Coin holdings
    current_price = 1950  # Coin current market price

    decision, reasons = make_trade_decision(stats, args.coin_balance, args.current_price)
    print(f"Decision: {decision}")
    print("Reasons:")
    for reason in reasons:
        print(f"- {reason}")