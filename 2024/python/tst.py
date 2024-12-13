import numpy as np
from scipy.spatial import ConvexHull

# Lijst met punten
points = np.array([(0,0), (0,1), (0,2), (1,0), (2,0)])

# Bereken de convex hull
hull = ConvexHull(points)

# Aantal zijden van de convex hull
num_sides = len(hull.simplices)

print(f"De convex hull heeft {num_sides} zijden.")