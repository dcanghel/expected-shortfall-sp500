import matplotlib.pyplot as plt

def plot_returns_with_var_cvar(returns, var, cvar):
    plt.figure(figsize=(10, 6))
    plt.hist(returns, bins=100, color='lightblue', edgecolor='black')
    plt.axvline(var, color='red', linestyle='dashed', linewidth=2, label=f'VaR 95% = {var:.2%}')
    plt.axvline(cvar, color='green', linestyle='dashed', linewidth=2, label=f'CVaR 95% = {cvar:.2%}')
    plt.title('S&P 500 Daily Returns (2021–2025) with VaR and CVaR at 95%')
    plt.xlabel('Daily Return')
    plt.ylabel('Frequency')
    plt.legend()
    plt.grid(True)
    plt.show()
