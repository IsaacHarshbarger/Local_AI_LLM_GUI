from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QLabel, QPushButton, QBoxLayout, QCheckBox, QGridLayout, QMainWindow, QApplication)
import sys



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


    def initUI(self):
        pass



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()