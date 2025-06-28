# visualization.py

import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def draw_rhombi(rhombi, ax):
    ax.clear()
    for rh in rhombi:
        verts = rh.get_vertices()
        poly = Polygon(verts, closed=True,
                       edgecolor='black',
                       facecolor='lightblue' if rh.is_fat else 'lightgreen')
        ax.add_patch(poly)
    ax.set_aspect('equal')
    ax.autoscale_view()
    ax.axis('off')