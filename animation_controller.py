# animation_controller.py

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from Rhmbus import Rhombus, create_initial_rhombus
from visualization import draw_rhombi
import matplotlib

matplotlib.use('TkAgg')

# You can adjust this limit. The reset will happen when the number of tiles exceeds this.
MAX_TILES = 100000

rhombi = [create_initial_rhombus(is_fat=True, size=1.0)]

fig = plt.figure(figsize=(16, 8))
ax_anim = fig.add_subplot(1, 2, 1)
ax_text = fig.add_subplot(1, 2, 2)

def draw_math_explanation(ax):
    ax.axis('off')
    ax.set_title("The Math Behind Penrose Tiling", fontsize=16)
    math_text = (
        r"$\bf{1. \ The \ Golden \ Ratio \ (\phi)}$"
        "\n"
        r"$\phi = \frac{1 + \sqrt{5}}{2} \approx 1.618...$"
        "\n\n"
        r"$\bf{2. \ The \ Two \ Prototiles}$"
        "\n"
        r"• $\bf{Fat \ Rhombus:}$ 72°, 108°"
        "\n"
        r"• $\bf{Thin \ Rhombus:}$ 36°, 144°"
        "\n\n"
        r"$\bf{3. \ The \ Deflation \ Rules}$"
        "\n"
        r"• A $\bf{fat}$ rhombus → 2 fat, 1 thin."
        "\n"
        r"• A $\bf{thin}$ rhombus → 1 fat, 1 thin."
        "\n\n"
        r"$\bf{4. \ Emergent \ Properties}$"
        "\n"
        r"• $\bf{Aperiodicity:}$ The pattern never repeats."
        "\n"
        r"• $\bf{Five-Fold \ Symmetry.}$"
    )
    ax.text(0.05, 0.95, math_text, ha='left', va='top', fontsize=12, wrap=True)

draw_math_explanation(ax_text)

def update(frame):
    global rhombi

    # --- Step 1: Generate the next state (Deflation) ---
    # (Skip on frame 0 to show the initial tile first)
    if frame > 0:
        new_rhombi = []
        for rh in rhombi:
            new_rhombi.extend(rh.deflate())
        rhombi = new_rhombi

    # --- Step 2: Draw the current state ---
    draw_rhombi(rhombi, ax_anim)
    ax_anim.set_title(f"Generation: {frame} | Tiles: {len(rhombi)}")

    # --- Step 3: Check the state and RESET for the next frame if over the limit ---
    if len(rhombi) > MAX_TILES:
        print(f"\n--- Reached Limit ({len(rhombi)} > {MAX_TILES}). Resetting simulation. ---\n")
        # This resets the data that the *next* call to update() will see
        rhombi = [create_initial_rhombus(is_fat=True, size=1.0)]


ani = animation.FuncAnimation(fig, update, interval=3000, repeat=False, cache_frame_data=False)
plt.show()