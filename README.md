# Basketball Prediction Engine v2.1
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

## Current Record: 8-3 (72.7%)

| Game | Prediction | Actual | Margin Error | Winner |
|------|-----------|--------|--------------|--------|
| Duke-UNC (Feb 7) | Duke by 7 (67.7%) | UNC by 3 | 10 pts | ❌ v1.0 |
| Duke-VA (Feb 28) | Duke by 12 (83.7%) | Duke by 26 | 14 pts | ✅ v2.0 |
| UNC-VT (Feb 28) | UNC by 2 (53.2%) | UNC by 7 | 5 pts | ✅ v2.0 |
| UNC@Duke (Mar 7) | Duke by 8 (76%) | Duke by 15 | 7 pts | ✅ v2.0 |
| NC State-Pitt (Mar 11) | NC State by 7 | NC State by 10 | 3 pts | ✅ v2.0 |
| Louisville-SMU (Mar 11) | Louisville by 4 | Louisville by 4 | 0 pts 🎯 | ✅ v2.0 |
| FSU-Cal (Mar 11) | Cal by 2 (53.8%) | FSU by 6 | 8 pts | ❌ v2.0 |
| Clemson-Wake (Mar 11) | Clemson by 5 | Clemson by 9 | 4 pts | ✅ v2.0 |
| Virginia-NC State (Mar 12) | Virginia by 9.4 | Virginia 81-74 | 2.4 pts | ✅ v2.0 |
| Miami-Louisville (Mar 12) | Miami by 15.3 | Miami 78-73 | 10.3 pts | ✅ v2.0 |
| Duke-FSU (Mar 12) | Duke by 10.2 | Duke 80-79 | 9.2 pts | ✅ v2.0 |
| **UNC-Clemson (Mar 12)** | **UNC by 20.4 (99.9%)** | **Clemson 80-79** | **21.4 pts** | **❌ v2.0** |

**v2.0 Final: 8-2 (80%)**  
**v2.1 Active: Tonight's semifinals**

## The Disaster That Built v2.1

**March 12, 2026:** Model gave UNC 99.9% chance to beat Clemson.  
**Final score:** Clemson 80, UNC 79.

Not just wrong. Catastrophically wrong.

### Root Causes (Full Autopsy: `models/unc_clemson_autopsy.md`)

1. **Over-penalized injury** → Carter Welling out (-6.0 too harsh)
2. **Ignored replacement quality** → Nick Davidson scored 17
3. **Missed bench depth** → Clemson bench 26, UNC 5
4. **Wrong fatigue logic** → Clemson shot 49% FG (not tired)
5. **Hubris** → 99.9% confidence on tournament game

**Pattern identified:** Model systematically over-indexes on star player injuries and undervalues replacement quality, team depth, and system resilience.

## Key Improvements

### v1.0 → v2.0 (Feb 7)
| Flaw | v1.0 | v2.0 |
|------|------|------|
| Foul Trouble | Only offensive stars | ALL key defenders |
| Defensive Floors | Hard cap at 58 pts | Soft suppression with variance |
| Late-Game | All possessions equal | ±5 pts variance final 5 min |
| Referees | Assumed neutral | 1.2x home FTA advantage |
| Recency | Season averages | Last 5 games weighted 2x |
| Context | None | Post-big-win fatigue |

### v2.0 → v2.1 (Mar 12)
| Flaw | v2.0 | v2.1 |
|------|------|------|
| Injury Impact | Fixed penalty (-6.0) | Scaled by replacement quality & depth |
| Bench Depth | Not modeled | `bench_depth_advantage = team_bench_ppg - opp_bench_ppg` |
| Fatigue | Blanket back-to-back | Context-aware (rotation depth × margin) |
| Confidence | Up to 99.9% | **Max 90%** on tournament games |
| Recent H2H | Weighted equally | Heavy weight if within 10 days |

## Current Test: ACC Semifinals (March 13)

**Virginia vs Miami - 7:00 PM ESPN2**  
Prediction: Virginia 84-76 (90%)

**Duke vs Clemson - 9:30 PM ESPN2**  
Prediction: Duke 87-86 (56% Duke, 44% Clemson) — **COIN FLIP**

The v2.1 test: Can the model respect Clemson's depth advantage over Duke's tired 7-man rotation?

See `predictions/march13_semifinals.md` for full analysis.

## Repository Structure

```
basketball-prediction-engine/
├── models/              # Model code & autopsies
│   ├── monte_carlo_v2_1.py
│   └── unc_clemson_autopsy.md
├── predictions/         # Game predictions with results
├── articles/           # Long-form writeups
└── images/             # Visualizations
```

## What I'm NOT Claiming

❌ "This model beats Vegas"  
❌ "You should bet based on these predictions"  
❌ "v2.1 is now perfect"  
❌ "I've solved sports prediction"

## What I AM Claiming

✅ Rapid iteration beats slow perfection  
✅ Public failure creates better feedback loops  
✅ Structural diagnosis > "bad luck" excuses  
✅ Testing beats theorizing  
✅ Transparent methodology > black boxes  
✅ **Depth beats talent when fatigue sets in**

## Read More

* **[UNC-Clemson Autopsy](models/unc_clemson_autopsy.md)** - How 99.9% confidence became 100% wrong
* **[Model Evolution Article](articles/model_evolution_v1_to_v2_1.md)** - From v1.0 to v2.1
* **[ACC Semifinals Predictions](predictions/march13_semifinals.md)** - Tonight's v2.1 test
* **[March 12 Quarterfinals Results](predictions/march12_quarterfinals.md)** - 3-1 with one disaster

## License

MIT - Use this methodology however you want

## Author

**John Andrews**  
Assistant Teaching Professor, Lenoir-Rhyne University  
Co-founder, Katadhin Consulting

## Related Projects

🏁 **[NASCAR Monte Carlo Predictor](https://github.com/Katadhin/nascar-monte-carlo)** - Adaptive racing predictions across track types  
🏢 **[Katadhin Consulting](https://katadhin.com)** - Business transformation & AI adoption  
📚 Teaching: Applied AI for Business @ Lenoir-Rhyne University

## Connect

💼 [LinkedIn](https://linkedin.com/in/johnandrews)  
📧 Email

---

**Next Update:** After tonight's semifinals (games at 7:00 PM & 9:30 PM EST)

*"The best models aren't the ones that start perfect. They're the ones that fail fast, diagnose honestly, and iterate publicly."*

#DataScience #MachineLearning #BuildInPublic #Methodology
