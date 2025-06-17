import numpy as np

def calculate_var_cvar(returns, confidence=0.95):
    var = np.percentile(returns, (1 - confidence) * 100)
    cvar = returns[returns < var].mean()
    return var, cvar
