import sys
from PyQt5.QtWidgets import QPushButton, QWidget, QDialog, QApplication, QMainWindow, QGraphicsScene, QGraphicsItem, \
    QGraphicsRectItem, QGraphicsSceneMouseEvent, QGraphicsEllipseItem, QFrame, QLabel
from PyQt5.QtCore import Qt, QMimeData, QPoint, QRect, QSize, QRectF, QSizeF, QPropertyAnimation, QTimeLine, QObject, \
    QTimer, QTime
from PyQt5.QtGui import QDrag, QImage, QColor
from PyQt5 import uic
import random
import winsound
from PyQt5.QtWidgets import (QApplication, QGraphicsView,
        QGraphicsPixmapItem, QGraphicsScene)
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtCore import (QObject, QPointF,
        QPropertyAnimation, pyqtProperty)
import sys

from PyQt5.uic.properties import QtGui
from Square import *
from Stopwatch import *
from View import *
COLS = 3
ROWS = 3
MARGIN = 40
#размер квадратика (мб потом станет прямоугольничком ,который не квадратик )
XYSIDE = 60
# это отступ для второго поля
MARGIN2 = 400
# квадратик ( элемент пазла ,мб в будущем переделан в прямоугольничек ,который не квадратик )
squares = []
START_TIME = 5

class MainWnd(QWidget):

    def __init__(self):
        super().__init__()
        initUI(self)
        self.stopWatch = Stopwatch(START_TIME,self.timer,self.btn_start_game,self.label_timer)


    def confirm(self):
        if self.stopWatch.sec == 0:
            print('вы проиграли')
        else:
            print('вы выиграли')

    def start_game(self):
        try:
            self.shuffle()
            self.stopWatch.start()
        except Exception as e:
            print(e)


    def shuffle(self):
        print('я начинаю мешать')
        numbers = [i for i in range(1,ROWS*COLS+1,1)]
        random.shuffle(numbers)
        self.set_img_numbers(numbers)


    def set_img_numbers(self,numbers):
        self.scene.clear()
        squares.clear()
        u = 0
        for y in range(COLS):
            for x in range(ROWS):
                obj = Square(x * XYSIDE, y * XYSIDE,numbers[u])
                self.scene.addItem(obj)
                squares.append(obj)
                u += 1

    def set_START_TIME(self,n):
        START_TIME = n



    def AnimeButton_clicked(self):
        try:
            self.animation = QPropertyAnimation(AnimSquare(squares[0]), b'pos')
            self.animation.setDuration(200)
            self.animation.setStartValue(QPointF(0, 0))
            self.animation.setKeyValueAt(0.3, QPointF(0, 30))
            self.animation.setKeyValueAt(0.5, QPointF(0, 60))
            self.animation.setKeyValueAt(0.8, QPointF(0, 90))
            self.animation.setEndValue(QPointF(0, 120))
            self.animation.start()
            '''
            self.animation = QPropertyAnimation(AnimSquare(squares[0]), b'angle')
            self.animation.setDuration(8000)
            self.animation.setStartValue(-90)
            self.animation.setKeyValueAt(0.3, -10)
            self.animation.setKeyValueAt(0.5, 0)
            self.animation.setKeyValueAt(0.8, 10)
            self.animation.setEndValue(30)
            self.animation.start()
            '''

        except Exception as e:
            print(e)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWnd()
    ex.show()
    app.exec_()
