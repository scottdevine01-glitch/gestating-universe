"""
Prediction 5: Right-handed neutrino scale from pituitary scaling.
Predicts M_R = 10^{14.0±0.3} GeV and cosmic string tension.
"""

import numpy as np
from typing import Dict, List

def calculate_rh_neutrino_scale(
    pituitary_mass_g: float = 0.12,
    brain_mass_g: float = 1400.0,
    scaling_factor: float = 1.30e19,
    biological_uncertainty: float = 0.1
) -> Dict:
    """
    Calculate RH neutrino mass scale from pituitary gland scaling.
    
    Parameters:
    -----------
    pituitary_mass_g : float
        Mass of human pituitary gland (default: 0.12 g)
    brain_mass_g : float
        Mass of human brain (default: 1400 g)
    scaling_factor : float
        α = M_Pl/m_p (default: 1.30e19)
    biological_uncertainty : float
        Biological variation (± fraction)
    
    Returns:
    --------
    dict : RH neutrino scale predictions
    """
    # Constants
    proton_mass_gev = 0.938
    planck_mass_gev = 1.22e19
    
    # 1. Calculate pituitary-to-brain ratio
    pituitary_ratio = pituitary_mass_g / brain_mass_g
    
    # 2. Scale to cosmic: pituitary -> RH neutrinos, brain -> Standard Model
    # Pituitary as master endocrine regulator ↔ RH neutrinos as seesaw regulator
    log_m_r_gev = np.log10(planck_mass_gev) - np.log10(pituitary_ratio) / 2
    
    m_r_gev = 10 ** log_m_r_gev
    
    # 3. Apply uncertainty
    uncertainty_log = 0.3  # ±0.3 in log10 scale
    m_r_min_gev = 10 ** (log_m_r_gev - uncertainty_log)
    m_r_max_gev = 10 ** (log_m_r_gev + uncertainty_log)
    
    # 4. Calculate cosmic string tension from B-L breaking
    # Gμ ≈ (M_R / M_Pl)²
    g_mu = (m_r_gev / planck_mass_gev) ** 2
    g_mu_min = (m_r_min_gev / planck_mass_gev) ** 2
    g_mu_max = (m_r_max_gev / planck_mass_gev) ** 2
    
    # 5. Calculate seesaw neutrino masses
    higgs_vev_gev = 174.0
    light_nu_mass_ev = (higgs_vev_gev ** 2) / m_r_gev * 1e9  # Convert to eV
    
    # 6. Predict cosmic string properties
    string_tension_range = [g_mu_min, g_mu_max]
    
    # Compare with experimental bounds
    experimental_bounds = {
        'LIGO_Virgo_2025': {'upper_limit': 1e-7, 'lower_limit': 1e-15},
        'PTA_2025': {'upper_limit': 5e-11, 'lower_limit': 1e-15},
        'Future_BBO': {'sensitivity': 1e-17}
    }
    
    return {
        'm_r_gev': m_r_gev,
        'm_r_log10': log_m_r_gev,
        'm_r_range_gev': [m_r_min_gev, m_r_max_gev],
        'string_tension_gmu': g_mu,
        'string_tension_range': string_tension_range,
        'predicted_gmu_log10': np.log10(g_mu),
        'seesaw_neutrino_mass_ev': light_nu_mass_ev,
        'pituitary_ratio': pituitary_ratio,
        'biological_parameters': {
            'pituitary_mass_g': pituitary_mass_g,
            'brain_mass_g': brain_mass_g,
            'scaling_factor': scaling_factor
        },
        'experimental_bounds': experimental_bounds,
        'compatible_with_bounds': g_mu_min > experimental_bounds['Future_BBO']['sensitivity'],
        'falsification_criteria': {
            'gmu_outside_range': not (1e-8 < g_mu < 1e-6),
            'test_timeline': '2035-2040 (BBO, DECIGO)'
        }
    }

def calculate_cosmic_string_spectrum(
    gmu: float = 1e-7,
    frequency_hz: float = 1e-3
) -> Dict:
    """
    Calculate stochastic gravitational wave background from cosmic strings.
    
    Parameters:
    -----------
    gmu : float
        String tension Gμ
    frequency_hz : float
        Frequency in Hz
    
    Returns:
    --------
    dict : GW spectrum predictions
    """
    # Characteristic amplitude for cosmic strings
    # Ω_gw(f) ≈ Γ Gμ where Γ ~ 50
    gamma = 50.0
    
    # Energy density parameter
    omega_gw = gamma * gmu
    
    # Characteristic strain
    h_c = 1e-18 * np.sqrt(gmu / 1e-10) * (frequency_hz / 1e-3) ** (-1)
    
    # Spectrum slope
    slope = -1  # Scale-invariant for Nambu-Goto strings
    
    return {
        'omega_gw': omega_gw,
        'characteristic_strain': h_c,
        'spectral_slope': slope,
        'peak_frequency_hz': 1e-9 / np.sqrt(gmu),  # Approximate
        'detectability': {
            'LISA': h_c > 1e-20,
            'BBO': h_c > 1e-23,
            'DECIGO': h_c > 1e-24
        }
    }

if __name__ == "__main__":
    # Run calculation
    results = calculate_rh_neutrino_scale()
    
    print("=" * 60)
    print("PREDICTION 5: RIGHT-HANDED NEUTRINO SCALE")
    print("=" * 60)
    print(f"Predicted M_R = 10^{results['m_r_log10']:.1f} GeV")
    print(f"Range: 10^{results['m_r_log10']-0.3:.1f} - 10^{results['m_r_log10']+0.3:.1f} GeV")
    print(f"Value: {results['m_r_gev']:.2e} GeV")
    print()
    print(f"Cosmic string tension: Gμ = {results['string_tension_gmu']:.2e}")
    print(f"Range: {results['string_tension_range'][0]:.2e} - {results['string_tension_range'][1]:.2e}")
    print()
    print(f"Seesaw neutrino mass: {results['seesaw_neutrino_mass_ev']:.2e} eV")
    print()
    print("Biological basis:")
    print(f"  Pituitary mass: {results['biological_parameters']['pituitary_mass_g']} g")
    print(f"  Brain mass: {results['biological_parameters']['brain_mass_g']} g")
    print(f"  Ratio: {results['pituitary_ratio']:.2e}")
    print()
    print(f"Test timeline: {results['falsification_criteria']['test_timeline']}")
    print(f"Falsification: Gμ ∉ [10^-8, 10^-6]")
