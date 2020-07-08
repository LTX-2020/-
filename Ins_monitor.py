# -*- coding: utf-8 -*-
"""
幻变声浪图形模块——乐器模拟widget
author:杨博远
"""
import os
from PyQt5 import QtCore, QtMultimedia
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QWidget, QLabel, QSlider, QHBoxLayout, QVBoxLayout, QPushButton, QGridLayout, \
    QGraphicsOpacityEffect, QTreeWidget, QFileDialog, QTreeWidgetItem, QHeaderView, QGroupBox


class Ins_monitor(QWidget):

    def playerstate(self,state,pos):
        if(state==1):
            self.piano2.setPixmap(self.pianomaplist[pos - 1])
        elif(state==0):
            self.piano2.setPixmap(self.piano2map)


    def __init__(self):
        super().__init__()
        self.initUI()  # 界面绘制交给InitUi方法

    def volume_control(self):
        self.volume1.setText(str(self.slider1.value()))
        if hasattr(self, 'player'):
            self.player.setVolume(self.slider1.value())

    def piano_player(self, event):
        #钢琴弹奏模块，待优化
        gx=event.globalPos().x()-self.mapToGlobal(self.piano.pos()).x()+11
        x = event.pos().x()
        y = event.pos().y()
        t1=self.piano.pos().x()
        t2=self.piano2.pos().x()
        t3=self.piano3.pos().x()
        #高音区域
        if gx>self.piano3.geometry().x():
            pass
        #中音区域
        elif gx>self.piano2.geometry().x():
            relative_pos = x - self.piano.geometry().x()
            result = int(relative_pos / (self.piano.geometry().width() / 7) + 1.2)
            url = QtCore.QUrl.fromLocalFile('./audio/%s.mp3' % result)
            content = QtMultimedia.QMediaContent(url)
            if not hasattr(self, 'player'):
                self.player = QtMultimedia.QMediaPlayer()
            self.player.stateChanged.connect(lambda: self.playerstate(self.player.state(), result))
            self.player.setMedia(content)
            self.player.setVolume(self.slider1.value())
            self.player.play()
        #低音区域
        else:
            pass

    def open_event(self):
        directory = QFileDialog.getOpenFileName(self,'打开','.','*.mp3')
        if(directory==('', '')):
            return
        new_treeitem=QTreeWidgetItem()
        new_treeitem.setText(0,directory[0])
        size=os.path.getsize(directory[0])/float(1024 * 1024)
        new_treeitem.setText(1,'%.2f MB'%size)
        self.tree.addTopLevelItem(new_treeitem)

    def save_event(self):
        directory = QFileDialog.getSaveFileName(self,'保存','.','*.mp3')
        if (directory == ('', '')):
            return

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
        self.pianomaplist=[QPixmap("./photos/piano1.png"),QPixmap("./photos/piano2.png"),QPixmap("./photos/piano3.png"),QPixmap("./photos/piano4.png"),QPixmap("./photos/piano5.png"),QPixmap("./photos/piano6.png"),QPixmap("./photos/piano7.png")]
        self.piano = QLabel(self)
        pianomap = QPixmap("./photos/piano.png")
        self.piano.setPixmap(pianomap)
        self.piano.setScaledContents(True)

        self.piano2 = QLabel(self)
        self.piano2map = QPixmap("./photos/piano.png")
        self.piano2.setPixmap(self.piano2map)
        self.piano2.setScaledContents(True)

        self.piano3 = QLabel(self)
        piano3map = QPixmap("./photos/piano.png")
        self.piano3.setPixmap(piano3map)
        self.piano3.setScaledContents(True)

        #钢琴键盘布局
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
        open_btn.clicked.connect(self.open_event)
        save_btn= QPushButton(QIcon('./photos/save.png'),"保存")
        save_btn.setIconSize(QSize(30, 30))
        save_btn.setObjectName('smallbtn')
        save_btn.clicked.connect(self.save_event)
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

        #volume_groupbox
        glayout1 = QGridLayout()
        glayout1.addWidget(self.slider1, 0, 0)
        glayout1.addWidget(slider2, 0, 1)
        glayout1.addWidget(self.volume1, 1, 0)
        glayout1.addWidget(volume2, 1, 1)
        volume_groupBox = QGroupBox("音量调节")
        volume_groupBox.setLayout(glayout1)

        #ins_groupbox
        glayout2 = QGridLayout()
        glayout2.addWidget(ins1, 0, 0)
        glayout2.addWidget(ins2, 0, 1)
        glayout2.addWidget(ins3, 1, 0)
        glayout2.addWidget(ins4, 1, 1)
        ins_groupBox = QGroupBox("乐器选择")
        ins_groupBox.setLayout(glayout2)

        #文件树
        self.tree = QTreeWidget()
        # 设置树形控件头部的标题
        self.tree.setHeaderLabels(['文件名', '大小'])
        self.tree.setRootIsDecorated(False)
        # 宽度对内容变化
        self.tree.header().setSectionResizeMode(QHeaderView.ResizeToContents)

        #file_groupbox
        vbox=QVBoxLayout()
        vbox.addWidget(open_btn)
        vbox.addWidget(save_btn)
        vbox.addWidget(record_btn)
        hbox3=QHBoxLayout()
        hbox3.addLayout(vbox)
        hbox3.addWidget(self.tree)
        file_groupBox = QGroupBox("文件操作")
        file_groupBox.setLayout(hbox3)

        #音量，文件操作，乐器选择布局
        hbox = QHBoxLayout()
        hbox.addWidget(volume_groupBox)
        hbox.addWidget(ins_groupBox)
        # hbox.addStretch(1)
        hbox.addWidget(file_groupBox)


        #竖直布局
        vbox2 = QVBoxLayout()
        vbox2.addLayout(hbox)
        vbox2.addSpacing(20)
        vbox2.addLayout(hbox2)
        vbox2.setStretchFactor(hbox, 1)
        vbox2.setStretchFactor(hbox2, 1)
        self.setLayout(vbox2)
