def lotka_volterra(t, y, alpha, beta, gamma, delta):
    prey, pred = y
    dydt = [alpha * prey - beta * prey * pred,
            delta * prey * pred - gamma * pred]
    return dydt
    
def logistic_hollingII(t, y, r, K, a, h, gamma, e):
    prey, pred = y
    predation_rate = (a * prey * pred) / (1 + a * h * prey)
    dydt = [
        r * prey * (1 - prey / K) - predation_rate,
        e * predation_rate - gamma * pred
    ]
    return dydt
