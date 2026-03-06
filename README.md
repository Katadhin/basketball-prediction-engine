# Basketball Prediction Engine v2.0

**An experiment in rapid iterative model development**

## The Goal

This isn't about beating Vegas. It's about answering a question:

**Can rapid public iteration create better prediction models faster than traditional isolated development?**

## The Methodology

**Traditional approach:**
1. Build in isolation
2. Backtest extensively  
3. Launch "perfect"
4. Fail quietly

**This approach:**
1. Build quickly (1 week)
2. Predict publicly (immediate test)
3. Fail loudly (full autopsy)
4. Rebuild rapidly (72 hours)
5. Test again
6. Repeat

## Results Tracking

| Game | Prediction | Actual | Margin Error | Winner |
|------|-----------|--------|--------------|--------|
| Duke-UNC (Feb 7) | Duke by 7 (67.7%) | UNC by 3 | 10 pts | ❌ |
| Duke-VA (Feb 28) | Duke by 12 (83.7%) | Duke by 26 | 14 pts | ✅ |
| UNC-VT (Feb 28) | UNC by 2 (53.2%) | UNC by 7 | 5 pts | ✅ |
| UNC-Duke (Mar 7) | Duke by 8 (76%) | TBD | TBD | TBD |

**v2.0 Performance:** 2/2 winners (100%), 9.5 pt avg margin error  
**v1.0 Performance:** 0/1 winners (0%), 10 pt margin error

✅ **Model v2.0 is demonstrably better than v1.0**

## Key Improvements (v1.0 → v2.0)

| Flaw | v1.0 | v2.0 |
|------|------|------|
| **Foul Trouble** | Only modeled offensive stars | ALL key defenders |
| **Defensive Floors** | Hard cap at 58 pts (overfitting) | Soft suppression with variance |
| **Late-Game** | All possessions equal | ±5 pts variance final 5 min |
| **Referees** | Assumed neutral | 1.2x home FTA advantage |
| **Recency** | Season averages | Last 5 games weighted 2x |
| **Context** | None | Post-big-win fatigue |

## Current Test: Model vs Market

**UNC @ Duke (March 7, 2026)**

Three different probabilities:
- **Robinhood Prediction Market:** Duke 91%
- **Vegas Spread:** Duke -5.5 (~65% implied)
- **Model v2.0:** Duke 76% (Wilson OUT scenario)

**The divergence:** Market is 15-25 percentage points more bullish on Duke than the model.

See [predictions/duke_unc_march7.md](predictions/duke_unc_march7.md) for full analysis.

## Repository Structure
```
basketball-prediction-engine/
├── models/           # Model code (Monte Carlo simulations)
├── predictions/      # Game predictions with results
├── articles/         # Long-form writeups
└── images/           # Visualizations
```

## What I'm NOT Claiming

❌ "This model beats Vegas"  
❌ "You should bet based on these predictions"  
❌ "v2.0 is now perfect"  
❌ "I've solved sports prediction"

## What I AM Claiming

✅ Rapid iteration beats slow perfection  
✅ Public failure creates better feedback loops  
✅ Structural diagnosis > "bad luck" excuses  
✅ Testing beats theorizing  
✅ Transparent methodology > black boxes

## Read More

- [Duke-UNC Prediction (Mar 7)](predictions/duke_unc_march7.md) - Model vs Market analysis
- [Feb 28 Results](predictions/feb28_predictions.md) - v2.0's first test (2-2)
- [Model Methodology](articles/model_v2_experiment_post.md) - Full writeup

## License

MIT - Use this methodology however you want

## Author

Built in public by someone who believes showing your work > hiding your failures

#DataScience #MachineLearning #BuildInPublic #Methodology
