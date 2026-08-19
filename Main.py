from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QLabel, QPushButton, QHBoxLayout, QCheckBox, QGridLayout, QMainWindow, QApplication, QWidget, QFrame, QGroupBox, QVBoxLayout, QRadioButton, QButtonGroup)
import sys



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.choose_ai = QLabel("Choose AI", self)
        self.llama3 = QRadioButton("Llama3", self)
        self.qwen314b = QRadioButton("Qwen3 (14B)", self)
        self.deepseekcoder = QRadioButton("DeepSeek Coder", self)
        self.deepseekr1 = QRadioButton("DeepSeek-r1 (14B)", self)
        self.choose_ai_group = QButtonGroup(self)

        self.choose_ai_checker = QLabel("Choose Fact Checker")
        self.cllama3 = QRadioButton("Llama3", self)
        self.cqwen314b = QRadioButton("Qwen3 (14B)", self)
        self.cdeepseekr1 = QRadioButton("DeepSeek-r1 (14B)", self)
        self.cnochecker = QRadioButton("None", self)
        self.choose_ai_checker_group = QButtonGroup(self)


        self.choose_ai.setObjectName("ailabels")
        self.choose_ai_checker.setObjectName("ailabels")


        self.ai_model = ""
        self.ai_checker_model = ""

        self.initUI()


    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)

        left_side_bar = QGroupBox("")

        divider = QFrame()
        # divider.setFrameShape(QFrame.VLine)

        divider.setStyleSheet("""
            background-color: black;
            min-width: 4px;
            max-width: 4px;
        """)

        right_side = QGroupBox("")

        main_layout.addWidget(left_side_bar, stretch=1)
        main_layout.addWidget(divider)
        main_layout.addWidget(right_side, stretch=3)

        left_side_layout = QVBoxLayout(left_side_bar)

        self.setStyleSheet("""
        QRadioButton{
            font-size: 30px;
            font-family: Arial;
        }
        QLabel#ailabels{
            font-size:35px;
            font-weight: bold;

        }
        """)

        left_side_layout.addWidget(self.choose_ai)


        self.choose_ai_group.addButton(self.llama3)
        self.choose_ai_group.addButton(self.qwen314b)
        self.choose_ai_group.addButton(self.deepseekcoder)
        self.choose_ai_group.addButton(self.deepseekr1)

        left_side_layout.addWidget(self.llama3)
        left_side_layout.addWidget(self.qwen314b)
        left_side_layout.addWidget(self.deepseekcoder)
        left_side_layout.addWidget(self.deepseekr1)


        left_side_layout.addWidget(self.choose_ai_checker)


        self.choose_ai_checker_group.addButton(self.cllama3)
        self.choose_ai_checker_group.addButton(self.cqwen314b)
        self.choose_ai_checker_group.addButton(self.cdeepseekr1)
        self.choose_ai_checker_group.addButton(self.cnochecker)

        left_side_layout.addWidget(self.cllama3)
        left_side_layout.addWidget(self.cqwen314b)
        left_side_layout.addWidget(self.cdeepseekr1)
        left_side_layout.addWidget(self.cnochecker)


        self.llama3.clicked.connect(self.func_choose_ai)
        self.qwen314b.clicked.connect(self.func_choose_ai)
        self.deepseekcoder.clicked.connect(self.func_choose_ai)
        self.deepseekr1.clicked.connect(self.func_choose_ai)

        self.cllama3.clicked.connect(self.choose_checker)
        self.cqwen314b.clicked.connect(self.choose_checker)
        self.cdeepseekr1.clicked.connect(self.choose_checker)
        self.cnochecker.clicked.connect(self.choose_checker)



    def func_choose_ai(self):
        button = self.sender()
        text = button.text()

        match text:
            case "Llama3":
                self.ai_model = "llama3"
            case "DeepSeek Coder":
                self.ai_model = "deepseek-coder"
            case "Qwen3 (14B)":
                self.ai_model = "qwen3:14b"
            case "DeepSeek-r1 (14B)":
                self.ai_model = "deepseek-r1:14b"
            case _:
                print("Something went wrong: func_choose_ai")

        print(f"Ai model: {self.ai_model}")


    def choose_checker(self):
        button = self.sender()
        text = button.text()

        match text:
            case "Llama3":
                self.ai_checker_model = "llama3"
            case "Qwen3 (14B)":
                self.ai_checker_model = "qwen3:14b"
            case "DeepSeek-r1 (14B)":
                self.ai_checker_model = "deepseek-r1:14b"
            case "None":
                self.ai_checker_model = None
            case _:
                print("Something went wrong: choose_checker")      

        print(f"Checker model: {self.ai_checker_model}")







def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()