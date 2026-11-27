import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon

# UNIDAD 4 - PRACTICA GUIADA: PERSONALIZA TU EMBLEMA

fig, ax = plt.subplots(figsize=(7, 7))

# 1. HEXAGONO EXTERIOR: RELLENO HOMOGENEO
hexagono = [
    (4, 1), (7, 2.5), (7, 5.5),
    (4, 7), (1, 5.5), (1, 2.5)
]

exterior = Polygon(
    hexagono,
    closed=True,
    facecolor="indigo",
    edgecolor="lavender",
    linewidth=4,
    zorder=1
)
ax.add_patch(exterior)

# 2. ROMBO INTERIOR: RELLENO DEGRADADO
rombo = [(4, 2), (6.2, 4), (4, 6), (1.8, 4)]

interior = Polygon(
    rombo,
    closed=True,
    facecolor="none",
    edgecolor="gold",
    linewidth=3,
    zorder=3
)
ax.add_patch(interior)

valores = np.linspace(0, 1, 300)
degradado = np.tile(valores[:, None], (1, 300)).T  # Degradado horizontal

imagen = ax.imshow(
    degradado,
    extent=(0, 8, 0, 8),
    origin="lower",
    cmap="viridis",
    zorder=2
)
imagen.set_clip_path(interior)

# 3. PRESENTACION
ax.set_xlim(0, 8)
ax.set_ylim(0, 8)
ax.set_aspect("equal")
ax.axis("off")
plt.title("Emblema Nebula", fontsize=16)
plt.show()