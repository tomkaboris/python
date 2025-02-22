# 🚀 Crypto Trading Decision System

This project is a **Crypto Trading Decision System** that fetches historical cryptocurrency data from **Binance**, performs statistical analysis using **NumPy & Pandas**, and suggests whether to **BUY, HOLD, or SELL** based on risk-adjusted returns, volatility, and price trends.

## 📌 Features
✅ Fetches **any cryptocurrency** historical data from Binance  
✅ Performs **statistical analysis** (Mean, Variance, Standard Deviation, Skewness, CAGR, etc.)  
✅ Calculates **risk-adjusted returns** (Sharpe Ratio, Sortino Ratio)  
✅ Detects **buy and sell zones** based on historical trends  
✅ Uses **argparse** for easy command-line input  

---

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/crypto-trading-decision.git
   cd crypto-trading-decision
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Required Python Packages**
- ccxt (Binance API for fetching market data)
- pandas
- numpy
- tabulate
- argparse

## 🏗 Usage
Run the script from the terminal by passing:
- --coin → Cryptocurrency symbol (e.g., BTC, ETH, ADA)
- --coin_balance → Your holdings (amount of coins you own)
- --current_price → Current market price of the coin

🔹 Example 1: Running for Ethereum (ETH)
```bash
python trade_decision.py --coin ETH --coin_balance 1.5 --current_price 1950
```
```bash
python trade_decision.py --coin BTC --coin_balance 2.0 --current_price 48000
```
```bash
python trade_decision.py --coin SOL --coin_balance 2.0 --current_price 48000
```

## Example output
```bash
Coin (ETH/USDT) Advanced Statistical Analysis:

+----------------------------+------------------+
| Metric                     | Value            |
+----------------------------+------------------+
| Mean Price                 | 2500.6543        |
| Standard Deviation         | 500.7891         |
| Variance                   | 250000.1234      |
| Minimum Price              | 1800.4523        |
| Maximum Price              | 3500.7896        |
| 25th Percentile            | 2200.3452        |
| 50th Percentile            | 2400.6789        |
| 75th Percentile            | 2800.6789        |
| Skewness                   | 0.1234           |
| Kurtosis                   | -0.6543          |
| Coefficient of Variation   | 0.2004           |
| CAGR (Annualized Return)   | 0.1243 (12.43%)  |
| Max Drawdown               | -0.3214 (-32.14%)|
| Sharpe Ratio               | 0.0423           |
| Sortino Ratio              | 0.0567           |
| Rolling 30-Day Volatility  | 0.1074 (10.74%)  |
+----------------------------+------------------+

Decision: BUY
Reasons:
- ETH shows 12.00% annual growth and is trading near a historical low (1950 < 2000).
- ETH has suffered a -35.00% max drawdown, indicating a potential dip-buying opportunity.
- Your Coin balance: 1.5000 ETH.
```