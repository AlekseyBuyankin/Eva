# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainMenu.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 870)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainFrame = QtWidgets.QFrame(self.centralwidget)
        self.mainFrame.setGeometry(QtCore.QRect(0, 0, 1400, 871))
        self.mainFrame.setObjectName("mainFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.mainFrame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalFrame_2 = QtWidgets.QFrame(self.mainFrame)
        self.verticalFrame_2.setMaximumSize(QtCore.QSize(990, 16777215))
        self.verticalFrame_2.setObjectName("verticalFrame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalFrame_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.gl = GLViewWidget(self.verticalFrame_2)
        self.gl.setObjectName("gl")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.gl)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_3.addWidget(self.gl)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout.addWidget(self.verticalFrame_2)
        self.verticalFrame = QtWidgets.QFrame(self.mainFrame)
        self.verticalFrame.setMaximumSize(QtCore.QSize(410, 16777215))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.verticalFrame.setFont(font)
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem5 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalFrame1 = QtWidgets.QFrame(self.verticalFrame)
        self.verticalFrame1.setObjectName("verticalFrame1")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalFrame1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalFrame = QtWidgets.QFrame(self.verticalFrame1)
        self.horizontalFrame.setMaximumSize(QtCore.QSize(16777215, 100))
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame11 = QtWidgets.QFrame(self.horizontalFrame)
        self.frame11.setObjectName("frame11")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame11)
        self.horizontalLayout_8.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame1 = QtWidgets.QFrame(self.frame11)
        self.frame1.setMaximumSize(QtCore.QSize(80, 16777215))
        self.frame1.setObjectName("frame1")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame1)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label = QtWidgets.QLabel(self.frame1)
        self.label.setMaximumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_7.addWidget(self.label)
        self.genes_number = QtWidgets.QLineEdit(self.frame1)
        self.genes_number.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.genes_number.setFont(font)
        self.genes_number.setObjectName("genes_number")
        self.verticalLayout_7.addWidget(self.genes_number)
        self.horizontalLayout_8.addWidget(self.frame1)
        self.frame2 = QtWidgets.QFrame(self.frame11)
        self.frame2.setMaximumSize(QtCore.QSize(80, 16777215))
        self.frame2.setObjectName("frame2")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame2)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_3 = QtWidgets.QLabel(self.frame2)
        self.label_3.setMaximumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_11.addWidget(self.label_3)
        self.ind_number = QtWidgets.QLineEdit(self.frame2)
        self.ind_number.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.ind_number.setFont(font)
        self.ind_number.setObjectName("ind_number")
        self.verticalLayout_11.addWidget(self.ind_number)
        self.horizontalLayout_8.addWidget(self.frame2)
        self.frame3 = QtWidgets.QFrame(self.frame11)
        self.frame3.setMaximumSize(QtCore.QSize(80, 16777215))
        self.frame3.setObjectName("frame3")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame3)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_4 = QtWidgets.QLabel(self.frame3)
        self.label_4.setMaximumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_12.addWidget(self.label_4)
        self.elite = QtWidgets.QLineEdit(self.frame3)
        self.elite.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.elite.setFont(font)
        self.elite.setObjectName("elite")
        self.verticalLayout_12.addWidget(self.elite)
        self.horizontalLayout_8.addWidget(self.frame3)
        self.frame4 = QtWidgets.QFrame(self.frame11)
        self.frame4.setMaximumSize(QtCore.QSize(80, 16777215))
        self.frame4.setObjectName("frame4")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame4)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.mutation_label = QtWidgets.QLabel(self.frame4)
        self.mutation_label.setMaximumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.mutation_label.setFont(font)
        self.mutation_label.setAlignment(QtCore.Qt.AlignCenter)
        self.mutation_label.setObjectName("mutation_label")
        self.verticalLayout_9.addWidget(self.mutation_label)
        self.mutation_probability = QtWidgets.QLineEdit(self.frame4)
        self.mutation_probability.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.mutation_probability.setFont(font)
        self.mutation_probability.setObjectName("mutation_probability")
        self.verticalLayout_9.addWidget(self.mutation_probability)
        self.horizontalLayout_8.addWidget(self.frame4)
        self.horizontalLayout_5.addWidget(self.frame11)
        self.verticalLayout_5.addWidget(self.horizontalFrame)
        self.frame22 = QtWidgets.QFrame(self.verticalFrame1)
        self.frame22.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame22.setObjectName("frame22")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame22)
        self.horizontalLayout_9.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.frame5 = QtWidgets.QFrame(self.frame22)
        self.frame5.setMaximumSize(QtCore.QSize(80, 16777215))
        self.frame5.setObjectName("frame5")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame5)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_6 = QtWidgets.QLabel(self.frame5)
        self.label_6.setMaximumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_13.addWidget(self.label_6)
        self.size_multiplier = QtWidgets.QLineEdit(self.frame5)
        self.size_multiplier.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.size_multiplier.setFont(font)
        self.size_multiplier.setObjectName("size_multiplier")
        self.verticalLayout_13.addWidget(self.size_multiplier)
        self.horizontalLayout_9.addWidget(self.frame5)
        self.frame6 = QtWidgets.QFrame(self.frame22)
        self.frame6.setMaximumSize(QtCore.QSize(80, 16777215))
        self.frame6.setObjectName("frame6")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame6)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_7 = QtWidgets.QLabel(self.frame6)
        self.label_7.setMaximumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_14.addWidget(self.label_7)
        self.xBorder = QtWidgets.QLineEdit(self.frame6)
        self.xBorder.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.xBorder.setFont(font)
        self.xBorder.setObjectName("xBorder")
        self.verticalLayout_14.addWidget(self.xBorder)
        self.horizontalLayout_9.addWidget(self.frame6)
        self.frame7 = QtWidgets.QFrame(self.frame22)
        self.frame7.setMaximumSize(QtCore.QSize(80, 16777215))
        self.frame7.setObjectName("frame7")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame7)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_8 = QtWidgets.QLabel(self.frame7)
        self.label_8.setMaximumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_15.addWidget(self.label_8)
        self.yBorder = QtWidgets.QLineEdit(self.frame7)
        self.yBorder.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.yBorder.setFont(font)
        self.yBorder.setObjectName("yBorder")
        self.verticalLayout_15.addWidget(self.yBorder)
        self.horizontalLayout_9.addWidget(self.frame7)
        self.frame8 = QtWidgets.QFrame(self.frame22)
        self.frame8.setMaximumSize(QtCore.QSize(80, 16777215))
        self.frame8.setObjectName("frame8")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame8)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_9 = QtWidgets.QLabel(self.frame8)
        self.label_9.setMaximumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_16.addWidget(self.label_9)
        self.zBorder = QtWidgets.QLineEdit(self.frame8)
        self.zBorder.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.zBorder.setFont(font)
        self.zBorder.setObjectName("zBorder")
        self.verticalLayout_16.addWidget(self.zBorder)
        self.horizontalLayout_9.addWidget(self.frame8)
        self.verticalLayout_5.addWidget(self.frame22)
        self.frame33 = QtWidgets.QFrame(self.verticalFrame1)
        self.frame33.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame33.setObjectName("frame33")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame33)
        self.horizontalLayout_10.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.frame9 = QtWidgets.QFrame(self.frame33)
        self.frame9.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame9.setObjectName("frame9")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.frame9)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_10 = QtWidgets.QLabel(self.frame9)
        self.label_10.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_17.addWidget(self.label_10)
        self.number_of_generations = QtWidgets.QLineEdit(self.frame9)
        self.number_of_generations.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.number_of_generations.setFont(font)
        self.number_of_generations.setObjectName("number_of_generations")
        self.verticalLayout_17.addWidget(self.number_of_generations)
        self.horizontalLayout_10.addWidget(self.frame9)
        self.verticalLayout_5.addWidget(self.frame33)
        self.frame44 = QtWidgets.QFrame(self.verticalFrame1)
        self.frame44.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame44.setObjectName("frame44")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame44)
        self.horizontalLayout_11.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.frame9_2 = QtWidgets.QFrame(self.frame44)
        self.frame9_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame9_2.setObjectName("frame9_2")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.frame9_2)
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_11 = QtWidgets.QLabel(self.frame9_2)
        self.label_11.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_18.addWidget(self.label_11)
        self.best_value = QtWidgets.QLineEdit(self.frame9_2)
        self.best_value.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.best_value.setFont(font)
        self.best_value.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.best_value.setReadOnly(True)
        self.best_value.setObjectName("best_value")
        self.verticalLayout_18.addWidget(self.best_value)
        self.horizontalLayout_11.addWidget(self.frame9_2)
        self.verticalLayout_5.addWidget(self.frame44)
        spacerItem6 = QtWidgets.QSpacerItem(0, 260, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem6)
        self.verticalLayout_4.addWidget(self.verticalFrame1)
        self.horizontalFrame1 = QtWidgets.QFrame(self.verticalFrame)
        self.horizontalFrame1.setMaximumSize(QtCore.QSize(16777215, 100))
        self.horizontalFrame1.setObjectName("horizontalFrame1")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalFrame1)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(7)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.stepBackButton = QtWidgets.QPushButton(self.horizontalFrame1)
        self.stepBackButton.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.stepBackButton.setFont(font)
        self.stepBackButton.setObjectName("stepBackButton")
        self.horizontalLayout_4.addWidget(self.stepBackButton)
        self.stepForwardButton = QtWidgets.QPushButton(self.horizontalFrame1)
        self.stepForwardButton.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.stepForwardButton.setFont(font)
        self.stepForwardButton.setObjectName("stepForwardButton")
        self.horizontalLayout_4.addWidget(self.stepForwardButton)
        self.startButton = QtWidgets.QPushButton(self.horizontalFrame1)
        self.startButton.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.startButton.setFont(font)
        self.startButton.setObjectName("startButton")
        self.horizontalLayout_4.addWidget(self.startButton)
        self.verticalLayout_4.addWidget(self.horizontalFrame1)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem8 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem8)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout.addWidget(self.verticalFrame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Количество\n"
"объектов"))
        self.label_3.setText(_translate("MainWindow", "Размер\n"
"популяции"))
        self.label_4.setText(_translate("MainWindow", "Размер\n"
"элиты"))
        self.mutation_label.setText(_translate("MainWindow", "Коэффициент\n"
"мутации"))
        self.label_6.setText(_translate("MainWindow", "Множитель\n"
"размера"))
        self.label_7.setText(_translate("MainWindow", "Граница\n"
"по X"))
        self.label_8.setText(_translate("MainWindow", "Граница\n"
"по Y"))
        self.label_9.setText(_translate("MainWindow", "Граница\n"
"по Z"))
        self.label_10.setText(_translate("MainWindow", "Количество итераций\n"
"генетического алгоритма"))
        self.label_11.setText(_translate("MainWindow", "Заполненность объектами"))
        self.stepBackButton.setText(_translate("MainWindow", "<"))
        self.stepForwardButton.setText(_translate("MainWindow", ">"))
        self.startButton.setText(_translate("MainWindow", "Start"))


from pyqtgraph.opengl import GLViewWidget
