import inspect

from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDesktopWidget, QStyle
import audioplayer
from customlistitem import QCustomQWidget
import os


class Player(QtWidgets.QMainWindow, audioplayer.Ui_MainWindow):
    def __init__(self):
        super(Player, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.dir = ""
        self.transparancy = 255
        self.offset = None
        self.mediaPlayer = QtMultimedia.QMediaPlayer()
        self.mediaPlayer.setVolume(5)
        #self.is_plaing = False
        self.current_cont = None



        #player tab
        self.play_pushButton.clicked.connect(self.play)
        self.next_pushButton.clicked.connect(self.next)
        self.prev_pushButton.clicked.connect(self.prev)
        self.expander.toggleButton.clicked.connect(self.change_size)

        #tracklist tab
        self.tracklist_listWidget.itemDoubleClicked.connect(self.play)
        self.shuffle_pushButton.clicked.connect(self.shuffle)
        self.delete_pushButton.clicked.connect(self.delete)

        #add tab
        self.loadfile_pushButton.clicked.connect(self.load_file)
        self.loadfolder_pushButton.clicked.connect(self.load_folder)
        self.tracklist_listWidget_2.itemDoubleClicked.connect(self.play)

        self.loadurl_lineEdit.returnPressed.connect(self.load_url)
        #self.search_lineEdit.returnPressed.connect(self.search)

        #settings tab
        self.ontop_radioButton.clicked.connect(self.ontop)
        self.transparancy_horizontalSlider.valueChanged.connect(self.change_trancparancy)

        self.track_horizontalSlider.sliderMoved.connect(self.set_position)
        self.mediaPlayer.stateChanged.connect(self.mediastate_changed)
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)
        self.show()

    def position_changed(self, position):
        self.track_horizontalSlider.setValue(position)
        if self.mediaPlayer.position() == self.mediaPlayer.duration() and self.mediaPlayer.duration()!=0:
            self.next()

    def duration_changed(self, duration):
        self.track_horizontalSlider.setRange(0, duration)

    def mediastate_changed(self, state):
        if self.mediaPlayer.state() == QtMultimedia.QMediaPlayer.PlayingState:
            self.play_pushButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.play_pushButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

    def set_position(self, position):
        self.mediaPlayer.setPosition(position)

    def change_trancparancy(self):
        self.transparancy = self.transparancy_horizontalSlider.value()/100 + 0.1
        self.setWindowOpacity(self.transparancy)

    def ontop(self):
        if self.ontop_radioButton.isChecked():
            self.setWindowFlag(Qt.WindowStaysOnTopHint)
            self.show()
        else:
            self.setWindowFlag(Qt.WindowStaysOnTopHint, False)
            self.show()


    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.offset = event.pos()
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.offset is not None and event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.pos() - self.offset)
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.offset = None
        super().mouseReleaseEvent(event)

    def change_size(self):
        if self.expander.toggleButton.isChecked():
            self.resize(500, 590)
        else:
            self.resize(500, self.player_frame.sizeHint().height() + 31)

    def play(self):
        if self.tracklist_listWidget.count() != 0:
            item = self.tracklist_listWidget.currentItem()
        else:
            return

        if item:
            file_name = self.tracklist_listWidget.itemWidget(item).dir
            content = QtMultimedia.QMediaContent(QtCore.QUrl(file_name))
            if self.current_cont != content and self.tracklist_listWidget.count() != 1:
                self.mediaPlayer.setMedia(content)
                self.current_cont = content
                self.mediaPlayer.play()
                self.trackname_label.setText(self.tracklist_listWidget.itemWidget(item).text())
            elif self.mediaPlayer.state() == QtMultimedia.QMediaPlayer.PlayingState:
                self.mediaPlayer.pause()
            elif self.mediaPlayer.state() == QtMultimedia.QMediaPlayer.PausedState:
                self.mediaPlayer.play()
            else:
                self.mediaPlayer.setMedia(content)
                self.current_cont = content
                self.mediaPlayer.play()
                self.trackname_label.setText(self.tracklist_listWidget.itemWidget(item).text())


    def load_folder(self):
        dir = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory")
        if dir:
            for file_name in os.listdir(dir):
                if file_name.endswith(".mp3"):
                    custom_item = QCustomQWidget(self.tracklist_listWidget)
                    custom_item.setText(file_name)
                    custom_item.setDir(dir+"/"+file_name)
                    item = QtWidgets.QListWidgetItem(self.tracklist_listWidget)
                    item.setSizeHint(custom_item.sizeHint())
                    self.tracklist_listWidget.addItem(item)
                    self.tracklist_listWidget.setItemWidget(item, custom_item)
                    if self.tracklist_listWidget.count() == 1:
                        print("1")
                        self.tracklist_listWidget.setCurrentRow(0)



    def next(self):
        if self.tracklist_listWidget.count() > 1:
            self.tracklist_listWidget.setCurrentRow((self.tracklist_listWidget.currentRow() + 1) % self.tracklist_listWidget.count())

          #  self.is_plaing = False
            self.play()
        else:
            self.play()

    def prev(self):
        if self.tracklist_listWidget.count():
            self.tracklist_listWidget.setCurrentRow((self.tracklist_listWidget.currentRow() - 1) % self.tracklist_listWidget.count())
           # self.is_plaing = False
            self.play()




    def load_url(self):

        url = self.loadurl_lineEdit.text()


        custom_item = QCustomQWidget(self.tracklist_listWidget)
        custom_item.setText(url)
        custom_item.setDir(url)
        item = QtWidgets.QListWidgetItem(self.tracklist_listWidget)
        item.setSizeHint(custom_item.sizeHint())
        self.tracklist_listWidget.addItem(item)
        self.tracklist_listWidget.setItemWidget(item, custom_item)
        if self.tracklist_listWidget.count() == 1:
            self.tracklist_listWidget.setCurrentRow(0)

        self.loadurl_lineEdit.clear()



    def shuffle(self):
        pass



    def delete(self):
        if self.tracklist_listWidget.count():
            item  = self.tracklist_listWidget.takeItem(self.tracklist_listWidget.currentRow())
            del item
            self.is_plaing = False

    def load_file(self):
        dir = QtWidgets.QFileDialog.getOpenFileName(self)[0]
        file_name = os.path.basename(dir)
        if file_name.endswith(".mp3"):
            custom_item = QCustomQWidget(self.tracklist_listWidget)
            custom_item.setText(file_name)
            custom_item.setDir(dir)
            item = QtWidgets.QListWidgetItem(self.tracklist_listWidget)
            item.setSizeHint(custom_item.sizeHint())
            self.tracklist_listWidget.addItem(item)
            self.tracklist_listWidget.setItemWidget(item, custom_item)
            if self.tracklist_listWidget.count() == 1:
                self.tracklist_listWidget.setCurrentRow(0)



if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    QtCore.QCoreApplication.setOrganizationName("Eyllanesc")
    QtCore.QCoreApplication.setOrganizationDomain("eyllanesc.com")
    QtCore.QCoreApplication.setApplicationName("MyApp")
    player = Player()

   # player.setWindowOpacity(player.transparancy)
    player.setAttribute(Qt.WA_NoSystemBackground, True)
    player.show()
    sys.exit(app.exec_())