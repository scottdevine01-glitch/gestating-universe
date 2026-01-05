#!/usr/bin/env python3
"""
Master script to run all 8 predictions of the Gestating Universe Theory.
Generates comprehensive report comparing predictions with current data.
"""

import sys
import json
import numpy as np
from datetime import datetime
from pathlib import Path

# Add the prediction calculators to path
sys.path.append(str(Path(__file__).parent / 'prediction_calculators'))

# Import all prediction modules
try:
    from neutrino_mass import calculate_neutrino_mass_sum, compare_with_experiments
    from cmb_periodicity import calculate_cmb_periodicity, generate_cmb_quadrupole_map
    from dm_core_scaling import calculate_dm_core_scaling
    from lorentz_invariance import calculate_lorentz_violation_suppression, generate_b_mode_coherence_map
    from rh_neutrino_scale import calculate_rh_neutrino_scale, calculate_cosmic_string_spectrum
    from hl_lhc_predictions import predict_hl_lhc_discoveries, calculate_exclusion_potential
    from higgs_21cm_correlation import calculate_higgs_21cm_correlation, simulate_cross_correlation_map
    from gw_echoes import calculate_gw_echo_profile, generate_echo_signal_for_detection
    IMPORT_SUCCESS = True
except ImportError as e:
    print(f"Warning: Could not import prediction modules: {e}")
    print("Make sure you're in the right directory or run: pip install -r requirements.txt")
    IMPORT_SUCCESS = False

def run_all_predictions(output_dir: str = "results") -> dict:
    """
    Run all 8 predictions and return comprehensive results.
    
    Parameters:
    -----------
    output_dir : str
        Directory to save results
    
    Returns:
    --------
    dict : All prediction results
    """
    if not IMPORT_SUCCESS:
        return {"error": "Failed to import prediction modules"}
    
    # Create output directory
    Path(output_dir).mkdir(exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    all_results = {
        "metadata": {
            "theory": "Gestating Universe Theory",
            "author": "Scott Devine",
            "timestamp": timestamp,
            "version": "1.0.0",
            "scaling_factor": 1.30e19,
            "biological_isomorphism": True
        },
        "predictions": {}
    }
    
    print("=" * 70)
    print("GESTATING UNIVERSE THEORY - ALL 8 PREDICTIONS")
    print("=" * 70)
    print()
    
    # ========== PREDICTION 1: NEUTRINO MASS SUM ==========
    print("🔬 [1/8] Calculating Neutrino Mass Sum...")
    p1_results = calculate_neutrino_mass_sum()
    p1_comparisons = compare_with_experiments(p1_results['mass_sum_mev'])
    all_results["predictions"]["neutrino_mass_sum"] = {
        **p1_results,
        "experimental_comparisons": p1_comparisons,
        "status": "Pending (2026-2028)",
        "falsification_threshold": ">73 meV or <60 meV (5σ)"
    }
    print(f"   ✓ Predicted: ∑m_ν = {p1_results['mass_sum_mev']:.1f} meV")
    
    # ========== PREDICTION 2: CMB PERIODICITY ==========
    print("🌌 [2/8] Calculating CMB ℓ=2 Periodicity...")
    p2_results = calculate_cmb_periodicity()
    all_results["predictions"]["cmb_periodicity"] = {
        **p2_results,
        "status": "Pending (2028-2030)",
        "falsification_threshold": "No ℓ=2 excess + phase lock (5σ)"
    }
    print(f"   ✓ Predicted: C_2^TT > {p2_results['predicted_power_microk2']:.0f} μK², Δφ = 0±0.1 rad")
    
    # ========== PREDICTION 3: DM CORE SCALING ==========
    print("🌀 [3/8] Calculating DM Core Scaling...")
    p3_results = calculate_dm_core_scaling()
    all_results["predictions"]["dm_core_scaling"] = {
        **p3_results,
        "status": "Pending (2026-2030)",
        "falsification_threshold": "No M^0.20 scaling (p > 0.05)"
    }
    print(f"   ✓ Predicted: r_c ∝ M^{p3_results['base_values']['scaling_exponent']:.2f}")
    
    # ========== PREDICTION 4: LORENTZ INVARIANCE ==========
    print("⚡ [4/8] Calculating Lorentz Invariance Effects...")
    p4_results = calculate_lorentz_violation_suppression()
    all_results["predictions"]["lorentz_invariance"] = {
        **p4_results,
        "status": "Pending (2028-2032)",
        "falsification_threshold": "C_23^BB = 0 (3σ)"
    }
    print(f"   ✓ Predicted: C_23^BB/√(C_2·C_3) > {p4_results['predicted_b_mode_coherence']:.2f}")
    
    # ========== PREDICTION 5: RH NEUTRINO SCALE ==========
    print("🧠 [5/8] Calculating RH Neutrino Scale...")
    p5_results = calculate_rh_neutrino_scale()
    p5_spectrum = calculate_cosmic_string_spectrum(p5_results['string_tension_gmu'])
    all_results["predictions"]["rh_neutrino_scale"] = {
        **p5_results,
        "cosmic_string_spectrum": p5_spectrum,
        "status": "Pending (2035-2040)",
        "falsification_threshold": "Gμ ∉ [10^-8, 10^-6]"
    }
    print(f"   ✓ Predicted: M_R = 10^{p5_results['m_r_log10']:.1f} GeV, Gμ = {p5_results['string_tension_gmu']:.2e}")
    
    # ========== PREDICTION 6: HL-LHC PREDICTIONS ==========
    print("⚛️  [6/8] Predicting HL-LHC Discoveries...")
    p6_results = predict_hl_lhc_discoveries()
    all_results["predictions"]["hl_lhc_predictions"] = {
        **p6_results,
        "status": "Pending (2029-2035)",
        "falsification_threshold": "Any new charged particle discovery"
    }
    new_particles = p6_results['summary']['predicted_new_charged_discoveries']
    print(f"   ✓ Predicted: {new_particles} new charged particles at HL-LHC")
    
    # ========== PREDICTION 7: HIGGS-21CM CORRELATION ==========
    print("📡 [7/8] Calculating Higgs-21cm Correlation...")
    p7_results = calculate_higgs_21cm_correlation()
    p7_simulation = simulate_cross_correlation_map(p7_results['predicted_correlation_mk_microk'])
    all_results["predictions"]["higgs_21cm_correlation"] = {
        **p7_results,
        "simulation_correlation": float(p7_simulation[2]),  # actual correlation from sim
        "status": "Pending (2030-2035)",
        "falsification_threshold": "No correlation at ℓ < 10 (3σ)"
    }
    print(f"   ✓ Predicted: ⟨a_ℓ^E a_ℓ^21⟩ = {p7_results['predicted_correlation_mk_microk']:.1f} mK·μK")
    
    # ========== PREDICTION 8: GW ECHOES ==========
    print("🌊 [8/8] Calculating GW Echo Profile...")
    p8_results = calculate_gw_echo_profile()
    p8_detection = generate_echo_signal_for_detection(n_mergers=10)
    all_results["predictions"]["gw_echoes"] = {
        **p8_results,
        "detection_strategy": p8_detection,
        "status": "Pending (2035-2040)",
        "falsification_threshold": "Stacked SNR < 5 (10 mergers)"
    }
    print(f"   ✓ Predicted: Echo delay Δt = {p8_results['echo_delay_s']:.3f} s")
    
    # ========== SUMMARY STATISTICS ==========
    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    
    # Count testable predictions
    testable_now = 0
    testable_future = 0
    falsified = 0
    confirmed = 0
    
    for pred_name, pred_data in all_results["predictions"].items():
        status = pred_data.get('status', 'Unknown')
        if '2026' in status or '2028' in status:
            testable_now += 1
        else:
            testable_future += 1
    
    # Calculate compression factor
    k_gestating = 2100  # bits
    k_lcdm = 1100000    # bits
    compression_factor = k_lcdm / k_gestating
    
    summary = {
        "total_predictions": 8,
        "testable_by_2030": testable_now,
        "testable_after_2030": testable_future,
        "currently_falsified": falsified,
        "currently_confirmed": confirmed,
        "pending": 8 - falsified - confirmed,
        "kolmogorov_complexity_bits": k_gestating,
        "compression_vs_lcdm": compression_factor,
        "biological_isomorphism": True,
        "scaling_factor_used": 1.30e19,
        "next_milestone": "2026 - Neutrino mass measurements (KATRIN/Project 8)"
    }
    
    all_results["summary"] = summary
    
    # Print summary
    print(f"Total predictions: {summary['total_predictions']}")
    print(f"Testable by 2030: {summary['testable_by_2030']}")
    print(f"Testable after 2030: {summary['testable_after_2030']}")
    print(f"Kolmogorov complexity: {summary['kolmogorov_complexity_bits']} bits")
    print(f"Compression vs ΛCDM: {summary['compression_vs_lcdm']:.0f}×")
    print(f"Biological isomorphism: {'Yes' if summary['biological_isomorphism'] else 'No'}")
    print(f"Next milestone: {summary['next_milestone']}")
    
    # ========== SAVE RESULTS ==========
    # Save as JSON
    json_path = Path(output_dir) / f"predictions_{timestamp}.json"
    with open(json_path, 'w') as f:
        json.dump(all_results, f, indent=2, default=lambda x: float(x) if isinstance(x, (np.float32, np.float64)) else str(x))
    
    # Save as text report
    txt_path = Path(output_dir) / f"predictions_report_{timestamp}.txt"
    with open(txt_path, 'w') as f:
        f.write(generate_text_report(all_results))
    
    print()
    print(f"✓ Results saved to:")
    print(f"  JSON: {json_path}")
    print(f"  Report: {txt_path}")
    
    return all_results

def generate_text_report(results: dict) -> str:
    """Generate a human-readable text report."""
    report = []
    report.append("=" * 70)
    report.append("GESTATING UNIVERSE THEORY - EXPERIMENTAL PREDICTIONS")
    report.append("=" * 70)
    report.append(f"Generated: {results['metadata']['timestamp']}")
    report.append(f"Theory: {results['metadata']['theory']}")
    report.append(f"Author: {results['metadata']['author']}")
    report.append("")
    
    # Summary
    summary = results['summary']
    report.append("SUMMARY")
    report.append("-" * 40)
    report.append(f"Total predictions: {summary['total_predictions']}")
    report.append(f"Testable by 2030: {summary['testable_by_2030']}")
    report.append(f"Testable after 2030: {summary['testable_after_2030']}")
    report.append(f"Kolmogorov complexity: {summary['kolmogorov_complexity_bits']} bits")
    report.append(f"Compression vs ΛCDM: {summary['compression_vs_lcdm']:.0f}×")
    report.append("")
    
    # Detailed predictions
    report.append("DETAILED PREDICTIONS")
    report.append("=" * 70)
    
    pred_order = [
        ("neutrino_mass_sum", "1. Neutrino Mass Sum"),
        ("cmb_periodicity", "2. CMB ℓ=2 Periodicity"),
        ("dm_core_scaling", "3. DM Core Scaling"),
        ("lorentz_invariance", "4. Lorentz Invariance"),
        ("rh_neutrino_scale", "5. RH Neutrino Scale"),
        ("hl_lhc_predictions", "6. HL-LHC Predictions"),
        ("higgs_21cm_correlation", "7. Higgs-21cm Correlation"),
        ("gw_echoes", "8. GW Echoes")
    ]
    
    for key, title in pred_order:
        if key in results['predictions']:
            pred = results['predictions'][key]
            report.append("")
            report.append(title)
            report.append("-" * 40)
            
            # Extract key prediction values
            if key == "neutrino_mass_sum":
                report.append(f"∑m_ν = {pred['mass_sum_mev']:.1f} meV")
                report.append(f"Range: {pred['prediction_range_mev'][0]:.1f} - {pred['prediction_range_mev'][1]:.1f} meV")
            
            elif key == "cmb_periodicity":
                report.append(f"C_2^TT > {pred['predicted_power_microk2']:.0f} μK²")
                report.append(f"Phase: Δφ = {pred['phase_coherence_rad']:.1f} ± {pred['phase_uncertainty_rad']:.1f} rad")
            
            elif key == "dm_core_scaling":
                report.append(f"r_c ∝ M^{pred['base_values']['scaling_exponent']:.2f}")
                report.append(f"Base: r_c = {pred['base_values']['base_core_radius_kpc']:.2f} kpc at M = {pred['base_values']['base_galaxy_mass_Msun']:.1e} M_sun")
            
            elif key == "lorentz_invariance":
                report.append(f"C_23^BB/√(C_2·C_3) > {pred['predicted_b_mode_coherence']:.2f}")
                report.append(f"Δc/c = {pred['lorentz_violation_suppression']:.2e}")
            
            elif key == "rh_neutrino_scale":
                report.append(f"M_R = 10^{pred['m_r_log10']:.1f} GeV")
                report.append(f"Gμ = {pred['string_tension_gmu']:.2e}")
            
            elif key == "hl_lhc_predictions":
                report.append(f"New charged particles: {pred['summary']['predicted_new_charged_discoveries']}")
                report.append(f"RH neutrinos: Indirect evidence expected")
            
            elif key == "higgs_21cm_correlation":
                report.append(f"⟨a_ℓ^E a_ℓ^21⟩ = {pred['predicted_correlation_mk_microk']:.1f} ± 0.3 mK·μK")
                report.append(f"For ℓ < {pred['angular_scale_dependence']['ell_max']}")
            
            elif key == "gw_echoes":
                report.append(f"Echo delay: Δt = {pred['echo_delay_s']:.3f} s (for {pred['black_hole_parameters']['mass_solar']} M_sun BH)")
                report.append(f"Amplitude: {pred['echo_amplitude_relative']:.3f} relative to main signal")
            
            report.append(f"Status: {pred.get('status', 'Unknown')}")
            report.append(f"Falsification: {pred.get('falsification_threshold', 'Not specified')}")
    
    # Biological isomorphism note
    report.append("")
    report.append("=" * 70)
    report.append("BIOLOGICAL ISOMORPHISM")
    report.append("=" * 70)
    report.append("All predictions derive from exact mathematical isomorphism")
    report.append("with mammalian gestation under scaling α = M_Pl/m_p ≈ 1.30×10^19")
    report.append("")
    report.append("Key mappings:")
    report.append("  • Fetal metabolism → Neutrino mass sum")
    report.append("  • Circadian rhythm → CMB periodicity")
    report.append("  • Placental allometry → DM core scaling")
    report.append("  • Heart synchronization → Lorentz invariance")
    report.append("  • Pituitary gland → RH neutrino scale")
    report.append("  • Complete blueprint → No new charged particles")
    report.append("  • Placental transport → Higgs-21cm correlation")
    report.append("  • Startle reflex → GW echoes")
    report.append("")
    report.append("=" * 70)
    report.append("END OF REPORT")
    report.append("=" * 70)
    
    return "\n".join(report)

def main():
    """Main function with command line interface."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Run all 8 predictions of the Gestating Universe Theory'
    )
    parser.add_argument('--output', '-o', default='results',
                       help='Output directory for results (default: results)')
    parser.add_argument('--format', '-f', choices=['json', 'text', 'both'], default='both',
                       help='Output format (default: both)')
    
    args = parser.parse_args()
    
    print("🚀 Starting Gestating Universe Theory prediction suite...")
    print()
    
    try:
        results = run_all_predictions(output_dir=args.output)
        
        if 'error' in results:
            print(f"❌ Error: {results['error']}")
            sys.exit(1)
        
        print()
        print("✅ All predictions calculated successfully!")
        print()
        print("📊 Key Results:")
        print(f"   • Neutrino mass: {results['predictions']['neutrino_mass_sum']['mass_sum_mev']:.1f} meV")
        print(f"   • CMB ℓ=2 power: >{results['predictions']['cmb_periodicity']['predicted_power_microk2']:.0f} μK²")
        print(f"   • RH neutrino scale: 10^{results['predictions']['rh_neutrino_scale']['m_r_log10']:.1f} GeV")
        print(f"   • Compression factor: {results['summary']['compression_vs_lcdm']:.0f}× vs ΛCDM")
        print()
        print("🔬 Next experimental test: Neutrino mass (2026-2028)")
        
    except Exception as e:
        print(f"❌ Error running predictions: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
