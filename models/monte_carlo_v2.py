"""Basketball Prediction Engine v2.0"""
import numpy as np
import pandas as pd

def simulate_game(team_a, team_b, n_sims=100000):
    results = []
    for _ in range(n_sims):
        score_a = np.random.normal(team_a['avg'], team_a['std'])
        score_b = np.random.normal(team_b['avg'], team_b['std'])
        score_b += np.random.uniform(3, 6)  # home court
        results.append({'a': score_a, 'b': score_b, 'a_wins': score_a > score_b})
    return pd.DataFrame(results)

print("Model v2.0 - Ready")
