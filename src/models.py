def lotka_volterra(t, state, alpha, beta, gamma, delta):
    """Lotka-Volterra predator-prey equations."""
    x, y = state
    dxdt = alpha * x - beta * x * y
    dydt = -gamma * y + delta * x * y
    return [dxdt, dydt]

def logistic_hollingII(t, state, r, K, a, h, gamma, e):
    """Logistic prey growth with Holling Type II predation."""
    x, y = state
    dxdt = r * x * (1 - x / K) - (a * x / (1 + a * h * x)) * y
    dydt = -gamma * y + e * (a * x / (1 + a * h * x)) * y
    return [dxdt, dydt]
