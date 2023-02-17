from PyQt5 import QtCore, QtGui, QtWidgets
from images import resource_rc


class Loading_UI(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(550, 650)
        self.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.setStyleSheet("#centralwidget{\n"
                           "    background-color: rgb(0, 0, 0);\n"
                           "}\n"
                           "#main_frame{\n"
                           "    background-color: ;\n"
                           "    background-color: rgb(0, 0, 0);\n"
                           "    border-radius:15px;\n"
                           "    margin:0px\n"
                           "}")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.main_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.main_frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.logo_image = QtWidgets.QLabel(self.main_frame)
        self.logo_image.setMinimumSize(QtCore.QSize(0, 420))
        self.logo_image.setStyleSheet("")
        self.logo_image.setText("")
        self.logo_image.setPixmap(QtGui.QPixmap(":/images/logo_with_name.jpg"))
        self.logo_image.setAlignment(QtCore.Qt.AlignCenter)
        self.logo_image.setObjectName("logo_image")
        self.verticalLayout.addWidget(
            self.logo_image, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.loading_gif = QtWidgets.QLabel(self.main_frame)
        self.loading_gif.setEnabled(True)
        self.loading_gif.setMinimumSize(QtCore.QSize(60, 60))
        self.loading_gif.setStyleSheet("padding-left:12px;")
        self.loading_gif.setText("")
        self.loading_gif.setObjectName("loading_gif")
        self.gif = QtGui.QMovie('images/splash.gif')
        self.gif.start()
        self.loading_gif.setMovie(self.gif)
        self.verticalLayout.addWidget(
            self.loading_gif, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.developers_info = QtWidgets.QLabel(self.main_frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.developers_info.sizePolicy().hasHeightForWidth())
        self.developers_info.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Chilanka")
        font.setBold(True)
        font.setWeight(75)
        self.developers_info.setFont(font)
        self.developers_info.setStyleSheet("color: rgb(255, 255, 255);")
        self.developers_info.setAlignment(QtCore.Qt.AlignCenter)
        self.developers_info.setObjectName("developers_info")
        self.verticalLayout.addWidget(
            self.developers_info, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom)
        self.gridLayout.addWidget(self.main_frame, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 2, 1, 1)
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate(
            "MainWindow", "Senaya - Virtual Assistant"))
        self.developers_info.setText(_translate(
            "MainWindow", "<html><head/><body><p>Made with 💓 By Manoj</p></body></html>"))
