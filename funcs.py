import pyqtgraph.opengl as gl
import extrafuncs
import numpy as np
from extrafuncs import rainbowColors
from random import randint


# Создать view, плоскости и текст
def makeSurface(self):
    w = self.ui.gl
    w.setCameraPosition(distance=100, azimuth=45, elevation=20)

    # Add a grid to the view
    g = gl.GLGridItem()
    g.scale(2, 2, 2)
    g.setDepthValue(10)  # draw grid after surfaces since they may be translucent
    g.translate(20, 20, 0)
    w.addItem(g)

    # Add x
    g = gl.GLGridItem()
    g.scale(2.1, 0, 0)
    g.translate(20, -1, 0)
    g.setDepthValue(10)  # draw grid after surfaces since they may be translucent
    w.addItem(g)

    # Add y
    g = gl.GLGridItem()
    g.scale(0, 2.1, 0)
    g.translate(-1, 20, 0)
    g.setDepthValue(10)  # draw grid after surfaces since they may be translucent
    w.addItem(g)

    # Add z
    g = gl.GLGridItem()
    g.scale(2, 0, 0)
    g.rotate(90, 0, 1, 0)
    g.translate(0, 0, 20)
    g.setDepthValue(10)  # draw grid after surfaces since they may be translucent
    w.addItem(g)

    extrafuncs.addText(self, 0, 0, 0, '0')
    extrafuncs.addText(self, 5, 0, 0, 'x')
    extrafuncs.addText(self, 10, 0, 0, 'x 10')
    extrafuncs.addText(self, 20, 0, 0, 'x 20')
    extrafuncs.addText(self, 30, 0, 0, 'x 30')
    extrafuncs.addText(self, 40, 0, 0, 'x 40')

    extrafuncs.addText(self, 0, 5, 0, 'y')
    extrafuncs.addText(self, 0, 10, 0, 'y 10')
    extrafuncs.addText(self, 0, 20, 0, 'y 20')
    extrafuncs.addText(self, 0, 30, 0, 'y 30')
    extrafuncs.addText(self, 0, 40, 0, 'y 40')

    extrafuncs.addText(self, 0, 0, 5, 'z')
    extrafuncs.addText(self, 0, 0, 10, 'z 10')
    extrafuncs.addText(self, 0, 0, 20, 'z 20')
    extrafuncs.addText(self, 0, 0, 30, 'z 30')
    extrafuncs.addText(self, 0, 0, 40, 'z 40')


def makeBorders(self):
    w = self.ui.gl

    xBorder = self.allDict['xBorder'] - 1
    yBorder = self.allDict['yBorder'] - 1
    zBorder = self.allDict['zBorder']

    borders = list(self.allDict['borders'])

    if borders:
        for border in borders:
            w.removeItem(border)

    # Add x
    tx = xBorder / 2
    ty = yBorder
    scale = xBorder / 20

    for tz in range(5):
        g = gl.GLGridItem()
        g.scale(scale, 0, 0)
        g.translate(tx, ty, float('0.' + str(tz)))
        g.setDepthValue(10)  # draw grid after surfaces since they may be translucent
        w.addItem(g)
        borders.append(g)

    # Add y
    tx = xBorder
    ty = yBorder / 2
    scale = yBorder / 20

    for tz in range(5):
        g = gl.GLGridItem()
        g.scale(0, scale, 0)
        g.translate(tx, ty, float('0.' + str(tz)))
        g.setDepthValue(10)  # draw grid after surfaces since they may be translucent
        w.addItem(g)
        borders.append(g)

    # Add z
    tx = xBorder / 2
    tz = zBorder
    scale = xBorder / 20
    n = 3

    for ty in range(n):
        g = gl.GLGridItem()
        g.scale(scale, 0, 0)
        g.translate(tx, float('0.' + str(ty % 10)), tz)
        g.setDepthValue(10)  # draw grid after surfaces since they may be translucent
        w.addItem(g)
        borders.append(g)

    y = yBorder - float('0.' + str(n - 1))
    for ty in range(n):
        g = gl.GLGridItem()
        g.scale(scale, 0, 0)
        g.translate(tx, y + float('0.' + str(ty % 10)), tz)
        g.setDepthValue(10)  # draw grid after surfaces since they may be translucent
        w.addItem(g)
        borders.append(g)

    ty = yBorder / 2
    tz = zBorder
    scale = yBorder / 20

    for tx in range(n):
        g = gl.GLGridItem()
        g.scale(0, scale, 0)
        g.translate(float('0.' + str(tx % 10)), ty, tz)
        g.setDepthValue(10)  # draw grid after surfaces since they may be translucent
        w.addItem(g)
        borders.append(g)

    y = xBorder - float('0.' + str(n - 1))
    for tx in range(n):
        g = gl.GLGridItem()
        g.scale(0, scale, 0)
        g.translate(y + float('0.' + str(tx % 10)), ty, tz)
        g.setDepthValue(10)  # draw grid after surfaces since they may be translucent
        w.addItem(g)
        borders.append(g)

    self.allDict['borders'] = borders


# Убрать график с плоскости
def removePlotFromSurface(self, p0: gl.GLScatterPlotItem):
    w = self.ui.gl

    if self.allDict['plot']:
        w.removeItem(self.allDict['plot'][0])
        self.allDict['plot'] = []
        self.allDict['plot'].append(p0)
    else:
        self.allDict['plot'].append(p0)


def makeParallelepipedCoords(self, k, l, w, h, x, y, z):
    window = self.ui.gl
    verts = np.array([[k + l, 0, 0],  # 0
                      [0, 0, 0],  # 1
                      [0, k + w, 0],  # 2
                      [0, 0, k + h],  # 3
                      [k + l, k + w, 0],  # 4
                      [k + l, k + w, k + h],  # 5
                      [0, k + w, k + h],  # 6
                      [k + l, 0, k + h]])  # 7

    faces = np.array([[1, 0, 7], [1, 3, 7],
                      [1, 2, 4], [1, 0, 4],
                      [1, 2, 6], [1, 3, 6],
                      [0, 4, 5], [0, 7, 5],
                      [2, 4, 5], [2, 6, 5],
                      [3, 6, 5], [3, 7, 5]])

    r, g, b = rainbowColors()
    op = .2
    colors = np.array([[r, g, b, op] for _ in range(12)])
    m1 = gl.GLMeshItem(vertexes=verts, faces=faces, drawFaces=True, drawEdges=True, faceColors=colors, smooth=False,
                       edgeColor=(r, g, b, op))
    m1.translate(x, y, z)
    m1.setGLOptions('additive')
    window.addItem(m1)


def makeRandParallelepipedCoords(self, k, x, y, z):
    l = randint(0, k)
    w = randint(0, k)
    h = randint(0, k)
    makeParallelepipedCoords(self, k, l, w, h, x, y, z)
    self.allDict['yw'] = k + w


def makeParallelepiped(self, k, l, w, h):
    verts = np.array([[k + l, 0, 0],  # 0
                      [0, 0, 0],  # 1
                      [0, k + w, 0],  # 2
                      [0, 0, k + h],  # 3
                      [k + l, k + w, 0],  # 4
                      [k + l, k + w, k + h],  # 5
                      [0, k + w, k + h],  # 6
                      [k + l, 0, k + h]])  # 7

    faces = np.array([[1, 0, 7], [1, 3, 7],
                      [1, 2, 4], [1, 0, 4],
                      [1, 2, 6], [1, 3, 6],
                      [0, 4, 5], [0, 7, 5],
                      [2, 4, 5], [2, 6, 5],
                      [3, 6, 5], [3, 7, 5]])

    r, g, b = rainbowColors()
    op = .15
    colors = np.array([[r, g, b, op] for _ in range(12)])
    m1 = gl.GLMeshItem(vertexes=verts, faces=faces, drawFaces=True, drawEdges=True, faceColors=colors, smooth=False,
                       edgeColor=(r, g, b, op), shader='balloon')

    m1.setGLOptions('additive')
    self.allDict['parals'].append(m1)
    self.allParals[m1] = (l + k, w + k, h + k)


def makeLarge(self, k):
    l = randint(0, k + 1)
    w = randint(0, k + 1)
    h = randint(0, k + 1)
    makeParallelepiped(self, k, l, w, h)

    return k * (l + w + h)


def makeSmall(self, k):
    high = (k + 1) // 2
    l = randint(0, high)
    w = randint(0, high)
    h = randint(0, high)
    makeParallelepiped(self, k, l, w, h)

    return k * (l + w + h)


def randGenes(self, k):
    parals_volume = 0
    while parals_volume <= self.allDict['maxSpace']:
        parals_volume += makeLarge(self, k)
        parals_volume += makeSmall(self, k)
    return parals_volume


def genes(self, k):
    parals = [
        (0, 1, 1),
        (1, 2, 1),
        (1, 1, 2),
        # (1, 2, 1),
        # (2, 2, 1),
        # (2, 2, 1),
        # (0, 1, 1),
        # (1, 0, 0),
        # (0, 2, 1),
        # (1, 1, 0),
        # (0, 0, 1),
        # (1, 0, 1),
        # (1, 0, 2),
    ]

    for l, w, h in parals:
        makeParallelepiped(self, k, l, w, h)
