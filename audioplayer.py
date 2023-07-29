# -*- coding: utf-8 -*-
import inspect

# Form implementation generated from reading ui file 'audioplayer.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QStyle

from spoiler import Expander


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 590)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(98, 0, 202, 255), stop:1 rgba(218, 0, 156, 255));\n"
"font-family: Noto Sans;\n"
"color: rgba(0,0,0,160);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalFrame = QtWidgets.QFrame(self.centralwidget)
        self.verticalFrame.setStyleSheet("background-color: rgba(255, 255, 255, 2);\n"
"")
        self.verticalFrame.setObjectName("verticalFrame")

        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.tabWidget = QtWidgets.QTabWidget(self.verticalFrame)

        self.tabWidget.setStyleSheet("\n"
"QTabBar::tab:selected {\n"
"color: black;\n"
"background-color: rgba(255,255,255,30);\n"
"color: rgba(0,0,0,200);\n"
"\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"color: black;\n"
"color: rgba(0,0,0,160);\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"height: 30px;\n"
"width: 100px;\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"border-bottom:none;\n"
"\n"
"\n"
"}\n"
"\n"
"QTabWidget{\n"
"font-weight: bold;\n"
"font-family: Noto Sans;\n"
"\n"
"\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"top:-1px;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"} \n"
"\n"
"QTabWidget::tab-bar {\n"
"bottom:1px;\n"
"\n"
"} \n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        self.tracklist = QtWidgets.QWidget()
        self.tracklist.setStyleSheet("font-weight: bold;\n"
"font-family: Noto Sans;")
        self.tracklist.setObjectName("tracklist")
        self.tracklist_frame = QtWidgets.QFrame(self.tracklist)
        self.tracklist_frame.setGeometry(QtCore.QRect(0, 5, 441, 361))
        self.tracklist_frame.setStyleSheet("border: none;\n"
"")
        self.tracklist_frame.setObjectName("tracklist_frame")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.tracklist_frame)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.shuffle_pushButton = QtWidgets.QPushButton(self.tracklist_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shuffle_pushButton.sizePolicy().hasHeightForWidth())
        self.shuffle_pushButton.setSizePolicy(sizePolicy)
        self.shuffle_pushButton.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"   background-color: none;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"  background-color: rgba(224, 255, 255, 50);\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"  background-color: rgba(224, 255, 255, 30);\n"
"    border-radius: 7px;\n"
"}")
        self.shuffle_pushButton.setObjectName("shuffle_pushButton")
        self.horizontalLayout_9.addWidget(self.shuffle_pushButton)
        spacerItem = QtWidgets.QSpacerItem(252, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem)
        self.delete_pushButton = QtWidgets.QPushButton(self.tracklist_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_pushButton.sizePolicy().hasHeightForWidth())
        self.delete_pushButton.setSizePolicy(sizePolicy)
        self.delete_pushButton.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"   background-color: none;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"  background-color: rgba(224, 255, 255, 50);\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"  background-color: rgba(224, 255, 255, 30);\n"
"    border-radius: 7px;\n"
"}")
        self.delete_pushButton.setObjectName("delete_pushButton")
        self.horizontalLayout_9.addWidget(self.delete_pushButton)
        self.verticalLayout_11.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tracklist_listWidget = QtWidgets.QListWidget(self.tracklist_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tracklist_listWidget.sizePolicy().hasHeightForWidth())
        self.tracklist_listWidget.setSizePolicy(sizePolicy)
        self.tracklist_listWidget.setStyleSheet("")
        self.tracklist_listWidget.setProperty("isWrapping", False)
        self.tracklist_listWidget.setObjectName("tracklist_listWidget")
        self.horizontalLayout_3.addWidget(self.tracklist_listWidget)
        self.verticalLayout_11.addLayout(self.horizontalLayout_3)
        self.tabWidget.addTab(self.tracklist, "")
        self.add = QtWidgets.QWidget()
        self.add.setStyleSheet("font-weight: bold;\n"
"font-family: Noto Sans;")
        self.add.setObjectName("add")
        self.load_frame = QtWidgets.QFrame(self.add)
        self.load_frame.setGeometry(QtCore.QRect(0, 5, 451, 371))
        self.load_frame.setStyleSheet("")
        self.load_frame.setObjectName("load_frame")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.load_frame)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.load_frame)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.loadurl_lineEdit = QtWidgets.QLineEdit(self.load_frame)
        self.loadurl_lineEdit.setObjectName("loadurl_lineEdit")
        self.verticalLayout_2.addWidget(self.loadurl_lineEdit)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.load_frame)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.loadfile_pushButton = QtWidgets.QPushButton(self.load_frame)
        self.loadfile_pushButton.setStyleSheet("\n"
"QPushButton\n"
"{\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"  background-color: rgba(224, 255, 255, 50);\n"
"  border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"  background-color: rgba(224, 255, 255, 30);\n"
"  border-radius: 7px;\n"
"}")
        self.loadfile_pushButton.setObjectName("loadfile_pushButton")
        self.horizontalLayout_4.addWidget(self.loadfile_pushButton)
        self.loadfolder_pushButton = QtWidgets.QPushButton(self.load_frame)
        self.loadfolder_pushButton.setStyleSheet("\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"  background-color: rgba(224, 255, 255, 50);\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"  background-color: rgba(224, 255, 255, 30);\n"
"    border-radius: 7px;\n"
"}")
        self.loadfolder_pushButton.setObjectName("loadfolder_pushButton")
        self.horizontalLayout_4.addWidget(self.loadfolder_pushButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_8.addLayout(self.horizontalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.load_frame)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.search_lineEdit = QtWidgets.QLineEdit(self.load_frame)
        self.search_lineEdit.setObjectName("search_lineEdit")
        self.verticalLayout_4.addWidget(self.search_lineEdit)
        self.verticalLayout_8.addLayout(self.verticalLayout_4)
        self.tracklist_listWidget_2 = QtWidgets.QListWidget(self.load_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tracklist_listWidget_2.sizePolicy().hasHeightForWidth())
        self.tracklist_listWidget_2.setSizePolicy(sizePolicy)
        self.tracklist_listWidget_2.setStyleSheet("")
        self.tracklist_listWidget_2.setProperty("isWrapping", False)
        self.tracklist_listWidget_2.setObjectName("tracklist_listWidget_2")
        self.verticalLayout_8.addWidget(self.tracklist_listWidget_2)
        self.tabWidget.addTab(self.add, "")
        self.settings = QtWidgets.QWidget()
        self.settings.setStyleSheet("font-weight: bold;\n"
"font-family: Noto Sans;")
        self.settings.setObjectName("settings")
        self.settings_frame = QtWidgets.QFrame(self.settings)
        self.settings_frame.setGeometry(QtCore.QRect(5, 5, 451, 90))
        self.settings_frame.setStyleSheet("")
        self.settings_frame.setObjectName("settings_frame")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.settings_frame)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_8 = QtWidgets.QLabel(self.settings_frame)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_9.addWidget(self.label_8)
        self.transparancy_horizontalSlider = QtWidgets.QSlider(self.settings_frame)
        self.transparancy_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.transparancy_horizontalSlider.setObjectName("transparancy_horizontalSlider")
        self.transparancy_horizontalSlider.setStyleSheet("QSlider::groove:horizontal {border: 1px solid; height: 10px; margin: 0px;}\n"
                                                         "QSlider::handle:horizontal {background-color: black;border: 1px solid;height: 40px;width: 5px;margin: -15px 0px;}")
        self.verticalLayout_9.addWidget(self.transparancy_horizontalSlider)
        self.horizontalLayout_8.addLayout(self.verticalLayout_9)
        self.widget = QtWidgets.QWidget(self.settings)
        self.widget.setGeometry(QtCore.QRect(5, 120, 150, 50))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_9 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout.addWidget(self.label_9)
        self.ontop_radioButton = QtWidgets.QRadioButton(self.widget)
        self.ontop_radioButton.setText("")

        self.ontop_radioButton.setChecked(True)
        self.ontop_radioButton.setObjectName("ontop_radioButton")
        self.horizontalLayout.addWidget(self.ontop_radioButton)
        self.tabWidget.addTab(self.settings, "")
        self.verticalLayout_12.addWidget(self.tabWidget)







        self.expanded_tab = QtWidgets.QVBoxLayout()
        self.expanded_tab.addWidget(self.verticalFrame)


        self.expander = Expander(self.centralwidget)
        self.expander.setGeometry(QtCore.QRect(0, 120, 500, 31))
        self.expander.setContentLayout(self.expanded_tab)


        #player_frame
        self.player_frame = QtWidgets.QFrame(self.centralwidget)
        self.player_frame.setGeometry(QtCore.QRect(10, 10, 481, 101))
        self.player_frame.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.player_frame.setObjectName("player_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.player_frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.trackname_label = QtWidgets.QLabel(self.player_frame)
        self.trackname_label.setStyleSheet("font-weight: bold;\n"
"font-size: 12pt;\n"
"background-color: none;\n"
"border: none;\n"
"")
        self.trackname_label.setAlignment(QtCore.Qt.AlignCenter)
        self.trackname_label.setObjectName("trackname_label")
        self.verticalLayout.addWidget(self.trackname_label)
        self.track_horizontalSlider = QtWidgets.QSlider(self.player_frame)

        self.track_horizontalSlider.setAutoFillBackground(False)
        self.track_horizontalSlider.setStyleSheet("QSlider::groove:horizontal {border: 0px solid; height: 10px; margin: 0px;}\n"
                                                         "QSlider::handle:horizontal {background-color: black; border: 1px solid; height: 40px;width: 5px;margin: -15px 0px;}")
        self.track_horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.track_horizontalSlider.setObjectName("track_horizontalSlider")
        self.verticalLayout.addWidget(self.track_horizontalSlider)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.prev_pushButton = QtWidgets.QPushButton(self.player_frame)
        self.prev_pushButton.setAutoFillBackground(False)
        self.prev_pushButton.setStyleSheet("\n"
"\n"
"QPushButton\n"
"{\n"
"   background-color: none;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"  background-color: rgba(224, 255, 255, 50);\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"  background-color: rgba(224, 255, 255, 30);\n"
"    border-radius: 7px;\n"
"}")
        self.prev_pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/skip_previous_FILL0_wght400_GRAD0_opsz48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.prev_pushButton.setIcon(icon)
        self.prev_pushButton.setIconSize(QtCore.QSize(30, 30))
        self.prev_pushButton.setObjectName("prev_pushButton")
        self.horizontalLayout_2.addWidget(self.prev_pushButton)
        self.play_pushButton = QtWidgets.QPushButton(self.player_frame)
        self.play_pushButton.setStyleSheet("QPushButton\n"
"{\n"
"   background-color: none;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"  background-color: rgba(224, 255, 255, 50);\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"  background-color: rgba(224, 255, 255, 30);\n"
"    border-radius: 7px;\n"
"}")
        self.play_pushButton.setText("")
        self.play_pushButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.play_pushButton.setIconSize(QtCore.QSize(30, 30))
        self.play_pushButton.setObjectName("play_pushButton")
        self.horizontalLayout_2.addWidget(self.play_pushButton)
        self.next_pushButton = QtWidgets.QPushButton(self.player_frame)
        self.next_pushButton.setStyleSheet("QPushButton\n"
"{\n"
"   background-color: none;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"  background-color: rgba(224, 255, 255, 50);\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed\n"
"{\n"
"  background-color: rgba(224, 255, 255, 30);\n"
"    border-radius: 7px;\n"
"}")
        self.next_pushButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/skip_next_FILL0_wght400_GRAD0_opsz48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.next_pushButton.setIcon(icon2)
        self.next_pushButton.setIconSize(QtCore.QSize(30, 30))
        self.next_pushButton.setObjectName("next_pushButton")
        self.horizontalLayout_2.addWidget(self.next_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        MainWindow.resize(500, self.player_frame.sizeHint().height() + self.expander.height())
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Audio player"))
        self.shuffle_pushButton.setText(_translate("MainWindow", "Shuffle"))
        self.delete_pushButton.setText(_translate("MainWindow", "Delete"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tracklist), _translate("MainWindow", "Tracklist"))
        self.label.setText(_translate("MainWindow", "Enter url to track"))
        self.label_3.setText(_translate("MainWindow", "Open file explorer"))
        self.loadfile_pushButton.setText(_translate("MainWindow", "Load file"))
        self.loadfolder_pushButton.setText(_translate("MainWindow", "Load folder"))
        self.label_4.setText(_translate("MainWindow", "Search for track"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.add), _translate("MainWindow", "Add"))
        self.label_8.setText(_translate("MainWindow", "Transparancy"))
        self.label_9.setText(_translate("MainWindow", "Always on top"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settings), _translate("MainWindow", "Settings"))
        self.trackname_label.setText(_translate("MainWindow", "Tracklist empty"))
        self.transparancy_horizontalSlider.setSliderPosition(100)


import res_rc
