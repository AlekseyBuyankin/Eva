def getWhite():
    return 'rgb(255, 255, 255)'


def getLight():
    # return 'rgb(236, 245, 255)'
    return 'rgb(219, 230, 249)'


def getDark():
    # return 'rgb(199, 225, 255)'
    return 'rgb(187, 211, 251)'


def getFontStyle():
    return '12pt "Consolas"'


def setStylesForMainWindow(self):
    white = getWhite()
    light = getLight()
    dark = getDark()
    fontStyle = getFontStyle()

    bbw = params(True, True, white, False, '')
    bbfl = params(True, True, light, True, fontStyle)
    bbfd = params(True, True, dark, True, fontStyle)
    bfw = params(False, True, white, False, '')

    self.ui.mainFrame.setStyleSheet(bbw)

    self.ui.stepBackButton.setStyleSheet(bbfl)
    self.ui.stepForwardButton.setStyleSheet(bbfl)
    self.ui.startButton.setStyleSheet(bbfl)

    # self.ui.nameFrame.setStyleSheet(bbfl)
    # self.ui.frame1.setStyleSheet(bbfl)
    # self.ui.frame22.setStyleSheet(bbfl)
    # self.ui.frame33.setStyleSheet(bbfl)
    # self.ui.frame44.setStyleSheet(bbfl)
    # self.ui.frame55.setStyleSheet(bbfl)
    #
    # self.ui.line1.setStyleSheet(bfw)
    # self.ui.line2.setStyleSheet(bfw)
    # self.ui.line3.setStyleSheet(bfw)
    # self.ui.plainText.setStyleSheet(bfw)
    #
    # self.ui.startButton.setStyleSheet(bbfl)
    # self.ui.textButton.setStyleSheet(bbfl)
    # self.ui.button1.setStyleSheet(bbfd)


def params(borderRadius: bool, backgroundColor: bool, color: str, font: bool, fontStyle: str):
    string = ''
    if borderRadius:
        string += 'border-radius: 5px; '
    if backgroundColor:
        string += 'background-color: ' + color + '; '
    if font:
        string += 'font: ' + fontStyle + '; '
    return string
