# 📉 Expected Shortfall (CVaR) & VaR for S&P 500

This project calculates and visualizes 1-day 95% Value at Risk (VaR) and Conditional Value at Risk (CVaR) for the S&P 500 index (using SPY ETF) based on historical simulation with real data from the Tiingo API.

## 🔍 Overview
- 📈 **Data:** Daily adjusted closing prices of SPY from 2021–2025.
- 🎯 **Goal:** Estimate 1-day risk measures: VaR and CVaR (Expected Shortfall).
- 📊 **Output:** Histogram of returns with VaR and CVaR visualized.

## 📁 Project Structure
```
expected_shortfall_sp500/
│
├── notebooks/
│   └── es_var_sp500.ipynb       # Main notebook with full analysis
├── scripts/
│   └── (optional scripts)
├── plots/
│   └── (optional output plots)
└── README.md                    # This file
```

## 🚀 How to Use
1. Replace `YOUR_TIINGO_API_KEY` in the notebook with your actual API key.
2. Run in [Google Colab](https://colab.research.google.com/) or Jupyter.
3. View output in plots and printed risk levels.

## 📌 Requirements
```bash
pip install pandas matplotlib requests
```

## 📬 Contact
Feel free to use and adapt for job portfolio or academic use.
