def lotka_volterra(t, state, alpha, beta, gamma, delta):
    """Lotka-Volterra predator-prey equations."""
    x, y = state
    dxdt = alpha * x - beta * x * y
    dydt = -gamma * y + delta * x * y
    return [dxdt, dydt]
