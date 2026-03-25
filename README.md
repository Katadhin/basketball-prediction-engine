# Basketball Prediction Engine v2.3

**An experiment in rapid iterative model development**

## The Goal

This isn't about beating Vegas. It's about answering a question:

**Can rapid public iteration create better prediction models faster than traditional isolated development?**

## Current Record: 13-3 (81.25%)

**v2.3 Active: NCAA Tournament Sweet 16**

### NCAA Tournament 2026
| Game | Prediction | Actual | Result |
|------|-----------|--------|--------|
| Duke vs Siena (R64) | Duke win (Ngongba uncertainty) | Duke 71-65 | ✅ |
| Duke vs TCU (R32) | Duke by 13 (if Ngongba plays) | Duke 81-58 (+20 in 13 min) | ✅ |
| **Duke vs St. John's (S16)** | **Duke 94-88 (73%)** | **TBD - March 27** | **🔄** |

### ACC Tournament 2026 (v2.0-v2.1)
| Game | Prediction | Actual | Margin Error | Result |
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

**Record breakdown:**
- v1.0: 0-1 (0%)
- v2.0/v2.1: 8-2 (80%)
- v2.2/v2.3: 2-0 (100%)
- **Overall: 10-3 regular, 2-0 tournament**

---

## Current Focus: Duke vs St. John's Sweet 16

**Game:** #1 Duke (34-2) vs #5 St. John's (30-6)  
**When:** Friday, March 27, 2026, 7:10 PM ET  
**Where:** Capital One Arena, Washington DC

### Model Output (v2.3)

**Prediction:** Duke 94, St. John's 88 (Duke 73%)  
**Market Line:** Duke -6.5  
**Model vs Market:** Nearly identical

### The Critical Insight

**St. John's shooting performance:**
- When shooting ≥45%: **22-1 record**
- When shooting <45%: **5-4 record**

**Duke allows opponents:** **39% FG** (elite defense)

**The entire game comes down to:** Can Duke hold St. John's under 45% shooting?

### Model Factors (v2.3)

**Ejiofor Revenge Psychology:**
- Just beat Kansas (transferred from there): 1.06x
- Big East POY validation: 1.04x
- Buzzer-beater confidence: 1.03x
- Mission mode: 1.03x
- **Compound effect: 1.16x**

**Pitino Revenge:**
- 1992 Laettner revenge (34 years): 1.04x
- Tournament experience: 1.03x

**Defensive Adjustments (NEW in v2.3):**
- Duke elite defense on St. John's: 0.88x
- St. John's pressure on Duke: 0.96x

**Safety Caps:**
- Maximum adjustment: 1.25x
- Minimum adjustment: 0.80x

---

## Methodology Evolution

### v2.2 → v2.3 (NCAA Tournament - March 2026)

**The "Schrödinger's Ngongba" Breakthrough:**
- Quantified uncertainty as a psychological factor
- Model predicted Duke advantage if Ngongba played
- Result: Ngongba played 13 minutes, was +20, Duke won by 23

| Improvement | v2.2 | v2.3 |
|-------------|------|------|
| Psychology Factors | None | Revenge games, coaching narratives, momentum |
| Defensive Caps | None | 0.88x resistance on elite defenses |
| Adjustment Limits | None | Max 1.25x boost, min 0.80x penalty |
| Confidence Ceiling | 90% | 90% (maintained) |
| Player Narratives | Generic | Specific (Ejiofor transfer story, Pitino revenge) |

### v2.0 → v2.1 (ACC Tournament - March 2026)

**The UNC-Clemson Disaster:**
- Model gave UNC 99.9% chance to beat Clemson
- Final: Clemson 80, UNC 79
- **Catastrophically wrong**

| Fix | v2.0 | v2.1 |
|-----|------|------|
| Injury Impact | Fixed penalty (-6.0) | Scaled by replacement quality |
| Bench Depth | Not modeled | `bench_depth = team_bench_ppg - opp` |
| Confidence Ceiling | 99.9% | **Max 90%** |
| Recent H2H | Equal weight | Heavy if within 10 days |

### v1.0 → v2.0 (Regular Season - February 2026)

| Flaw | v1.0 | v2.0 |
|------|------|------|
| Foul Trouble | Only offensive stars | ALL key defenders |
| Defensive Floors | Hard cap at 58 pts | Soft suppression with variance |
| Late-Game | All possessions equal | ±5 pts variance final 5 min |
| Referees | Assumed neutral | 1.2x home FTA advantage |
| Recency | Season averages | Last 5 games weighted 2x |

---

## Repository Structure

```
basketball-prediction-engine/
├── models/              # Model code & autopsies
│   ├── monte_carlo_v2_3.py         (NCAA Tournament - Sweet 16)
│   ├── monte_carlo_v2_2.py         (NCAA Tournament - Round 1&2)
│   ├── monte_carlo_v2_1.py         (ACC Tournament)
│   └── unc_clemson_autopsy.md      (99.9% confidence failure)
├── predictions/         # Game predictions with results
│   ├── duke_st_johns_sweet16.md    (March 27 - Active)
│   ├── duke_tcu_round32.md         (March 21 - Validated)
│   └── march13_semifinals.md       (ACC Tournament)
├── articles/           # Long-form analysis
│   └── schrodingers_ngongba.md    (Hope is quantifiable)
└── README.md
```

---

## What Makes v2.3 Different

### 1. Psychology as Math
**Ejiofor revenge story:**
- Transferred from Kansas after freshman year
- Bill Self recruited Hunter Dickinson over him
- Dad rented U-Haul and moved him out during finals
- Just beat Kansas 67-65 on buzzer-beater (18 pts, 9 reb)
- Now faces Duke as Big East POY

**Quantified as:** 1.16x compound multiplier

### 2. Narrative + Numbers
**Pitino's revenge:**
- 1992 East Regional Final: Duke beat Kentucky on Laettner buzzer-beater
- 34 years later, Pitino faces Duke again
- Quote: "I'm hoping we can get Duke at the buzzer next"

**Quantified as:** 1.04x motivation factor

### 3. Defensive Reality Checks
**Problem:** Early v2.3 runs had St. John's scoring 100+ against Duke's #2 defense

**Solution:** 
- Duke defensive resistance: 0.88x on opponent scoring
- St. John's pressure: 0.96x on Duke scoring
- Adjustment caps to prevent runaway multiplication

---

## Key Learnings

### From 99.9% Confidence to Humility
**UNC-Clemson taught us:**
- Never exceed 90% confidence on tournament games
- Depth > talent when fatigue sets in
- Replacement quality matters more than star power
- System resilience beats individual brilliance

### From Hope to Math
**"Schrödinger's Ngongba" taught us:**
- Uncertainty has psychological value
- Hope changes decision-making
- Quantifying the unquantifiable is possible
- Narrative factors can be measured

### From Generic to Specific
**St. John's prediction taught us:**
- Generic "momentum" < specific revenge stories
- Shooting splits reveal hidden vulnerabilities
- Market alignment doesn't mean you're wrong
- Sometimes "I don't know" is the right answer

---

## What I'm NOT Claiming

❌ "This model beats Vegas"  
❌ "You should bet based on these predictions"  
❌ "v2.3 is now perfect"  
❌ "Psychology factors are scientifically validated"

## What I AM Claiming

✅ Rapid iteration beats slow perfection  
✅ Public failure creates better feedback loops  
✅ Transparent methodology > black boxes  
✅ **Narrative factors can be quantified**  
✅ **Defensive efficiency matters more than offense**  
✅ **Shooting percentage splits predict outcomes**

---

## Read More

**NCAA Tournament:**
- **[Duke vs St. John's Prediction](predictions/duke_st_johns_sweet16.md)** - Current active prediction
- **[Schrödinger's Ngongba](articles/schrodingers_ngongba.md)** - How we quantified hope
- **[Duke vs TCU Validation](predictions/duke_tcu_round32.md)** - Psychology model validated

**ACC Tournament:**
- **[UNC-Clemson Autopsy](models/unc_clemson_autopsy.md)** - How 99.9% became 100% wrong
- **[Model Evolution v1→v2.1](articles/model_evolution.md)** - Learning from disaster

---

## Contact & Projects

**John Andrews**  
Alex Lee Profesor of Business, Lenoir-Rhyne University  
Co-founder, Katadhin Consulting

### Related Projects
🏁 **[NASCAR Monte Carlo Predictor](https://github.com/Katadhin/nascar-monte-carlo)** - Race predictions with track-type adaptation  
🏢 **[Katadhin Consulting](https://katadhin.com)** - AI adoption & business transformation  

### Connect
💼 [LinkedIn](https://linkedin.com/in/johnandrews)  
🐦 Twitter: @johnhandrews  
📧 john@katadhin.com

---

## License

MIT - Use this methodology however you want. Credit appreciated but not required.

---

**Next Update:** After Duke vs St. John's (March 27, 2026, 7:10 PM ET)

*"The best models aren't the ones that start perfect. They're the ones that fail fast, diagnose honestly, and iterate publicly."*

---

### Topics
#MachineLearning #MonteCarlo #Basketball #NCAA #Duke #BuildInPublic #DataScience #PredictiveModeling #SportsAnalytics
