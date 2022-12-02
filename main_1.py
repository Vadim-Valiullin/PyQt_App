from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
import sys
import time

from PyQt5.QtWidgets import QMessageBox

import design


class Programm(QtWidgets.QMainWindow):

    def __init__(self):
        super(Programm, self).__init__()
        self.ui = design.Ui_App()
        self.ui.setupUi(self)
        self.ui.refreshButton.clicked.connect(self.validate_ip)
        self.ui.lineEdit.setPlaceholderText('192.168.1.0')      # Пример строки на вводе
        self.ui.lineEdit.clear()  # Удаляет текст из поля ввода после нажатия на кнопку
        self.timer = QTimer()
        self.ui.listWidget.scrollToBottom()    # Позволяет оставаться списку подсетей при добавлении в окно в самом начале

    def fill_data(self):
        self.ui.listWidget.clear()
        address = self.ui.lineEdit.text()[:10]
        for i in range(256):
            self.ui.listWidget.addItem(f'{address}{i}')
            self.ui.progressBar.setProperty("value", 100/256*i)
            time.sleep(0.1)

    def validate_ip(self):
        a = self.ui.lineEdit.text().split('.')
        print(a)
        if len(a) != 4:
            return QMessageBox.information(self, 'Input information_1', 'Write correct address')   # Отображает всплывающее окно об ошибке ввода
        for x in a:
            if not x.isdigit():
                return QMessageBox.information(self, 'Input information_2', 'Write correct address')
            i = int(x)
            if i < 0 or i > 255:
                return QMessageBox.information(self, 'Input information_3', 'Write correct address')
        return self.fill_data()

def application():
    app = QtWidgets.QApplication(sys.argv)
    window = Programm()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    application()
