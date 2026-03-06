# Basketball Prediction Engine v2.0

An experiment in rapid iterative model development.

## The Question

Can rapid public iteration create better prediction models faster than traditional isolated development?

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

**Next Test:** Duke revenge game + Wilson status uncertainty + Market at 91% Duke

## Methodology

Build → Predict → Fail → Diagnose → Rebuild → Test → Repeat

See `/predictions/feb28_predictions.md` for detailed analysis.# Basketball Prediction Engine v2.0

An experiment in rapid iterative model development.

## The Question

Can rapid public iteration create better prediction models faster than traditional isolated development?

## Results

| Game | Prediction | Actual | Margin Error | Winner |
|------|-----------|--------|--------------|--------|
| Duke-UNC (Feb 7) | Duke by 7 (67.7%) | UNC by 3 | 10 pts | ❌ |
| Duke-VA (Feb 28) | Duke by 12 (83.7%) | Duke by 26 | 14 pts | ✅ |
| UNC-VT (Feb 28) | UNC by 2 (53.2%) | UNC by 7 | 5 pts | ✅ |

**v2.0 Performance:** 2/2 winners (100%), 9.5 pt avg margin error
**v1.0 Performance:** 0/1 winners (0%), 10 pt margin error

✅ **Model v2.0 is demonstrably better than v1.0**

## Methodology

Build → Predict → Fail → Diagnose → Rebuild → Test → Repeat

See `/predictions/feb28_predictions.md` for detailed analysis.# Basketball Prediction Engine v2.0

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-brightgreen.svg)
![Accuracy](https://img.shields.io/badge/accuracy-testing-yellow.svg)

Monte Carlo prediction system for college basketball. Built in public as a rapid iteration experiment.

## The Experiment

**Question:** Can rapid public iteration create better prediction models faster than traditional isolated development?

**Approach:** Build → Predict → Fail → Diagnose → Rebuild → Test → Repeat

**Focus:** Duke vs UNC rivalry games (high-stakes, data-rich matchups)

---

## Current Results

| Date | Game | Prediction | Actual | Error | Status |
|------|------|-----------|--------|-------|--------|
| Feb 7 | Duke vs UNC | Duke by 7 | UNC by 3 | 10 pts | ❌ Miss |
| Feb 28 | Duke vs VA | Duke by 12 | TBD | TBD | ⏳ Pending |
| Feb 28 | UNC vs VT | UNC by 2 | TBD | TBD | ⏳ Pending |

**Record:** 0-1 (learning mode activated 🤖)

---

## How It Works

### Monte Carlo Simulation
Runs 10,000+ simulated games using:
- Historical team performance data
- Tempo adjustments (possessions per game)
- Home court advantage
- Recent form momentum
- Injury/roster impacts
- Defensive efficiency metrics

### Key Features (v2.0)
- **Possession-based modeling** (not just points per game)
- **Variance simulation** (accounts for hot/cold shooting)
- **Momentum factors** (winning streaks, recent performance)
- **Context awareness** (rivalry games, tournament pressure)
- **Rapid iteration** (rebuild after each miss)

### What Changed from v1.0
- ✅ Added tempo/possession modeling
- ✅ Improved defensive metrics weighting
- ✅ Home court advantage recalibrated
- ✅ Recent form integration (last 5 games)
- ❌ Still missed Duke-UNC by 10 pts (back to drawing board)

---

## Installation
```bash
# Clone the repository
git clone https://github.com/Katadhin/basketball-prediction-engine.git
cd basketball-prediction-engine

# Install dependencies
pip install -r requirements.txt

# Run prediction
python models/monte_carlo_v2.py
```

---

## Example Prediction Output
```
DUKE vs UNC PREDICTION
Simulations: 10,000
Date: February 28, 2026

Duke win probability: 67.3%
UNC win probability: 32.7%

Predicted Score:
Duke: 78
UNC: 71

Predicted Margin: Duke by 7
Confidence: Medium (rivalry game = high variance)
```

---

## Model Architecture
```
Input Data
  ↓
Historical Performance Metrics
  ↓
Tempo/Possession Adjustments
  ↓
Monte Carlo Simulation (10,000 runs)
  ↓
Aggregate Results
  ↓
Predicted Margin + Win Probability
```

---

## Why This Approach?

Traditional sports prediction models are built in isolation, tested privately, and released when "ready."

This project does the opposite:
- **Public predictions** before games
- **Immediate feedback** when wrong
- **Rapid iteration** based on failures
- **Transparent methodology** (see `/models`)

The hypothesis: Public accountability + rapid iteration = faster improvement than slow, private development.

---

## Roadmap

**Immediate (Feb-Mar 2026):**
- [ ] Fix Duke-UNC prediction error (missed by 10 pts)
- [ ] Test improved v2.0 on Feb 28 games
- [ ] Add tournament pressure modeling

**Next (Mar-Apr 2026):**
- [ ] Expand beyond Duke/UNC to ACC games
- [ ] Integrate real-time injury data
- [ ] Build bracket prediction engine for March Madness

**Future:**
- [ ] Multi-sport expansion (NFL, NASCAR already built)
- [ ] API for live game predictions
- [ ] Ensemble model (combine multiple approaches)

---

## Project Structure
```
basketball-prediction-engine/
├── models/
│   ├── monte_carlo_v1.py    # Original model (deprecated)
│   └── monte_carlo_v2.py    # Current model
├── predictions/
│   └── feb28_predictions.md # Latest picks
├── data/
│   └── team_stats.json      # Historical data
└── articles/
    └── why_i_missed_duke_unc.md
```

---

## Learn More

- 📊 [Full methodology writeup](#)
- 🏀 [Why I missed Duke-UNC by 10 points](#)
- 🤖 [Building in public: Lessons learned](#)

---

## Related Projects

- [NASCAR Monte Carlo Predictor](https://github.com/Katadhin/nascar-monte-carlo-predictor) - Adaptive racing predictions across track types

---

## License

MIT License - see [LICENSE](LICENSE) file for details

---

**Current Status:** Iterating rapidly. 0-1 record. Learning mode engaged. 🏀🤖

*"The best way to improve a model is to watch it fail in public."*# Basketball Prediction Engine v2.0
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-brightgreen.svg)

An experiment in rapid iterative model development.

## The Question

Can rapid public iteration create better prediction models faster than traditional isolated development?

## Results

| Game | Prediction | Actual | Error |
|------|-----------|--------|-------|
| Duke-UNC (Feb 7) | Duke by 7 | UNC by 3 | 10 pts ❌ |
| Duke-VA (Feb 28) | Duke by 12 | TBD | TBD |
| UNC-VT (Feb 28) | UNC by 2 | TBD | TBD |

## Methodology

Build → Predict → Fail → Diagnose → Rebuild → Test → Repeat

See `/articles` for full writeups.# Basketball Prediction Engine v2.0
