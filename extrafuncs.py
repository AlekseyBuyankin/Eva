from pyqtgraph.Qt import QtCore
from pyqtgraph.opengl.GLGraphicsItem import GLGraphicsItem
import styles
from random import randint
import colorsys


#
# # действия на кнопку
# def onButtonClick(self, buttons: list, button):
#     if buttons and button != self.ui.startButton and self.ui.textButton:
#         if self.allDict['otherButtons']:
#             self.allDict['otherButtons'][0].setStyleSheet(
#                 styles.params(True, True, styles.getLight(), True, styles.getFontStyle()))
#             self.allDict['otherButtons'].remove(self.allDict['otherButtons'][0])
#
#         buttons[0].setStyleSheet(styles.params(True, True, styles.getLight(), True, styles.getFontStyle()))
#
#         buttons.remove(buttons[0])
#
#     button.setStyleSheet(styles.params(True, True, styles.getDark(), True, styles.getFontStyle()))
#
#     buttons.append(button)


# добавить одну надпись
def addText(self, x: int, y: int, z: int, text: str):
    w = self.ui.gl

    t = GLTextItem(x=x, y=y, z=z, text=text)
    t.setGLViewWidget(w)
    w.addItem(t)

    # self.allDict['xs'].append(x)
    # self.allDict['ys'].append(y)
    # self.allDict['zs'].append(z)
    # self.allDict['texts'].append(text)
    # self.allDict['textBox'].append(t)


# добавить весь текст на плоскость (на кнопку Т)
def addAllText(self):
    w = self.ui.gl

    xs = self.allDict['xs']
    ys = self.allDict['ys']
    zs = self.allDict['zs']
    texts = self.allDict['texts']

    for i in range(0, len(xs)):
        t = GLTextItem(x=xs[i], y=ys[i], z=zs[i], text=texts[i])
        t.setGLViewWidget(w)
        w.addItem(t)

        self.allDict['textBox'].append(t)


# убрать текст с плоскости (на кнопку Т)
def removeText(self):
    w = self.ui.gl

    for item in self.allDict['textBox']:
        w.removeItem(item)

    self.allDict['textBox'] = []


# нужна для отрисовки текста на плоскости
class GLTextItem(GLGraphicsItem):
    def __init__(self, x=None, y=None, z=None, text=None):
        GLGraphicsItem.__init__(self)

        self.text = text
        self.x = x
        self.y = y
        self.z = z

    def setGLViewWidget(self, GLViewWidget):
        self.GLViewWidget = GLViewWidget

    def setText(self, text):
        self.text = text
        self.update()

    def setX(self, x):
        self.x = x
        self.update()

    def setY(self, y):
        self.y = y
        self.update()

    def setZ(self, z):
        self.z = z
        self.update()

    def paint(self):
        self.GLViewWidget.qglColor(QtCore.Qt.white)
        self.GLViewWidget.renderText(self.x, self.y, self.z, self.text)


def fromRGB(r, g, b):
    newR = float(str(r / 255)[0:3])
    newG = float(str(g / 255)[0:3])
    newB = float(str(b / 255)[0:3])
    return newR, newG, newB


def rainbowColors():
    i = randint(0, 1000)
    (r, g, b) = colorsys.hsv_to_rgb(i / 1000.0, 1.0, 1.0)
    return r, g, b
