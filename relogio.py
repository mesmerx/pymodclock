#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import math
class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):      
        self.lcd = QLCDNumber(self)
        self.sld = QSlider(Qt.Horizontal, self)
        self.actual=12
        vbox = QVBoxLayout()
        vbox.addWidget(self.lcd)
        vbox.addWidget(self.sld)

        self.setLayout(vbox)
        self.sld.valueChanged.connect(self.changeclock)
        self.sld.valueChanged.connect(self.lcd.display)
        self.setGeometry(100, 100, 100, 50)
        self.setWindowTitle('Points')
        self.show()

    def changeclock(self):

        self.actual=self.sld.value()%12
        if self.actual==0: self.actual=12
        self.update()

    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        self.drawPoints(qp)
        qp.end()
    

    def drawPoints(self, qp):
        r=100
        points=12
        angle=int(360/points)
        pen = QPen(Qt.red, 10)
        qp.setPen(pen) 
        size = self.size() 
        center=(size.width()/2-90,size.height()/2)
        qp.drawEllipse(center[0],center[1],10,10)
        i=+2
        for a in range(0,360,angle):
            i=i%12 
            i+=1
            x=center[0]+math.cos(math.radians(a))*r
            y=center[1]+math.sin(math.radians(a))*r
            if i==self.actual:
                pen = QPen(Qt.red, 10)
                qp.setPen(pen)
            else:
                qp.setPen(QColor(168, 34, 3))
                qp.setFont(QFont('Decorative', 10))
            qp.drawEllipse(x,y,10,10)
            if i==12:
                text=str(i)+'/0'
            else:
                text=str(i)
            qp.drawText(x+math.cos(math.radians(a))*20,
                        y+math.sin(math.radians(a))*20+8,text)



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
