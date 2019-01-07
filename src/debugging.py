# ========== debugging.py ==========

# ===== Imports =====
import Grids
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


# Grid spacing visualization
grid1 = Grids.Grid1D(0, 1, 10, grid_type='cell edge')
grid2 = Grids.Grid1D(0, 1, 10, grid_type='cell centered')
grid3 = Grids.Grid1D(0, 1, 10, grid_type='cell edge gp')
grid4 = Grids.Grid1D(0, 1, 10, grid_type='cell centered gp')

for point in grid1:
    print(point)

x1 = grid1.getPoints()
x2 = grid2.getPoints()
x3 = grid3.getPoints()
x4 = grid4.getPoints()

y1 = np.zeros(10) + 1
y2 = np.zeros(10) + 2
y3 = np.zeros(10) + 3
y4 = np.zeros(10) + 4

fig1 = plt.figure(1)
plt.plot(x1, y1, 'r.', x2, y2, 'b.', x3, y3, 'g.', x4, y4, 'y.')
plt.legend(['Cell-Edge',
            'Cell-Centered',
            'Cell-Edge w/ GP',
            'Cell-Centered w/ GP'],
           loc='lower left',
           bbox_to_anchor=(.2, 1.00),
           borderaxespad=0.5,
           ncol=2)

# 3D plotting with Grid2D
grid5 = Grids.Grid2D([-1, 1], [2, 5], 10, 20, grid_type='cell centered gp')
X = grid5.getX()
Y = grid5.getY()
Z = np.sin(X) + np.cos(Y)

fig2 = plt.figure(2)
ax = fig2.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z)

plt.show(fig1)
plt.show(fig2)


# ========== END OF debugging.py ==========
