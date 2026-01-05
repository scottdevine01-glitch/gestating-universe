"""
Causal Set implementation for Gestating Universe Theory.
Generates discrete spacetime structure with partial ordering.
"""

import numpy as np
import networkx as nx
from typing import List, Tuple

class CausalSet:
    """Discrete spacetime as a locally finite partial order."""
    
    def __init__(self, n_elements: int = 1000, density: float = 0.1):
        """
        Initialize a random causal set.
        
        Parameters:
        -----------
        n_elements : int
            Number of causal set elements (spacetime atoms)
        density : float
            Approximate density of causal relations (0-1)
        """
        self.n = n_elements
        self.density = density
        self.elements = np.arange(n_elements)  # Element identifiers
        self.graph = nx.DiGraph()
        self._build_random_causet()
    
    def _build_random_causet(self):
        """Build a random causal set that satisfies partial order axioms."""
        # Start with empty graph
        self.graph.add_nodes_from(self.elements)
        
        # Generate random causal relations
        for i in self.elements:
            for j in self.elements[i+1:]:
                if np.random.random() < self.density:
                    # Check for transitivity consistency
                    if not self._would_create_cycle(i, j):
                        self.graph.add_edge(i, j)
    
    def _would_create_cycle(self, i: int, j: int) -> bool:
        """Check if adding edge i->j would create a cycle."""
        # Simplified check - in full implementation would use transitive closure
        return j in nx.ancestors(self.graph, i)
    
    def get_prec(self, x: int, y: int) -> bool:
        """Return True if x precedes y in the causal order."""
        return self.graph.has_edge(x, y) or x in nx.ancestors(self.graph, y)
    
    def benincasa_dowker_action(self) -> float:
        """
        Calculate Benincasa-Dowker action for causal set gravity.
        
        Returns:
        --------
        float : S_BD = N - N_1 + 9N_2 - 16N_3 + 8N_4
        """
        N = self.n
        
        # Count chains of length 1 (edges)
        N1 = self.graph.number_of_edges()
        
        # For a complete implementation, we'd need to count:
        # N2: number of 2-chains (x ≺ y ≺ z)
        # N3: number of 3-chains
        # N4: number of 4-chains
        
        # Simplified placeholder
        N2 = int(N1 * 0.3)  # Approximate
        N3 = int(N1 * 0.1)  # Approximate
        N4 = int(N1 * 0.05) # Approximate
        
        return N - N1 + 9*N2 - 16*N3 + 8*N4
    
    def to_adjacency_matrix(self) -> np.ndarray:
        """Return adjacency matrix representation."""
        return nx.to_numpy_array(self.graph, nodelist=sorted(self.graph.nodes()))
    
    def visualize(self, save_path: str = None):
        """Visualize the causal set (for small n)."""
        if self.n > 50:
            print(f"Warning: Visualization skipped for large n={self.n}")
            return
            
        import matplotlib.pyplot as plt
        
        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos, with_labels=True, node_size=500, 
                node_color='skyblue', font_size=8, arrowsize=10)
        
        plt.title(f"Causal Set (n={self.n}, density={self.density})")
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Saved to {save_path}")
        else:
            plt.show()


if __name__ == "__main__":
    # Example usage
    print("Testing CausalSet implementation...")
    
    # Create a small causal set
    causet = CausalSet(n_elements=20, density=0.15)
    
    # Check some properties
    print(f"Number of elements: {causet.n}")
    print(f"Number of causal relations: {causet.graph.number_of_edges()}")
    print(f"BD Action (approx): {causet.benincasa_dowker_action():.2f}")
    
    # Test precedence
    print(f"Does 0 precede 5? {causet.get_prec(0, 5)}")
    
    # Visualize if small enough
    causet.visualize()
