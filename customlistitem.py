import sys
from PyQt5 import QtGui, QtWidgets

class QCustomQWidget (QtWidgets.QWidget):
    def __init__ (self, parent = None):
        super(QCustomQWidget, self).__init__(parent)
        self.textQVBoxLayout = QtWidgets.QVBoxLayout()
        self.textQLabel    = QtWidgets.QLabel()

        self.textQVBoxLayout.addWidget(self.textQLabel)

        self.allQHBoxLayout  = QtWidgets.QHBoxLayout()
        self.iconQLabel      = QtWidgets.QLabel()
        self.allQHBoxLayout.addWidget(self.iconQLabel, 0)
        self.allQHBoxLayout.addLayout(self.textQVBoxLayout, 1)
        self.setLayout(self.allQHBoxLayout)
        # setStyleSheet


        self.dir = ""


    def setText (self, text):
        self.textQLabel.setText(text)

    def setDir (self, dir):
        self.dir = dir

    def dir (self):
        return self.dir
    def text (self):
        return self.textQLabel.text()

    def setIcon (self, imagePath):
        self.iconQLabel.setPixmap(QtGui.QPixmap(imagePath))

