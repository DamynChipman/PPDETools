import numpy as np


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

grid1 = Grid1D(0, 1, 10, grid_type='cell edge')
grid2 = Grid1D(0, 1, 10, grid_type='cell centered')
grid3 = Grid1D(0, 1, 10, grid_type='cell edge gp')
grid4 = Grid1D(0, 1, 10, grid_type='cell centered gp')

print(grid1.getPoints())
print(grid2.getPoints())
print(grid3.getPoints())
print(grid4.getPoints())
