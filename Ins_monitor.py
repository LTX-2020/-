# -*- coding: utf-8 -*-
"""
幻变声浪图形模块——乐器模拟widget
author:杨博远
"""

from PyQt5 import QtCore, QtMultimedia
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QWidget, QLabel, QSlider, QHBoxLayout, QVBoxLayout, QPushButton, QGridLayout, \
    QGraphicsOpacityEffect, QFrame, QTreeWidget


class Ins_monitor(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()  # 界面绘制交给InitUi方法

    def volume_control(self):
        self.volume1.setText(str(self.slider1.value()))
        if hasattr(self, 'player'):
            self.player.setVolume(self.slider1.value())

    def piano_player(self, event):
        gx=event.globalPos().x()-self.mapToGlobal(self.piano.pos()).x()+11
        x = event.pos().x()
        y = event.pos().y()
        t1=self.piano.pos().x()
        t2=self.piano2.pos().x()
        t3=self.piano3.pos().x()
        if gx>self.piano3.geometry().x():
            pass
        elif gx>self.piano2.geometry().x():
            relative_pos = x - self.piano.geometry().x()
            result = int(relative_pos / (self.piano.geometry().width() / 7) + 1.2)
            url = QtCore.QUrl.fromLocalFile('./audio/%s.mp3' % result)
            content = QtMultimedia.QMediaContent(url)
            if not hasattr(self, 'player'):
                self.player = QtMultimedia.QMediaPlayer()
            self.player.setMedia(content)
            self.player.setVolume(self.slider1.value())
            self.player.play()
        else:
            pass

    def initUI(self):
        # 载入样式文件
        with open('style.qss', 'r') as f:
            qssstyle = f.read()
            self.setStyleSheet(qssstyle)
        # 内容布局
        # 设置透明度的值，0.0到1.0，最小值0是透明，1是不透明
        op = QGraphicsOpacityEffect()
        op.setOpacity(0.7)
        self.setGraphicsEffect(op)

        # 钢琴按键
        self.piano = QLabel(self)
        pianomap = QPixmap("./photos/piano1.png")
        self.piano.setPixmap(pianomap)
        self.piano.setScaledContents(True)

        self.piano2 = QLabel(self)
        piano2map = QPixmap("./photos/piano1.png")
        self.piano2.setPixmap(piano2map)
        self.piano2.setScaledContents(True)

        self.piano3 = QLabel(self)
        piano3map = QPixmap("./photos/piano1.png")
        self.piano3.setPixmap(piano3map)
        self.piano3.setScaledContents(True)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.piano)
        hbox2.addWidget(self.piano2)
        hbox2.addWidget(self.piano3)
        hbox2.setSpacing(0)

        self.piano.mousePressEvent = self.piano_player
        self.piano2.mousePressEvent = self.piano_player
        self.piano3.mousePressEvent = self.piano_player
        # 音量滑动条
        self.slider1 = QSlider(Qt.Vertical)
        slider2 = QSlider(Qt.Vertical)
        self.slider1.valueChanged.connect(self.volume_control)
        self.volume1 = QLabel(str(self.slider1.value()))
        self.volume1.setObjectName('volume')
        self.slider1.setValue(50)
        volume2 = QLabel(str(slider2.value()))
        volume2.setObjectName('volume')
        #打开，保存按钮
        open_btn= QPushButton(QIcon('./photos/load.png'),'打开')
        open_btn.setIconSize(QSize(30, 30))
        open_btn.setObjectName('smallbtn')
        save_btn= QPushButton(QIcon('./photos/save.png'),"保存")
        save_btn.setIconSize(QSize(30, 30))
        save_btn.setObjectName('smallbtn')
        record_btn=QPushButton(QIcon('./photos/record.png'),"录制")
        record_btn.setIconSize(QSize(30, 30))
        record_btn.setObjectName('smallbtn')
        # 乐器选择
        ins1 = QPushButton("钢琴")
        ins1.setCheckable(True)
        ins1.setChecked(True)
        ins1.setAutoExclusive(True)
        ins1.setObjectName('btn')
        ins2 = QPushButton("ins2")
        ins2.setCheckable(True)
        ins2.setAutoExclusive(True)
        ins2.setObjectName('btn')
        ins3 = QPushButton("ins3")
        ins3.setCheckable(True)
        ins3.setAutoExclusive(True)
        ins3.setObjectName('btn')
        ins4 = QPushButton("ins4")
        ins4.setCheckable(True)
        ins4.setAutoExclusive(True)
        ins4.setObjectName('btn')

        volume_widget=QWidget()
        volume_name=QLabel('音量调节')
        volume_name.setObjectName('volume')
        glayout1 = QGridLayout()
        glayout1.addWidget(volume_name, 0, 0)
        glayout1.addWidget(self.slider1, 1, 0)
        glayout1.addWidget(slider2, 1, 1)
        glayout1.addWidget(self.volume1, 2, 0)
        glayout1.addWidget(volume2, 2, 1)
        volume_widget.setLayout(glayout1)
        volume_widget.setObjectName('bg_widget')

        ins_widget=QWidget()
        ins_name=QLabel('乐器选择')
        ins_name.setObjectName('volume')
        glayout2 = QGridLayout()
        glayout2.addWidget(ins_name,0,0)
        glayout2.addWidget(ins1, 1, 0)
        glayout2.addWidget(ins2, 1, 1)
        glayout2.addWidget(ins3, 2, 0)
        glayout2.addWidget(ins4, 2, 1)
        ins_widget.setLayout(glayout2)
        ins_widget.setObjectName('bg_widget')

        file_widget=QWidget()
        file_name=QLabel('文件操作')
        file_name.setObjectName('volume')

        #文件树
        self.tree = QTreeWidget()
        # 设置列数
        self.tree.setColumnCount(2)
        # 设置树形控件头部的标题
        self.tree.setHeaderLabels(['文件名', '大小'])


        vbox=QVBoxLayout()
        vbox.addWidget(file_name)
        vbox.addWidget(open_btn)
        vbox.addWidget(save_btn)
        vbox.addWidget(record_btn)
        file_widget.setLayout(vbox)
        file_widget.setObjectName('bg_widget')

        #音量，文件操作，乐器选择框架
        hbox = QHBoxLayout()
        hbox.addWidget(volume_widget)
        hbox.addWidget(file_widget)
        hbox.addWidget(ins_widget)
        hbox.addWidget(self.tree)
        hbox.addStretch(1)

        vbox2 = QVBoxLayout()
        vbox2.addLayout(hbox)
        vbox2.addSpacing(20)
        vbox2.addLayout(hbox2)
        vbox2.setStretchFactor(hbox, 1)
        vbox2.setStretchFactor(hbox2, 1)
        self.setLayout(vbox2)
