
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QTextBrowser


from user_cases.qt_ui_response import QtResponse as repo

class QtInit(repo):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.input_start()
        self.input_step()
        self.select_path()
        self.run_button()
        self.out_info()
        self.setGeometry(300, 300, 350, 340)
        self.setWindowTitle('Josephus Ring')
        self.show()

    def input_start(self):
        qtlabel = QLabel(self)
        start = QLineEdit(self)
        start.setPlaceholderText("请输入0~3位数字")
        qtlabel.move(20, 40)
        qtlabel.setText("Start:")
        start.move(60, 35)
        start.textChanged[str].connect(self.start_Changed)
        start.setText("3")
        #start.adjustSize()

    def input_step(self):
        qtlabel = QLabel(self)
        step = QLineEdit(self)
        step.setPlaceholderText("请输入0~3位数字")
        qtlabel.move(20, 70)
        qtlabel.setText("Step:")
        step.move(60, 65)
        step.textChanged[str].connect(self.step_Changed)
        step.setText("2")
        #step.adjustSize()

    def select_path(self):
        path_label = QLabel(self)
        path = QComboBox(self)
        path_label.move(20, 100)
        path_label.setText("File:")
        path.addItem("请下拉选择文件...")
        path.addItem("josephus_list1.csv")
        path.addItem("josephus_list2.txt")
        path.addItem("josephus.zip")
        path.move(60, 95)
        path.activated[str].connect(self.selceted_path)

    def run_button(self):
        run = QPushButton('RUN', self)
        run.move(150, 138)
        run.clicked.connect(self.click_run)
        #run.adjustSize()

    def out_info(self):
        self.info = QTextBrowser(self)
        self.info.move(30,180)
        self.info.resize(290,150)
        