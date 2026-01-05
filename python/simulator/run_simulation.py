"""
Main simulation runner for Gestating Universe.
"""

import argparse
import json
from causal_set import CausalSet
from sm_dynamics import StandardModelOnCausalSet

def run_simulation(config: dict):
    """
    Run a complete simulation with given configuration.
    
    Parameters:
    -----------
    config : dict
        Simulation parameters
    """
    print("=" * 60)
    print("GESTATING UNIVERSE SIMULATION")
    print("=" * 60)
    
    # Extract parameters
    n_elements = config.get('n_elements', 1000)
    density = config.get('density', 0.1)
    n_steps = config.get('n_steps', 5)
    
    print(f"Creating causal set with {n_elements} elements...")
    causet = CausalSet(n_elements=n_elements, density=density)
    
    print(f"Initializing Standard Model fields...")
    sm = StandardModelOnCausalSet(causet)
    
    print(f"\nInitial Actions:")
    actions = sm.total_action()
    for key, value in actions.items():
        print(f"  {key}: {value:.4f}")
    
    print(f"\nEvolving for {n_steps} steps...")
    sm.evolve(steps=n_steps)
    
    print(f"\nFinal Actions:")
    actions = sm.total_action()
    for key, value in actions.items():
        print(f"  {key}: {value:.4f}")
    
    print("\n" + "=" * 60)
    print("Simulation complete!")
    print("=" * 60)

def main():
    parser = argparse.ArgumentParser(description='Run Gestating Universe simulation')
    parser.add_argument('--parameters', type=str, default='config/default.json',
                       help='Path to parameter JSON file')
    parser.add_argument('--n_elements', type=int, default=1000,
                       help='Number of causal set elements')
    parser.add_argument('--density', type=float, default=0.1,
                       help='Density of causal relations')
    parser.add_argument('--n_steps', type=int, default=5,
                       help='Number of evolution steps')
    
    args = parser.parse_args()
    
    # Load config or use defaults
    config = {
        'n_elements': args.n_elements,
        'density': args.density,
        'n_steps': args.n_steps
    }
    
    # Try to load from file
    try:
        with open(args.parameters, 'r') as f:
            file_config = json.load(f)
            config.update(file_config)
    except FileNotFoundError:
        print(f"Config file {args.parameters} not found, using defaults")
    
    run_simulation(config)

if __name__ == "__main__":
    main()
