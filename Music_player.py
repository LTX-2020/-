# -*- coding: utf-8 -*-
"""
幻变声浪图形模块——音乐播放器widget
author:杨博远
Todo:音乐长度较长时，进度条无法自己刷新;加入拖动进度条功能;
"""
import threading
import time

from PyQt5 import QtMultimedia
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtMultimedia import QMediaPlaylist
from PyQt5.QtWidgets import QPushButton, QLabel, QProgressBar, QHBoxLayout, QWidget


class mthread(QThread):
    _signal = pyqtSignal(int)

    def __init__(self,s):
        super(mthread, self).__init__()
        self.s=s

    def run(self):
        self._signal.emit(self.s)

class Music_player(QWidget):

    def __init__(self):
        super().__init__()
        self.music_player = QtMultimedia.QMediaPlayer()
        self.music_player.durationChanged.connect(self.music_player_state)
        # self.playlist=QMediaPlaylist()
        # self.playlist.setPlaybackMode(3)
        self.__play = QPushButton()
        self.__play.setCheckable(True)
        self.__play.setObjectName("player_play")
        self.__play.clicked.connect(self.play_music)
        # self.__next = QPushButton()
        # self.__next.setObjectName("player_next")
        # self.__next.clicked.connect(self.play_next)
        self.__play_time = QLabel('0:00')
        self.__play_time.setObjectName('player_label')
        self.__play_totaltime = QLabel('0:00')
        self.__play_totaltime.setObjectName('player_label')
        self.__pbar = QProgressBar()
        self.__pbar.setTextVisible(False)
        player = QHBoxLayout()
        player.addWidget(self.__play)
        # player.addWidget(self.__next)
        player.addWidget(self.__play_time)
        player.addWidget(self.__pbar)
        player.addWidget(self.__play_totaltime)
        self.setLayout(player)

    def reset(self):
        self.__play_time.setText("0:00")
        self.__pbar.setValue(0)
        self.__play.setChecked(False)
    # def play_next(self):
    #     self.playlist.next()
        # threading.Thread(target=self.progressbar_control).start()

    def play_music(self):
        if self.__play.isChecked():
            if self.music_player.duration()!=0:
                self.music_player.play()
                self.__isplay=True
                threading.Thread(target=self.progressbar_control).start()
            else:
                self.__play.setChecked(False)
        else:
            self.__isplay = False
            self.music_player.pause()

    def set_text(self,s):
        # print(s)
        if s>=60:
            min=int(s/60)
            sec=s-min*60
            # print(sec)
            if sec<10:
                self.__play_time.setText(str(min) + ':0' + str(sec))
            else:
                self.__play_time.setText(str(min)+':'+str(sec))
        else:
            if s < 10:
                self.__play_time.setText('0:0' + str(s))
            else:
                self.__play_time.setText('0:'+str(s))

    def progressbar_control(self):
        while(self.__isplay):
            if self.music_player.duration()==0:
                time.sleep(0.25)
                continue
            position=self.music_player.position()
            progress=position/self.music_player.duration()*100
            # print(progress)
            thread=mthread(position/1000)
            thread._signal.connect(self.set_text)
            thread.start()
            self.__pbar.setValue(progress)
            if progress==100:
                if self.music_player.state()==0:
                    self.__play.setChecked(False)
                    break
            time.sleep(0.25)

    def music_player_state(self):
        s=round(self.music_player.duration()/1000)
        if s>=60:
            min=int(s/60)
            sec=s-min*60
            if s < 10:
                self.__play_totaltime.setText(str(min) + ':0' + str(sec))
            else:
                self.__play_totaltime.setText(str(min)+':'+str(sec))
        else:
            if s<10:
                self.__play_totaltime.setText('0:0'+str(s))
            else:
                self.__play_totaltime.setText('0:' + str(s))