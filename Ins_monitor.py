# -*- coding: utf-8 -*-
"""
幻变声浪图形模块——乐器模拟widget
author:杨博远
"""
import os
from PyQt5 import QtCore, QtMultimedia
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QLabel, QSlider, QHBoxLayout, QVBoxLayout, QPushButton, QGridLayout, \
    QGraphicsOpacityEffect, QTreeWidget, QFileDialog, QTreeWidgetItem, QHeaderView, QGroupBox, QSizePolicy
from Recorder import Recorder
import threading
import time
from datetime import datetime


class Ins_monitor(QWidget):

    def playerstate(self,tar):
        #尝试解决内存泄漏(不理想)
        state=tar.state()
        if(state==0):
            self.playerlist.remove(tar)


    def __init__(self):
        super().__init__()
        self.playerlist=[]
        self.initUI()  # 界面绘制交给InitUi方法

    def volume_control(self):
        self.volume1.setText(str(self.slider1.value()))
        if hasattr(self, 'player'):
            self.player.setVolume(self.slider1.value())


    def piano_player(self):
        sender=self.sender()
        # threading.Thread(target=self.play, args=(sender.text(),)).start()
        self.playerlist.append(QtMultimedia.QMediaPlayer())
        player = self.playerlist[len(self.playerlist) - 1]
        # 强行延长作用域？？？
        print(len(self.playerlist))
        player.stateChanged.connect(lambda: self.playerstate(player))
        url = QtCore.QUrl.fromLocalFile('./audio/%s.mp3' % sender.text())
        content = QtMultimedia.QMediaContent(url)
        player.setMedia(content)
        player.setVolume(self.slider1.value())
        player.play()


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
        self.pianol1 = QPushButton('l1')
        # self.pianol1.sizePolicy().setVerticalPolicy(QSizePolicy.MinimumExpanding)
        self.pianol1.setObjectName('piano1')
        self.pianol1.clicked.connect(self.piano_player)
        self.pianol2 = QPushButton('l2')
        self.pianol2.setObjectName('piano2')
        self.pianol2.clicked.connect(self.piano_player)
        self.pianol3 = QPushButton('l3')
        self.pianol3.setObjectName('piano3')
        self.pianol3.clicked.connect(self.piano_player)
        self.pianol4 = QPushButton('l4')
        self.pianol4.setObjectName('piano1')
        self.pianol4.clicked.connect(self.piano_player)
        self.pianol5 = QPushButton('l5')
        self.pianol5.setObjectName('piano2')
        self.pianol5.clicked.connect(self.piano_player)
        self.pianol6 = QPushButton('l6')
        self.pianol6.setObjectName('piano2')
        self.pianol6.clicked.connect(self.piano_player)
        self.pianol7 = QPushButton('l7')
        self.pianol7.setObjectName('piano3')
        self.pianol7.clicked.connect(self.piano_player)

        self.pianom1 = QPushButton('m1')
        self.pianom1.setShortcut('1')
        self.pianom1.setObjectName('piano1')
        self.pianom1.clicked.connect(self.piano_player)
        self.pianom2 = QPushButton('m2')
        self.pianom2.setShortcut('2')
        self.pianom2.setObjectName('piano2')
        self.pianom2.clicked.connect(self.piano_player)
        self.pianom3 = QPushButton('m3')
        self.pianom3.setShortcut('3')
        self.pianom3.setObjectName('piano3')
        self.pianom3.clicked.connect(self.piano_player)
        self.pianom4 = QPushButton('m4')
        self.pianom4.setShortcut('4')
        self.pianom4.setObjectName('piano1')
        self.pianom4.clicked.connect(self.piano_player)
        self.pianom5 = QPushButton('m5')
        self.pianom5.setShortcut('5')
        self.pianom5.setObjectName('piano2')
        self.pianom5.clicked.connect(self.piano_player)
        self.pianom6 = QPushButton('m6')
        self.pianom6.setShortcut('6')
        self.pianom6.setObjectName('piano2')
        self.pianom6.clicked.connect(self.piano_player)
        self.pianom7 = QPushButton('m7')
        self.pianom7.setShortcut('7')
        self.pianom7.setObjectName('piano3')
        self.pianom7.clicked.connect(self.piano_player)

        self.pianoh1 = QPushButton('h1')
        self.pianoh1.setObjectName('piano1')
        self.pianoh1.clicked.connect(self.piano_player)
        self.pianoh2 = QPushButton('h2')
        self.pianoh2.setObjectName('piano2')
        self.pianoh2.clicked.connect(self.piano_player)
        self.pianoh3 = QPushButton('h3')
        self.pianoh3.setObjectName('piano3')
        self.pianoh3.clicked.connect(self.piano_player)
        self.pianoh4 = QPushButton('h4')
        self.pianoh4.setObjectName('piano1')
        self.pianoh4.clicked.connect(self.piano_player)
        self.pianoh5 = QPushButton('h5')
        self.pianoh5.setObjectName('piano2')
        self.pianoh5.clicked.connect(self.piano_player)
        self.pianoh6 = QPushButton('h6')
        self.pianoh6.setObjectName('piano2')
        self.pianoh6.clicked.connect(self.piano_player)
        self.pianoh7 = QPushButton('h7')
        self.pianoh7.setObjectName('piano3')
        self.pianoh7.clicked.connect(self.piano_player)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.pianol1)
        hbox2.addWidget(self.pianol2)
        hbox2.addWidget(self.pianol3)
        hbox2.addWidget(self.pianol4)
        hbox2.addWidget(self.pianol5)
        hbox2.addWidget(self.pianol6)
        hbox2.addWidget(self.pianol7)
        hbox2.addSpacing(10)
        hbox2.addWidget(self.pianom1)
        hbox2.addWidget(self.pianom2)
        hbox2.addWidget(self.pianom3)
        hbox2.addWidget(self.pianom4)
        hbox2.addWidget(self.pianom5)
        hbox2.addWidget(self.pianom6)
        hbox2.addWidget(self.pianom7)
        hbox2.addSpacing(10)
        hbox2.addWidget(self.pianoh1)
        hbox2.addWidget(self.pianoh2)
        hbox2.addWidget(self.pianoh3)
        hbox2.addWidget(self.pianoh4)
        hbox2.addWidget(self.pianoh5)
        hbox2.addWidget(self.pianoh6)
        hbox2.addWidget(self.pianoh7)
        hbox2.setSpacing(0)

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
        self.record_btn = QPushButton(QIcon('./photos/record.png'), "录制")
        self.record_btn.setIconSize(QSize(30, 30))
        self.record_btn.setObjectName('smallbtn')
        self.record_btn.setCheckable(True)
        self.record_btn.clicked.connect(self.record_event)
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
        vbox.addWidget(self.record_btn)
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
        vbox2.addStretch()
        vbox2.addLayout(hbox2)
        vbox2.addStretch()
        # vbox2.setStretchFactor(hbox, 1)
        # vbox2.setStretchFactor(hbox2, 1)
        self.setLayout(vbox2)

    def record_job(self):
        if not os.path.exists('records'):
            os.makedirs('records')
        rec = Recorder()
        begin = 0
        if 1:  # 开始录音的条件
            begin = time.time()
            rec.start()  # 开始
            running = True
            #print(1)
            while running:  # 循环录音
                if not self.record_btn.isChecked():  # 结束录音的条件
                    running = False
                    rec.stop()
                    t = time.time() - begin
                    #print('录音时间为%ds' % t)
                    # 以当前时间为关键字保存wav文件
                    rec.save("records/rec_" + datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".wav")  # 保存文件

    def record_event(self):
        if self.record_btn.isChecked():
          record_thread = threading.Thread(target=self.record_job)
          record_thread.start()