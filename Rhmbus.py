# Rhmbus.py (Corrected Version)

import numpy as np

PHI = (1 + np.sqrt(5)) / 2  # Golden ratio

class Rhombus:
    def __init__(self, vertices, is_fat):
        self.vertices = vertices
        self.is_fat = is_fat

    def get_vertices(self):
        return self.vertices

    def deflate(self):
        new_rhombi = []
        A, B, C, D = self.vertices
        if self.is_fat:
            P = A + (B - A) / PHI
            Q = A + (D - A) / PHI
            new_rhombi.append(Rhombus([P, C, Q, A], is_fat=False))
            new_rhombi.append(Rhombus([D, Q, C, B], is_fat=True))
            new_rhombi.append(Rhombus([Q, C, B, P], is_fat=True))
        else:  # if thin
            R = B + (C - B) / PHI
            new_rhombi.append(Rhombus([D, A, B, R], is_fat=False))
            new_rhombi.append(Rhombus([D, R, C, A], is_fat=True))
        return new_rhombi

# --- CORRECTED HELPER FUNCTION ---
def create_initial_rhombus(center=(0, 0), size=1.0, is_fat=True, angle=0):
    """Creates a mathematically perfect rhombus."""
    if is_fat:
        # The smaller interior angle of a fat rhombus is 72 degrees
        interior_angle = 72 * np.pi / 180
    else:
        # The smaller interior angle of a thin rhombus is 36 degrees
        interior_angle = 36 * np.pi / 180

    # Create a perfect rhombus at the origin based on side length (size)
    #    and interior angle.
    A = np.array([0.0, 0.0])
    B = np.array([size, 0.0])
    D = np.array([size * np.cos(interior_angle), size * np.sin(interior_angle)])
    C = B + D
    vertices = [A, B, C, D]

    #  Find the center of this rhombus and shift it to the origin
    current_center = sum(vertices) / 4.0
    centered_vertices = [v - current_center for v in vertices]

    #  Rotate the centered rhombus and move it to the final center position
    rot_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                           [np.sin(angle), np.cos(angle)]])
    final_vertices = [np.dot(v, rot_matrix.T) + np.array(center) for v in centered_vertices]

    return Rhombus(final_vertices, is_fat)
