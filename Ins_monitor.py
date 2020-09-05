# -*- coding: utf-8 -*-
"""
幻变声浪图形模块——乐器模拟widget
author:杨博远
"""
import threading
from datetime import datetime
import os
import time
from Music_player import Music_player
from PyQt5 import QtCore, QtMultimedia
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QSlider, QHBoxLayout, QVBoxLayout, QPushButton, QGridLayout, \
    QGraphicsOpacityEffect, QTreeWidget, QFileDialog, QTreeWidgetItem, QHeaderView, QGroupBox
from Recorder import Recorder


class Ins_monitor(QWidget):

    def playerstate(self,tar):
        #释放内存
        state=tar.state()
        if(state==0):
            self.playerlist.remove(tar)
            del tar


    def __init__(self):
        super().__init__()
        self.playerlist=[]
        self.initUI()  # 界面绘制交给InitUi方法


    def volume_control(self):
        self.volume1.setText(str(self.slider1.value()))
        if len(self.playerlist)>0:
            for item in self.playerlist:
                try:
                    item.setVolume(self.slider1.value())
                except:
                    pass


    def piano_player(self):
        sender=self.sender()
        self.playerlist.append(QtMultimedia.QMediaPlayer())
        player = self.playerlist[len(self.playerlist) - 1]
        player.stateChanged.connect(lambda: self.playerstate(player))
        if self.ins1.isChecked():
            ins='piano'
        elif self.ins2.isChecked():
            ins='bass'
        else:
            return
        url = QtCore.QUrl.fromLocalFile('./audio/{0}/{1}.mp3'.format(ins, sender.text()))
        content = QtMultimedia.QMediaContent(url)
        player.setMedia(content)
        player.setVolume(self.slider1.value())
        player.play()

    def init_piano(self):
        # 钢琴按键
        pixmap = QPixmap('./photos/p1tm.png')
        pixmapb = QPixmap('./photos/b.png')
        pixmap2 = QPixmap('./photos/p2tm.png')
        pixmap3 = QPixmap('./photos/p3tm.png')

        self.pianol1 = QPushButton('c4')
        self.pianol1.setMask(pixmap.mask())
        self.pianol1.setObjectName('piano1')
        self.pianol1.setShortcut('1')
        self.pianol1.clicked.connect(self.piano_player)

        self.pianolb1 = QPushButton('c#4')
        self.pianolb1.setMask(pixmapb.mask())
        self.pianolb1.setObjectName('pianob')
        self.pianolb1.clicked.connect(self.piano_player)

        self.pianol2 = QPushButton('d4')
        self.pianol2.setObjectName('piano2')
        self.pianol2.setMask(pixmap2.mask())
        self.pianol2.setShortcut('2')
        self.pianol2.clicked.connect(self.piano_player)

        self.pianolb2 = QPushButton('d#4')
        self.pianolb2.setMask(pixmapb.mask())
        self.pianolb2.setObjectName('pianob')
        self.pianolb2.clicked.connect(self.piano_player)

        self.pianol3 = QPushButton('e4')
        self.pianol3.setMask(pixmap3.mask())
        self.pianol3.setObjectName('piano3')
        self.pianol3.setShortcut('3')
        self.pianol3.clicked.connect(self.piano_player)

        self.pianol4 = QPushButton('f4')
        self.pianol4.setMask(pixmap.mask())
        self.pianol4.setObjectName('piano1')
        self.pianol4.setShortcut('4')
        self.pianol4.clicked.connect(self.piano_player)

        self.pianolb3 = QPushButton('f#4')
        self.pianolb3.setMask(pixmapb.mask())
        self.pianolb3.setObjectName('pianob')
        self.pianolb3.clicked.connect(self.piano_player)

        self.pianol5 = QPushButton('g4')
        self.pianol5.setMask(pixmap2.mask())
        self.pianol5.setObjectName('piano2')
        self.pianol5.setShortcut('5')
        self.pianol5.clicked.connect(self.piano_player)

        self.pianolb4 = QPushButton('g#4')
        self.pianolb4.setMask(pixmapb.mask())
        self.pianolb4.setObjectName('pianob')
        self.pianolb4.clicked.connect(self.piano_player)

        self.pianol6 = QPushButton('a4')
        self.pianol6.setMask(pixmap2.mask())
        self.pianol6.setObjectName('piano2')
        self.pianol6.setShortcut('6')
        self.pianol6.clicked.connect(self.piano_player)

        self.pianolb5 = QPushButton('a#4')
        self.pianolb5.setMask(pixmapb.mask())
        self.pianolb5.setObjectName('pianob')
        self.pianolb5.clicked.connect(self.piano_player)

        self.pianol7 = QPushButton('b4')
        self.pianol7.setMask(pixmap3.mask())
        self.pianol7.setObjectName('piano3')
        self.pianol7.setShortcut('7')
        self.pianol7.clicked.connect(self.piano_player)

        self.pianom1 = QPushButton('c5')
        self.pianom1.setMask(pixmap.mask())
        self.pianom1.setShortcut('q')
        self.pianom1.setObjectName('piano1')
        self.pianom1.clicked.connect(self.piano_player)

        self.pianomb1 = QPushButton('c#5')
        self.pianomb1.setMask(pixmapb.mask())
        self.pianomb1.setObjectName('pianob')
        self.pianomb1.clicked.connect(self.piano_player)

        self.pianom2 = QPushButton('d5')
        self.pianom2.setMask(pixmap2.mask())
        self.pianom2.setShortcut('w')
        self.pianom2.setObjectName('piano2')
        self.pianom2.clicked.connect(self.piano_player)

        self.pianomb2 = QPushButton('d#5')
        self.pianomb2.setMask(pixmapb.mask())
        self.pianomb2.setObjectName('pianob')
        self.pianomb2.clicked.connect(self.piano_player)

        self.pianom3 = QPushButton('e5')
        self.pianom3.setMask(pixmap3.mask())
        self.pianom3.setShortcut('e')
        self.pianom3.setObjectName('piano3')
        self.pianom3.clicked.connect(self.piano_player)

        self.pianom4 = QPushButton('f5')
        self.pianom4.setMask(pixmap.mask())
        self.pianom4.setShortcut('r')
        self.pianom4.setObjectName('piano1')
        self.pianom4.clicked.connect(self.piano_player)

        self.pianomb3 = QPushButton('f#5')
        self.pianomb3.setMask(pixmapb.mask())
        self.pianomb3.setObjectName('pianob')
        self.pianomb3.clicked.connect(self.piano_player)

        self.pianom5 = QPushButton('g5')
        self.pianom5.setMask(pixmap2.mask())
        self.pianom5.setShortcut('t')
        self.pianom5.setObjectName('piano2')
        self.pianom5.clicked.connect(self.piano_player)

        self.pianomb4 = QPushButton('g#5')
        self.pianomb4.setMask(pixmapb.mask())
        self.pianomb4.setObjectName('pianob')
        self.pianomb4.clicked.connect(self.piano_player)

        self.pianom6 = QPushButton('a5')
        self.pianom6.setMask(pixmap2.mask())
        self.pianom6.setShortcut('y')
        self.pianom6.setObjectName('piano2')
        self.pianom6.clicked.connect(self.piano_player)

        self.pianomb5 = QPushButton('a#5')
        self.pianomb5.setMask(pixmapb.mask())
        self.pianomb5.setObjectName('pianob')
        self.pianomb5.clicked.connect(self.piano_player)

        self.pianom7 = QPushButton('b5')
        self.pianom7.setMask(pixmap3.mask())
        self.pianom7.setShortcut('u')
        self.pianom7.setObjectName('piano3')
        self.pianom7.clicked.connect(self.piano_player)

        self.pianoh1 = QPushButton('c6')
        self.pianoh1.setMask(pixmap.mask())
        self.pianoh1.setObjectName('piano1')
        self.pianoh1.setShortcut('a')
        self.pianoh1.clicked.connect(self.piano_player)

        self.pianohb1 = QPushButton('c#6')
        self.pianohb1.setMask(pixmapb.mask())
        self.pianohb1.setObjectName('pianob')
        self.pianohb1.clicked.connect(self.piano_player)

        self.pianoh2 = QPushButton('d6')
        self.pianoh2.setMask(pixmap2.mask())
        self.pianoh2.setObjectName('piano2')
        self.pianoh2.setShortcut('s')
        self.pianoh2.clicked.connect(self.piano_player)

        self.pianohb2 = QPushButton('d#6')
        self.pianohb2.setMask(pixmapb.mask())
        self.pianohb2.setObjectName('pianob')
        self.pianohb2.clicked.connect(self.piano_player)

        self.pianoh3 = QPushButton('e6')
        self.pianoh3.setMask(pixmap3.mask())
        self.pianoh3.setObjectName('piano3')
        self.pianoh3.setShortcut('d')
        self.pianoh3.clicked.connect(self.piano_player)

        self.pianoh4 = QPushButton('f6')
        self.pianoh4.setMask(pixmap.mask())
        self.pianoh4.setObjectName('piano1')
        self.pianoh4.setShortcut('f')
        self.pianoh4.clicked.connect(self.piano_player)

        self.pianohb3 = QPushButton('f#6')
        self.pianohb3.setMask(pixmapb.mask())
        self.pianohb3.setObjectName('pianob')
        self.pianohb3.clicked.connect(self.piano_player)

        self.pianoh5 = QPushButton('g6')
        self.pianoh5.setMask(pixmap2.mask())
        self.pianoh5.setObjectName('piano2')
        self.pianoh5.setShortcut('g')
        self.pianoh5.clicked.connect(self.piano_player)

        self.pianohb4 = QPushButton('g#6')
        self.pianohb4.setMask(pixmapb.mask())
        self.pianohb4.setObjectName('pianob')
        self.pianohb4.clicked.connect(self.piano_player)

        self.pianoh6 = QPushButton('a6')
        self.pianoh6.setMask(pixmap2.mask())
        self.pianoh6.setObjectName('piano2')
        self.pianoh6.setShortcut('h')
        self.pianoh6.clicked.connect(self.piano_player)

        self.pianohb5 = QPushButton('a#6')
        self.pianohb5.setMask(pixmapb.mask())
        self.pianohb5.setObjectName('pianob')
        self.pianohb5.clicked.connect(self.piano_player)

        self.pianoh7 = QPushButton('b6')
        self.pianoh7.setMask(pixmap3.mask())
        self.pianoh7.setObjectName('piano3')
        self.pianoh7.setShortcut('j')
        self.pianoh7.clicked.connect(self.piano_player)

        hbox = QHBoxLayout()
        hbox.addWidget(self.pianol1)
        hbox.addSpacing(-24)
        hbox.addWidget(self.pianolb1, 0, Qt.AlignTop)
        hbox.addSpacing(-24)
        hbox.addWidget(self.pianol2)
        hbox.addSpacing(-24)
        hbox.addWidget(self.pianolb2, 0, Qt.AlignTop)
        hbox.addSpacing(-24)
        hbox.addWidget(self.pianol3)
        hbox.addWidget(self.pianol4)
        hbox.addSpacing(-24)
        hbox.addWidget(self.pianolb3, 0, Qt.AlignTop)
        hbox.addSpacing(-24)
        hbox.addWidget(self.pianol5)
        hbox.addSpacing(-24)
        hbox.addWidget(self.pianolb4, 0, Qt.AlignTop)
        hbox.addSpacing(-24)
        hbox.addWidget(self.pianol6)
        hbox.addSpacing(-24)
        hbox.addWidget(self.pianolb5, 0, Qt.AlignTop)
        hbox.addSpacing(-24)
        hbox.addWidget(self.pianol7)
        hbox.addStretch()
        hbox.addWidget(self.pianom1)
        hbox.addSpacing(-24)
        hbox.addWidget(self.pianomb1, 0, Qt.AlignTop)
        hbox.addSpacing(-24)
        hbox.addWidget(self.pianom2)
        hbox.addSpacing(-24)
        hbox.addWidget(self.pianomb2, 0, Qt.AlignTop)
        hbox.addSpacing(-24)
        hbox.addWidget(self.pianom3)
        hbox.addWidget(self.pianom4)
        hbox.addSpacing(-24)
        hbox.addWidget(self.pianomb3, 0, Qt.AlignTop)
        hbox.addSpacing(-24)
        hbox.addWidget(self.pianom5)
        hbox.addSpacing(-24)
        hbox.addWidget(self.pianomb4, 0, Qt.AlignTop)
        hbox.addSpacing(-24)
        hbox.addWidget(self.pianom6)
        hbox.addSpacing(-24)
        hbox.addWidget(self.pianomb5, 0, Qt.AlignTop)
        hbox.addSpacing(-24)
        hbox.addWidget(self.pianom7)
        hbox.addStretch()
        hbox.addWidget(self.pianoh1)
        hbox.addSpacing(-24)
        hbox.addWidget(self.pianohb1, 0, Qt.AlignTop)
        hbox.addSpacing(-24)
        hbox.addWidget(self.pianoh2)
        hbox.addSpacing(-24)
        hbox.addWidget(self.pianohb2, 0, Qt.AlignTop)
        hbox.addSpacing(-24)
        hbox.addWidget(self.pianoh3)
        hbox.addWidget(self.pianoh4)
        hbox.addSpacing(-24)
        hbox.addWidget(self.pianohb3, 0, Qt.AlignTop)
        hbox.addSpacing(-24)
        hbox.addWidget(self.pianoh5)
        hbox.addSpacing(-24)
        hbox.addWidget(self.pianohb4, 0, Qt.AlignTop)
        hbox.addSpacing(-24)
        hbox.addWidget(self.pianoh6)
        hbox.addSpacing(-24)
        hbox.addWidget(self.pianohb5, 0, Qt.AlignTop)
        hbox.addSpacing(-24)
        hbox.addWidget(self.pianoh7)
        hbox.setSpacing(0)
        return hbox

    def open_event(self):
        directory = QFileDialog.getOpenFileName(self,'打开','./records','*.wav;;*.mp3;;*')
        if(directory==('', '')):
            return
        new_treeitem=QTreeWidgetItem()
        new_treeitem.setText(0,directory[0])
        size=os.path.getsize(directory[0])/float(1024 * 1024)
        new_treeitem.setText(1,'%.2f MB'%size)
        self.tree.addTopLevelItem(new_treeitem)
        # self.mplayer.playlist.addMedia(QtMultimedia.QMediaContent(QtCore.QUrl(directory[0])))
        # if self.mplayer.music_player.playlist()!=self.mplayer.playlist:
        #     self.mplayer.music_player.setPlaylist(self.mplayer.playlist)
    # def save_event(self):
    #     directory = QFileDialog.getSaveFileName(self,'保存','.','*.wav;;*.mp3')
    #     if (directory == ('', '')):
    #         return

    def tree_itemdoubleclicked(self,item):
        url = QtCore.QUrl.fromLocalFile(item.text(0))
        content = QtMultimedia.QMediaContent(url)
        self.mplayer.music_player.setMedia(content)
        self.mplayer.reset()

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

        # 音量滑动条
        self.slider1 = QSlider(Qt.Vertical)
        slider2 = QSlider(Qt.Vertical)
        self.slider1.valueChanged.connect(self.volume_control)
        self.volume1 = QLabel(str(self.slider1.value()))
        self.volume1.setObjectName('volume')
        self.slider1.setValue(100)
        volume2 = QLabel(str(slider2.value()))
        volume2.setObjectName('volume')
        #打开，保存按钮
        open_btn= QPushButton(QIcon('./photos/load.png'),'打开')
        open_btn.setIconSize(QSize(30, 30))
        open_btn.setObjectName('smallbtn')
        open_btn.clicked.connect(self.open_event)
        # save_btn= QPushButton(QIcon('./photos/save.png'),"保存")
        # save_btn.setIconSize(QSize(30, 30))
        # save_btn.setObjectName('smallbtn')
        # save_btn.clicked.connect(self.save_event)
        self.record_btn = QPushButton(QIcon('./photos/record.png'), "录制")
        self.record_btn.setIconSize(QSize(30, 30))
        self.record_btn.setObjectName('smallbtn')
        self.record_btn.setCheckable(True)
        self.record_btn.clicked.connect(self.record_event)
        # 演奏模式选择按钮
        # self.choicebtn =  QPushButton("开启黑键")
        # self.choicebtn.setCheckable(True)
        # self.choicebtn.setObjectName('choicebtn')
        # 乐器选择
        self.ins1 = QPushButton("钢琴")
        self.ins1.setCheckable(True)
        self.ins1.setChecked(True)
        self.ins1.setAutoExclusive(True)
        self.ins1.setObjectName('btn')
        self.ins2 = QPushButton("bass")
        self.ins2.setCheckable(True)
        self.ins2.setAutoExclusive(True)
        self.ins2.setObjectName('btn')
        self.ins3 = QPushButton("ins3")
        self.ins3.setCheckable(True)
        self.ins3.setAutoExclusive(True)
        self.ins3.setObjectName('btn')
        self.ins4 = QPushButton("ins4")
        self.ins4.setCheckable(True)
        self.ins4.setAutoExclusive(True)
        self.ins4.setObjectName('btn')

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
        # glayout2.addWidget(self.choicebtn, 0, 0,1,2)
        glayout2.addWidget(self.ins1, 1, 0)
        glayout2.addWidget(self.ins2, 1, 1)
        glayout2.addWidget(self.ins3, 2, 0)
        glayout2.addWidget(self.ins4, 2, 1)
        ins_groupBox = QGroupBox("乐器选择")
        ins_groupBox.setLayout(glayout2)

        #文件树
        self.tree = QTreeWidget()
        # 设置树形控件头部的标题
        self.tree.setHeaderLabels(['文件名', '大小'])
        self.tree.setRootIsDecorated(False)
        # 宽度对内容变化
        self.tree.header().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tree.itemDoubleClicked.connect(self.tree_itemdoubleclicked)
        
        #播放器
        self.mplayer=Music_player()


        #file_groupbox
        vbox=QVBoxLayout()
        vbox.addWidget(open_btn)
        # vbox.addWidget(save_btn)
        vbox.addWidget(self.record_btn)
        hbox3=QHBoxLayout()
        hbox3.addLayout(vbox)
        hbox3.addWidget(self.tree)
        vbox2=QVBoxLayout()
        vbox2.addWidget(self.mplayer)
        vbox2.addLayout(hbox3)
        file_groupBox = QGroupBox("文件操作")
        file_groupBox.setLayout(vbox2)


        #音量，文件操作，乐器选择布局
        hbox = QHBoxLayout()
        hbox.addWidget(volume_groupBox)
        hbox.addWidget(ins_groupBox)
        # hbox.addStretch(1)
        hbox.addWidget(file_groupBox)
        # hbox.addLayout(player)


        #竖直布局
        vbox2 = QVBoxLayout()
        vbox2.addLayout(hbox)
        vbox2.addStretch()
        vbox2.addLayout(self.init_piano())
        vbox2.addStretch()
        # vbox2.setStretchFactor(hbox, 1)
        # vbox2.setStretchFactor(hbox, 1)
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