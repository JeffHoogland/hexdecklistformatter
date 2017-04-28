# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formatter.ui'
#
# Created: Fri Apr 28 13:16:08 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.deckListEntry = QtGui.QTextEdit(self.frame)
        self.deckListEntry.setObjectName("deckListEntry")
        self.horizontalLayout.addWidget(self.deckListEntry)
        self.deckListOutput = QtGui.QTextEdit(self.frame)
        self.deckListOutput.setObjectName("deckListOutput")
        self.horizontalLayout.addWidget(self.deckListOutput)
        self.verticalLayout.addWidget(self.frame)
        self.generateImage = QtGui.QPushButton(self.centralwidget)
        self.generateImage.setObjectName("generateImage")
        self.verticalLayout.addWidget(self.generateImage)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Hex Decklist Formatter", None, QtGui.QApplication.UnicodeUTF8))
        self.generateImage.setText(QtGui.QApplication.translate("MainWindow", "Format", None, QtGui.QApplication.UnicodeUTF8))

