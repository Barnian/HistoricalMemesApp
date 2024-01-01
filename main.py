import sys
from gui4 import Ui_MainWindow
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PIL import Image
from PyQt5.QtCore import Qt
from convertation.read_save import read
uip = 0

class ExampleApp(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        self.uip = 0
        self.kol = 'ww2'
        self.fg = {}
        self.av = read(self.kol)
        for i in self.av[2]:
            self.fg[i] = 0
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.fu()

    def pni(self):
        self.label_2.setText("")
        g = True
        for i in list(self.fg.keys()):
            if i != 'pressf':
                g = False
        if g:
            print("hjotr")
        self.pushButton_2.clicked.connect(self.fu)
        self.pushButton.clicked.connect(self.g)
        self.pushButton_3.clicked.connect(self.h)

    def h(self):

        p = list(self.fg.keys()).index(self.kol) + 1
        if p < len(list(self.fg.keys())):
            self.kol = list(self.fg.keys())[p]
            self.av = read(self.kol)
            self.uip = 0
        else:
            self.kol = list(self.fg.keys())[0]
            self.av = read(self.kol)
            self.uip = 0
        self.fu()

    def g(self):
        tx = read(self.kol)[1][self.uip - 1]
        self.label_2.setText(tx)
        self.label_2.setWordWrap(True)

    def fu(self):
        self.label_2.setText('')
        im = self.av[0][self.uip]
        self.uip += 1
        if im.mode == "RGB":
            r, g, b = im.split()
            im = Image.merge("RGB", (b, g, r))
        elif im.mode == "RGBA":
            r, g, b, a = im.split()
            im = Image.merge("RGBA", (b, g, r, a))
        elif im.mode == "L":
            im = im.convert("RGBA")
            # Bild in RGBA konvertieren, falls nicht bereits passiert
        im2 = im.convert("RGBA")
        data = im2.tobytes("raw", "RGBA")
        qim = QtGui.QImage(data, im.size[0], im.size[1], QtGui.QImage.Format_ARGB32)
        # k = self.label.width() / (self.label.height())
        # qim = qim.scaled(round(qim.height() / k), round(self.label.height()). Qt.keepAspectRatio)
        pixmap = QtGui.QPixmap.fromImage(qim).scaledToHeight(self.label.height())
        # k = pixmap.height() / pixmap.width()
        # pixmap.scaled(round(self.label.height() / k), self.label.height())

        self.label.setPixmap(pixmap)
        self.label.setAlignment(Qt.AlignCenter)
        if self.uip >= len(self.av[0]):
            print("sr")
            self.h()
        # self.label.setStyleSheet(f'margin-left: {(self.label.width() - pixmap.width()) / 2}px;')


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.pni()
    window.show()  # Показываем окно
    app.exec()  # и запускаем приложение



if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()
