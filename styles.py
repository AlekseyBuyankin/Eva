def getWhite():
    return 'rgb(255, 255, 255)'


def getLight():
    # return 'rgb(236, 245, 255)'
    return 'rgb(219, 230, 249)'


def getDark():
    # return 'rgb(199, 225, 255)'
    return 'rgb(187, 211, 251)'


def getFontStyle(pt: int):
    return str(pt) + 'pt "Consolas"'


def setStylesForMainWindow(self):
    white = getWhite()
    light = getLight()
    dark = getDark()
    fontStyle12 = getFontStyle(12)
    fontStyle9 = getFontStyle(9)
    fontStyle8 = getFontStyle(8)

    bbw = params(True, True, white, False, '')
    bbfl12 = params(True, True, light, True, fontStyle12)
    bbfl9 = params(True, True, light, True, fontStyle9)
    bbfl8 = params(True, True, light, True, fontStyle8)
    bbfd12 = params(True, True, dark, True, fontStyle12)
    bfw = params(False, True, white, False, '')

    self.ui.mainFrame.setStyleSheet(bbw)

    self.ui.stepBackButton.setStyleSheet(bbfl12)
    self.ui.stepForwardButton.setStyleSheet(bbfl12)
    self.ui.startButton.setStyleSheet(bbfl12)

    self.ui.frame11.setStyleSheet(bbfl9)
    self.ui.frame22.setStyleSheet(bbfl9)
    self.ui.frame33.setStyleSheet(bbfl9)
    self.ui.frame44.setStyleSheet(bbfl9)
    self.ui.mutation_label.setStyleSheet(bbfl8)

    self.ui.genes_number.setStyleSheet(bfw)
    self.ui.ind_number.setStyleSheet(bfw)
    self.ui.elite.setStyleSheet(bfw)
    self.ui.mutation_probability.setStyleSheet(bfw)
    self.ui.size_multiplier.setStyleSheet(bfw)
    self.ui.xBorder.setStyleSheet(bfw)
    self.ui.yBorder.setStyleSheet(bfw)
    self.ui.zBorder.setStyleSheet(bfw)
    self.ui.number_of_generations.setStyleSheet(bfw)
    self.ui.best_value.setStyleSheet(bfw)


def params(borderRadius: bool, backgroundColor: bool, color: str, font: bool, fontStyle12: str):
    string = ''
    if borderRadius:
        string += 'border-radius: 5px; '
    if backgroundColor:
        string += 'background-color: ' + color + '; '
    if font:
        string += 'font: ' + fontStyle12 + '; '
    return string
