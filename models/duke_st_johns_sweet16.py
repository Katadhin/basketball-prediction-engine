#!/usr/bin/env python3
"""
Duke vs St. John's - Sweet 16 (East Region)
Monte Carlo Prediction Model v2.3
"The Pitino Revenge Game Edition"

New in v2.3:
- Momentum from buzzer-beater wins
- Legendary coach motivation factor (Pitino revenge narrative)
- Tournament-tested depth vs portal-built chemistry
- Injury context (Foster out, Ngongba limited)
- Sweet 16 intensity scaling
"""

import numpy as np
from datetime import datetime

np.random.seed(42)

# ============================================================================
# TEAM STATISTICS (Season + Tournament)
# ============================================================================

DUKE_STATS = {
    'ppg': 83.2,
    'oppg': 63.8,
    'pace': 71.2,
    'off_rating': 120.3,
    'def_rating': 92.1,
    'three_pt_pct': 0.330,  # Without Foster (structural issue)
    'ft_pct': 0.742,
    'reb_margin': 8.4,
    'turnover_rate': 0.142,
    'record': (34, 2),
    'kenpom_rank': 1,
    'tournament_performance': {
        'siena': 'Nearly lost (71-65), down 11 at half',
        'tcu': 'Crushed (81-58), tied 44-44 then kill shot',
    },
    'injuries': {
        'foster': 'OUT (fractured foot, "outside chance" = no)',
        'ngongba': 'LIMITED (13 min vs TCU, +20, will play more)'
    }
}

ST_JOHNS_STATS = {
    'ppg': 79.8,
    'oppg': 68.3,
    'pace': 68.9,
    'off_rating': 116.7,
    'def_rating': 98.2,
    'three_pt_pct': 0.348,
    'ft_pct': 0.698,  # WEAKNESS (6-11 vs Kansas)
    'reb_margin': 4.2,
    'turnover_rate': 0.129,
    'forcing_turnovers': 19.0,  # Force 19 TOs per game (elite pressure)
    'record': (30, 6),
    'kenpom_rank': 12,
    'tournament_performance': {
        'uni': 'Blowout (79-53)',
        'kansas': 'Buzzer beater (67-65), Darling layup at horn'
    },
    'coach': {
        'name': 'Rick Pitino',
        'age': 73,
        'career_wins': 913,
        'final_fours': 7,
        'titles': 2,
        'motivation': 'Christian Laettner revenge (Duke 1992 East Regional Final)'
    }
}

# ============================================================================
# CONTEXT FACTORS
# ============================================================================

# The Pitino Revenge Narrative
PITINO_CONTEXT = {
    'christian_laettner_game': '1992 East Regional Final, Duke won on buzzer beater',
    'pitino_quote': '"I\'m hoping we can get Duke at the buzzer next to make up for that Christian Laettner shot"',
    'revenge_motivation': 1.04,  # Pitino wants this badly
    'sweet_16_drought': '27 years (first since 1999)',
    'big_moment_experience': 1.03,  # Pitino in 25th NCAA Tournament
}

# The Ejiofor Revenge Game
EJIOFOR_REVENGE = {
    'just_beat_kansas': 1.06,  # Beat the team that didn't believe in him
    'big_east_poy_validation': 1.04,  # Proving everyone wrong
    'buzzer_beater_confidence': 1.03,  # Just executed in clutch
    'mission_mode': 1.03,  # Validating entire career arc
}

# Momentum Factors
MOMENTUM = {
    'st_johns_buzzer_beater': 1.04,  # Just hit game-winner vs Kansas
    'duke_dominance_tcu': 1.03,  # Crushed TCU in 2nd half
    'st_johns_win_streak': 1.03,  # Won 21 of last 22
    'duke_win_streak': 1.02,  # Won 13 straight
}

# Talent vs Chemistry
TALENT_VS_CHEMISTRY = {
    'duke_talent_edge': 1.22,  # Boozer twins are generational (top 5 NBA picks)
    'st_johns_portal_chemistry': 0.98,  # 8 new players, year 1 together
    'duke_season_together': 1.04,  # Core has played all year
    'st_johns_pitino_system': 1.03,  # Elite coaching + veterans bought in
}

# Tournament Context
SWEET_16_FACTORS = {
    'intensity_multiplier': 1.04,  # Everyone plays harder
    'depth_matters_more': 1.03,  # Duke's 7-man rotation is a problem
    'st_johns_pressure_defense': 1.05,  # Force 19 TOs/game
    'duke_turnover_vulnerability': 0.97,  # Without Foster (primary ball handler)
}

# Foster/Ngongba Impact
INJURY_IMPACT = {
    'foster_out': 0.94,  # No primary ball handler vs pressure
    'ngongba_limited': 0.98,  # Will play ~20 min (up from 13)
    'st_johns_no_injuries': 1.00,  # Full healthy roster
}

# Coaching Edge
COACHING = {
    'pitino_tournament_experience': 1.03,  # 55-22 NCAA record (.714)
    'scheyer_tournament_experience': 0.99,  # Year 3 as HC, learning
    'pitino_adjustments': 1.02,  # Known for in-game changes
}

# X-Factors
X_FACTORS = {
    'st_johns_free_throw_weakness': 0.98,  # Shot 6-11 vs Kansas (55%)
    'duke_three_point_regression': 0.97,  # 33% without Foster
    'st_johns_turnover_creation': 1.04,  # Elite at forcing mistakes
    'duke_size_advantage': 1.05,  # Boozer twins + Ngongba vs smaller St. John's
}

# ============================================================================
# MONTE CARLO SIMULATION
# ============================================================================

def simulate_game(n_sims=50000):
    """
    Run Monte Carlo simulation for Duke vs St. John's
    
    Key variables:
    - Pitino revenge motivation
    - Buzzer-beater momentum
    - Duke talent vs St. John's pressure defense
    - Foster out / Ngongba limited
    - Sweet 16 intensity
    """
    
    duke_scores = []
    st_johns_scores = []
    
    for _ in range(n_sims):
        # Base pace (St. John's likes to slow it, Duke wants up-tempo)
        base_pace = (DUKE_STATS['pace'] + ST_JOHNS_STATS['pace']) / 2
        pace_variance = np.random.normal(base_pace, 3.2)
        possessions = max(58, min(72, int(pace_variance)))
        
        # Duke scoring
        duke_base = DUKE_STATS['ppg']
        
        # Apply all Duke adjustments
        duke_talent = TALENT_VS_CHEMISTRY['duke_talent_edge']
        duke_momentum = MOMENTUM['duke_dominance_tcu'] * MOMENTUM['duke_win_streak']
        duke_injuries = INJURY_IMPACT['foster_out'] * INJURY_IMPACT['ngongba_limited']
        duke_tournament = SWEET_16_FACTORS['intensity_multiplier']
        duke_pressure_defense = SWEET_16_FACTORS['duke_turnover_vulnerability']
        duke_shooting = X_FACTORS['duke_three_point_regression']
        duke_size = X_FACTORS['duke_size_advantage']
        
        duke_total_adj = (duke_talent * duke_momentum * duke_injuries * 
                         duke_tournament * duke_pressure_defense * 
                         duke_shooting * duke_size)
        
        # Cap Duke's total adjustment (prevent runaway)
        duke_total_adj = min(duke_total_adj, 1.25)  # Max 25% boost
        duke_total_adj = max(duke_total_adj, 0.80)  # Max 20% penalty
        
        # Shooting variance (key uncertainty)
        duke_three_variance = np.random.normal(DUKE_STATS['three_pt_pct'], 0.07)
        duke_three_variance = max(0.24, min(0.40, duke_three_variance))
        
        duke_score = np.random.normal(
            duke_base * duke_total_adj * (possessions / DUKE_STATS['pace']),
            7.8
        )
        
        # St. John's pressure defense (force 19 TOs/game, elite)
        # But Duke is disciplined (low turnover rate)
        st_johns_defensive_pressure = 0.96  # Some impact but Duke handles it
        duke_score = duke_score * st_johns_defensive_pressure
        
        # St. John's scoring
        st_johns_base = ST_JOHNS_STATS['ppg']
        
        # Apply all St. John's adjustments
        st_johns_momentum = (MOMENTUM['st_johns_buzzer_beater'] * 
                            MOMENTUM['st_johns_win_streak'])
        st_johns_revenge = PITINO_CONTEXT['revenge_motivation']
        st_johns_experience = PITINO_CONTEXT['big_moment_experience']
        st_johns_ejiofor_revenge = (EJIOFOR_REVENGE['just_beat_kansas'] *
                                   EJIOFOR_REVENGE['big_east_poy_validation'] *
                                   EJIOFOR_REVENGE['buzzer_beater_confidence'] *
                                   EJIOFOR_REVENGE['mission_mode'])
        st_johns_coaching = (COACHING['pitino_tournament_experience'] * 
                            COACHING['pitino_adjustments'])
        st_johns_chemistry = TALENT_VS_CHEMISTRY['st_johns_portal_chemistry']
        st_johns_system = TALENT_VS_CHEMISTRY['st_johns_pitino_system']
        st_johns_pressure = X_FACTORS['st_johns_turnover_creation']
        st_johns_ft_weakness = X_FACTORS['st_johns_free_throw_weakness']
        
        st_johns_total_adj = (st_johns_momentum * st_johns_revenge * 
                             st_johns_experience * st_johns_ejiofor_revenge *
                             st_johns_coaching * st_johns_chemistry * 
                             st_johns_system * st_johns_pressure * 
                             st_johns_ft_weakness)
        
        # Cap St. John's total adjustment (prevent runaway)
        st_johns_total_adj = min(st_johns_total_adj, 1.25)  # Max 25% boost
        st_johns_total_adj = max(st_johns_total_adj, 0.80)  # Max 20% penalty
        
        st_johns_score = np.random.normal(
            st_johns_base * st_johns_total_adj * (possessions / ST_JOHNS_STATS['pace']),
            7.2
        )
        
        # CRITICAL: Duke's elite defense (#2 in country)
        # St. John's averaging 79.8 PPG, but Duke holds teams to 63.8 PPG
        # Apply defensive resistance (Duke makes it harder to score)
        duke_defensive_resistance = 0.88  # Duke's elite defense
        st_johns_score = st_johns_score * duke_defensive_resistance
        
        duke_scores.append(duke_score)
        st_johns_scores.append(st_johns_score)
    
    return np.array(duke_scores), np.array(st_johns_scores)

# ============================================================================
# RUN SIMULATION
# ============================================================================

duke_scores, st_johns_scores = simulate_game()

duke_win_pct = (duke_scores > st_johns_scores).mean() * 100
duke_avg = duke_scores.mean()
st_johns_avg = st_johns_scores.mean()
margin = duke_avg - st_johns_avg

# Close game probability
close_games = np.abs(duke_scores - st_johns_scores) <= 5
close_pct = close_games.mean() * 100

# Duke covers probability (spread is -7)
duke_covers = (duke_scores - st_johns_scores) > 7
duke_covers_pct = duke_covers.mean() * 100

print("=" * 80)
print("DUKE vs ST. JOHN'S - SWEET 16 (EAST REGION)")
print("Monte Carlo Prediction Model v2.3")
print('"The Pitino Revenge Game Edition"')
print("=" * 80)
print()

print("GAME INFO:")
print(f"  Date: Friday, March 27, 2026")
print(f"  Location: Capital One Arena, Washington DC")
print(f"  Time: 7:10 PM ET (CBS)")
print()

print("THE NARRATIVE:")
print("  Rick Pitino: 'I'm hoping we can get Duke at the buzzer next")
print("              to make up for that Christian Laettner shot'")
print("  Context: 1992 East Regional Final, Duke beat Pitino's Kentucky on buzzer beater")
print()
print("  Zuby Ejiofor: Big East POY who transferred from KANSAS")
print("  • Just BEAT Kansas 67-65 on buzzer beater (18 pts, 9 reb)")
print("  • Revenge game: Bill Self recruited over him (Hunter Dickinson)")
print("  • His dad: '100% he wants to prove Coach Self made a mistake'")
print("  • On a MISSION to validate his entire career")
print()
print("  St. John's: First Sweet 16 in 27 years (since 1999)")
print("  Momentum: Won 21 of last 22 games")
print()

print("INJURY CONTEXT:")
print("  Duke:")
print("    • Caleb Foster: OUT ('outside chance' = he's not playing)")
print("    • Patrick Ngongba: LIMITED (~20 min, was +20 in 13 min vs TCU)")
print("  St. John's:")
print("    • Full healthy roster")
print()

print("=" * 80)
print("PREDICTION")
print("=" * 80)
print()

print(f"Duke {duke_avg:.0f}, St. John's {st_johns_avg:.0f}")
print(f"Margin: Duke by {margin:.1f}")
print(f"Duke Win Probability: {duke_win_pct:.1f}%")
print()

print("KEY PROBABILITIES:")
print(f"  Games decided by ≤5 pts: {close_pct:.1f}%")
print(f"  Duke covers -7 spread: {duke_covers_pct:.1f}%")
print()

print("=" * 80)
print("MARKET COMPARISON")
print("=" * 80)
print()

print("Consensus Line:")
print("  Spread: Duke -7")
print("  Moneyline: Duke -285 / St. John's +230")
print("  Total: 141.5")
print("  Implied Duke Win %: ~74%")
print()

print("Model vs Market:")
print(f"  Model Duke Win %: {duke_win_pct:.1f}%")
print("  Market Duke Win %: 74%")
print(f"  Difference: {duke_win_pct - 74:.1f} percentage points")
print()

print(f"  Model Margin: Duke by {margin:.1f}")
print("  Market Spread: Duke by 7")
print(f"  Difference: {abs(margin - 7):.1f} points")
print()

if duke_covers_pct < 50:
    print("BETTING EDGE:")
    print(f"  St. John's +7 has VALUE (Duke covers only {duke_covers_pct:.1f}%)")
    print(f"  St. John's ML +230 is intriguing (model has them at {100-duke_win_pct:.1f}%)")
else:
    print("BETTING EDGE:")
    print(f"  Duke -7 is FAIR (Duke covers {duke_covers_pct:.1f}%)")

print()

print("=" * 80)
print("THE BREAKDOWN")
print("=" * 80)
print()

print("WHY DUKE WINS:")
print("  1. Talent gap is REAL (Boozer twins are NBA lottery picks)")
print("  2. Size advantage (Ngongba + Boozers vs smaller St. John's)")
print("  3. Duke crushed TCU 81-58 in 2nd half (confidence)")
print("  4. 13-game win streak")
print("  5. Elite defensive rating (92.1, #2 in country)")
print()

print("WHY ST. JOHN'S KEEPS IT CLOSE:")
print("  1. Pitino revenge motivation (34 years since Laettner)")
print("  2. Buzzer-beater momentum (just beat Kansas at the horn)")
print("  3. Elite pressure defense (force 19 TOs/game)")
print("  4. Duke without Foster = turnover vulnerable")
print("  5. Pitino tournament experience (55-22 record, .714%)")
print("  6. First Sweet 16 in 27 years (nothing to lose)")
print("  7. Won 21 of last 22 games")
print()

print("THE X-FACTORS:")
print("  1. Can Duke handle St. John's pressure without Foster?")
print("  2. Will St. John's make free throws? (Shot 6-11 vs Kansas)")
print("  3. How many minutes can Ngongba give Duke?")
print("  4. Does Pitino's revenge narrative fuel or pressure St. John's?")
print("  5. Can Duke shoot 33%+ from three without Foster?")
print()

print("=" * 80)
print("THE CALL")
print("=" * 80)
print()

print(f"PREDICTION: Duke {duke_avg:.0f}, St. John's {st_johns_avg:.0f}")
print(f"CONFIDENCE: Duke {duke_win_pct:.0f}%")
print()

if margin < 7:
    print("THE LINE:")
    print("  Duke wins but doesn't cover.")
    print("  St. John's +7 is the play.")
    print("  This will be CLOSE.")
else:
    print("THE LINE:")
    print("  Duke wins and covers.")
    print("  Duke -7 is fair.")

print()

print("THE STORYLINE:")
print("  Pitino wants revenge for Christian Laettner.")
print("  Duke has the talent.")
print("  St. John's has the momentum and the legend on the sideline.")
print("  This will be a BATTLE.")
print()

print("=" * 80)
print(f"Simulation completed: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}")
print("=" * 80)
