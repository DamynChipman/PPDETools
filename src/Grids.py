import numpy as np
import matplotlib.pyplot as plt


class Grid1D:

    def __init__(self, lBound, rBound, NPTS, grid_type='cell edge'):
        self._lBound = lBound
        self._rBound = rBound
        self._NPTS = NPTS

        if (grid_type == 'cell edge'):
            self._delX = (self._rBound - self._lBound)/(self._NPTS - 1)
            self._pts = np.linspace(self._lBound,
                                    self._rBound,
                                    num=self._NPTS)
        elif (grid_type == 'cell centered'):
            self._delX = (self._rBound - self._lBound)/(self._NPTS)
            self._pts = np.linspace(self._lBound + self._delX/2,
                                    self._rBound - self._delX/2,
                                    num=self._NPTS)
        elif (grid_type == 'cell edge gp'):
            self._delX = (self._rBound - self._lBound)/(self._NPTS - 1)
            self._pts = np.linspace(self._lBound - self._delX,
                                    self._rBound + self._delX,
                                    num=self._NPTS)
        elif (grid_type == 'cell centered gp'):
            self._delX = (self._rBound - self._lBound)/(self._NPTS)
            self._pts = np.linspace(self._lBound - self._delX/2,
                                    self._rBound + self._delX/2,
                                    num=self._NPTS)
        else:
            print("ERROR IN Grid1D: INVALID grid_type NAME")

    def getRBound(self):
        return self._rBound

    def getLBound(self):
        return self._lBound

    def getNPTS(self):
        return self._NPTS

    def getDelX(self):
        return self._delX

    def getPoints(self):
        return self._pts


# --- END OF CLASS Grid1D ---

# -- BEGIN TESTING/DEBUGGING SECTION ---

grid1 = Grid1D(0, 1, 10, grid_type='cell edge')
grid2 = Grid1D(0, 1, 10, grid_type='cell centered')
grid3 = Grid1D(0, 1, 10, grid_type='cell edge gp')
grid4 = Grid1D(0, 1, 10, grid_type='cell centered gp')

x1 = grid1.getPoints()
x2 = grid2.getPoints()
x3 = grid3.getPoints()
x4 = grid4.getPoints()

y1 = x1**2
y2 = x2**2
y3 = x3**2
y4 = x4**2

plt.plot(x1, y1, 'r', x2, y2, 'b', x3, y3, 'g', x4, y4, 'y')
plt.show()
