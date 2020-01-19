import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget
from PyQt5.QtGui import QIcon


class FirstMainWin(QMainWindow):
    app = QApplication(sys.argv)

    def __init__(self):
        super(FirstMainWin, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("窗口应用")
        self.setGeometry(300, 300, 400, 280)
        self.status = self.statusBar()
        self.status.showMessage("只存在五秒的消息", 5000)
        self.setWindowIcon(QIcon("./images/s1.ico"))
        self.show()
        sys.exit(self.app.exec_())

    # 让窗口居中
    def center(self):
        # 获取屏幕坐标系
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口坐标系
        size = self.geometry()
        newLeft = (screen.width() - size.width()) / 2


f1 = FirstMainWin()
