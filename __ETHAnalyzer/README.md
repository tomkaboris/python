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
   git clone https://github.com/tomkaboris/python.git
   cd crypto-trading-decision
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Required Python Packages**
   - [ccxt](https://github.com/ccxt/ccxt) (Binance API for fetching market data)
   - pandas
   - numpy
   - tabulate
   - argparse

   To install them manually:
   ```bash
   pip install ccxt pandas numpy tabulate argparse
   ```

---

## 🏗 Usage

Run the script from the terminal by passing:
- `--coin` → Cryptocurrency symbol (e.g., BTC, ETH, ADA)
- `--coin_balance` → Your holdings (amount of coins you own)
- `--current_price` → Current market price of the coin

### 🔹 **Example 1: Running for Ethereum (ETH)**
```bash
python trade_decision.py --coin ETH --coin_balance 1.5 --current_price 1950
```

### 🔹 **Example 2: Running for Bitcoin (BTC)**
```bash
python trade_decision.py --coin BTC --coin_balance 2.0 --current_price 48000
```

### 🔹 **Example 3: Running for Solana (SOL)**
```bash
python trade_decision.py --coin SOL --coin_balance 5.0 --current_price 150
```

---

## 📊 Example Output

```plaintext
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

---

## 📌 Decision Logic (BUY, HOLD, or SELL?)
| **Metric**            | **BUY Signal** | **SELL Signal** | **HOLD Signal** |
|----------------------|--------------|--------------|--------------|
| **CAGR** (>10%)    | Strong growth | Declining (<0%) | Moderate growth (0-10%) |
| **Max Drawdown** (>30%) | Buy at dip | >50% (crashing) | Stable (<30%) |
| **Sharpe Ratio** (>1.0) | Good risk-adjusted return | <0.5 (too risky) | 0.5 - 1.0 (Neutral) |
| **Sortino Ratio** (>1.0) | Good downside risk return | <0.5 (high risk) | 0.5 - 1.0 (Neutral) |
| **Volatility** (<20%) | Stability | >20% (High risk) | Normal (10-20%) |
| **Current Price** | Below 25th percentile | Above 75th percentile | Between 25-75% |

---

## 🚀 Future Improvements
🔹 Add **real-time price tracking** with WebSockets  
🔹 Implement **machine learning** for price prediction  
🔹 Create a **dashboard using Streamlit** for visualization  

---

## 📜 License
This project is open-source under the **MIT License**.

---

## 💬 Contributing
If you want to contribute:
1. Fork the repo 🍴
2. Create a new branch 🛠
3. Make your changes and submit a PR ✨

---

## 💡 Author
📌 **Boris Tomka**  
📧 Email: tomkaboris@gmail.com  
🌐 GitHub: [yourusername](https://github.com/tomkaboris)  

---

### ⭐ **If you like this project, give it a star on GitHub!** ⭐

