# UNC-CLEMSON PREDICTION AUTOPSY
## Model v2.0's Worst Miss Yet

**PREDICTION:** UNC 82, Clemson 61 (UNC 99.9%)
**ACTUAL:** Clemson 80, UNC 79 (Clemson wins)
**ERROR:** 21.4 point margin miss + WRONG WINNER

---

## WHAT THE MODEL THOUGHT:

### UNC Advantages (Net: +4.5):
- `caleb_wilson_still_out`: -5.0
- `double_bye_rest`: +2.5
- `henri_veesaar_interior`: +2.0
- `paint_advantage_no_welling`: +3.5 ⚠️
- `jarin_stevenson_rebounding`: +1.5
- `luka_bogavac_wildcard`: +1.0
- `quad_1_pressure`: -1.0

### Clemson Disadvantages (Net: -11.5):
- `carter_welling_out`: -6.0 ⚠️
- `rj_godfrey_variance`: -2.0
- `nick_davidson_replacement`: +1.0 ⚠️
- `played_last_night`: -2.5 ⚠️
- `paint_dominated_last_time`: -2.0
- `platoon_system_broken`: -1.5
- `tournament_desperation`: +1.5
- `familiarity_with_unc`: +1.0

**Total swing: 16 points in UNC's favor**

---

## WHAT ACTUALLY HAPPENED:

### The Nick Davidson Story:
**Model assumption:** Nick Davidson +1.0 ("solid but not Welling")
**Reality:** Nick Davidson was INCREDIBLE
- 17 points (second-leading scorer)
- Played starter minutes, no drop-off
- Hit clutch shots all game
- Model drastically undervalued him

**MISSED:** Davidson wasn't just "solid" — he was a STAR performance

---

### The Fatigue Myth:
**Model assumption:** Clemson `played_last_night`: -2.5 (tired legs)
**Reality:** Clemson looked FRESHER than UNC
- Shot 49% FG, 48% from 3 (elite efficiency)
- Bench outscored UNC's bench 26-5 (depth!)
- No visible fatigue whatsoever
- Led 61-46 at one point in 2nd half

**MISSED:** Back-to-back games don't automatically = tired if you have depth

---

### The Depth Disaster:
**Model assumption:** Clemson's `platoon_system_broken`: -1.5
**Reality:** Clemson's BENCH DOMINATED
- 26 bench points vs UNC's 5 (!!)
- SIX players in double figures
- Brad Brownell rotated effectively despite Welling loss
- UNC looked thin, not Clemson

**MISSED:** Clemson had MORE depth than UNC, not less

---

### The Paint Myth:
**Model assumption:** UNC `paint_advantage_no_welling`: +3.5
**Reality:** Clemson held their own inside
- Nick Davidson + RJ Godfrey handled the interior
- UNC didn't dominate the glass like expected
- Henri Veesaar had 28 but it took 28 shots (volume, not dominance)

**MISSED:** Welling's absence didn't crater Clemson's interior defense

---

### The UNC Caleb Wilson Hole:
**Model assumption:** UNC `caleb_wilson_still_out`: -5.0 (but still wins by 20)
**Reality:** UNC "looked outmatched without Caleb Wilson" (per reports)
- Only 5 bench points (catastrophic)
- Couldn't match Clemson's depth
- No answers when Clemson went on runs

**MISSED:** Wilson's absence was MORE devastating than modeled, not less

---

## THE FUNDAMENTAL ERRORS:

### 1. OVER-INDEXED ON WELLING'S ABSENCE
The model assumed:
- Clemson loses their anchor = paint domination for UNC
- Platoon system breaks = rotation disaster
- Fatigue from back-to-back = tired legs

**Reality:**
- Nick Davidson stepped up HUGE (17 pts)
- Depth was BETTER than UNC's (26-5 bench scoring)
- No visible fatigue (49% FG, 48% 3PT)

**Lesson:** Don't assume injury = automatic collapse. Need to account for:
- Quality of replacement player
- Team depth beyond the injured player
- Opponent's own weaknesses (UNC's thin bench)

---

### 2. UNDERVALUED CLEMSON'S BALANCED SCORING
**Model modifier:** `rj_godfrey_variance`: -2.0 (unreliable)

**Reality:** 
- RJ Godfrey: 11 pts, 8 rebs (solid, not spectacular)
- But SIX players scored 10+
- Didn't NEED Godfrey to go nuclear

**Missed:** Variance works both ways. Clemson's balance meant they didn't need one hero.

---

### 3. FATIGUE PENALTY TOO HARSH
**Model:** `played_last_night`: -2.5 for Clemson

**Context we ignored:**
- Clemson beat Wake Forest 71-62 (comfortable win, not exhausting)
- Deep rotation (rested starters throughout)
- UNC also looked tired despite double-bye (emotional letdown?)

**Lesson:** Back-to-back penalty should vary based on:
- How hard was yesterday's game?
- How deep is the rotation?
- What's the opponent's rest situation?

A team with 8-9 rotation players playing back-to-back might be BETTER than a thin 6-man team with rest.

---

### 4. PAINTED THE WRONG PICTURE
The narrative we built:
- "UNC fresh, Clemson exhausted"
- "UNC dominates paint, Clemson has no answer"
- "Clemson's system broken, UNC rolls"

**The reality:**
- Clemson had MORE depth and energy
- Paint was competitive
- Clemson's system adapted beautifully

**Lesson:** Beware of building a narrative first, then finding data to support it.

---

## WHAT WE SHOULD HAVE SEEN:

### Red Flags We Missed:

1. **UNC's bench was always thin** (not just vs Clemson)
   - Without Wilson, they had no depth
   - Clemson's 8-man rotation > UNC's 6-man rotation

2. **Clemson beat UNC 67-63 ten days ago**
   - With Welling: Clemson lost by 4
   - Without Welling: Clemson won by 1
   - **That's only a 5-point swing, not 20+**

3. **Nick Davidson's performance vs Wake Forest**
   - 8 pts, 7 rebs in 1st game without Welling
   - Not spectacular but capable
   - Should've been +2.0, not +1.0

4. **UNC's recent struggles**
   - Barely beat VT/Wake at home
   - Relying heavily on Veesaar heroics
   - Lost to Duke without Wilson

---

## CORRECTED MODIFIERS (RETROSPECTIVE):

### What they SHOULD have been:

**UNC:**
- `caleb_wilson_still_out`: -7.0 (not -5.0) — bigger hole than we thought
- `double_bye_rest`: +1.5 (not +2.5) — emotional letdown possible
- `paint_advantage_no_welling`: +1.5 (not +3.5) — Davidson competent
- `thin_bench_exposed`: -3.0 (NEW) — only 5 bench points

**Clemson:**
- `carter_welling_out`: -3.0 (not -6.0) — Davidson capable replacement
- `nick_davidson_steps_up`: +3.0 (not +1.0) — STAR performance
- `depth_advantage`: +3.0 (NEW) — 26-5 bench scoring
- `played_last_night`: -1.0 (not -2.5) — deep rotation, comfortable win
- `platoon_system_intact`: +1.5 (not -1.5) — Brownell adapted well
- `shot_lights_out`: +2.5 (NEW) — 49% FG, 48% 3PT

**Revised prediction:** UNC 76, Clemson 74 (UNC 62%)

Much closer to reality (Clemson 80-79).

---

## THE META-LESSON:

### We made the SAME mistake as Duke-UNC in February:

**February Duke-UNC:**
- Model overpenalized Duke for Wilson being out
- Predicted UNC by 8
- Duke won by 15
- Error: 23 points

**March UNC-Clemson:**
- Model overpenalized Clemson for Welling being out
- Predicted UNC by 20
- Clemson won by 1
- Error: 21 points

**PATTERN:** The model over-indexes on star player injuries and undervalues:
1. Replacement player quality
2. Team depth/system resilience
3. Opponent's own weaknesses

---

## FIXES FOR v2.1:

### 1. INJURY IMPACT SCALING:
Don't use fixed penalties. Use:
```python
injury_impact = base_penalty * (1 - replacement_quality) * (1 - team_depth_factor)
```

Example:
- Welling out, Davidson replaces (0.7 quality), Clemson deep (0.8 depth factor)
- Impact = -6.0 * (1 - 0.7) * (1 - 0.8) = -6.0 * 0.3 * 0.2 = -0.36

Not -6.0!

---

### 2. BENCH SCORING METRIC:
Add explicit bench strength modifier:
```python
'bench_depth_advantage': team_bench_ppg - opponent_bench_ppg
```

Clemson: ~20 bench ppg
UNC: ~8 bench ppg (without Wilson)
Modifier: +12 for Clemson? That's huge!

---

### 3. FATIGUE CONTEXT:
Back-to-back penalty should consider:
- Yesterday's margin (blowout = less tired)
- Rotation depth (9 players = less tired)
- Minutes played by starters

Clemson beat Wake 71-62 (9-pt win, rotated freely) = minimal fatigue

---

### 4. RECENT H2H WEIGHTING:
If teams played within 10 days, heavily weight that result:
- Clemson lost 67-63 WITH Welling
- Clemson won 80-79 WITHOUT Welling
- Delta: 5 points, not 20

Use that as a baseline, not season-long stats.

---

## THE UNCOMFORTABLE TRUTH:

**We got cocky.**

99.9% confidence on a tournament quarterfinal is INSANE hubris, especially when:
- They played 10 days ago (close game)
- Clemson has proven depth
- UNC is thin without Wilson
- Tournament basketball is chaotic

Should've been: **UNC 72-70 (65%)** — close game, slight UNC edge

Not: **UNC 82-61 (99.9%)** — blowout lock

---

## FINAL TAKEAWAY:

**Injuries don't automatically break teams.**

Good coaches adjust. Depth matters. Replacements can step up. Systems can adapt.

The model needs to:
1. Lower injury penalties
2. Increase replacement player valuations
3. Add bench depth metrics
4. Reduce overconfidence

**v2.0 record:** 6-2 (75%)
**v2.0 avg margin error:** Now ~8.5 pts (up from 2.7)

Time to build v2.1. 🔧
