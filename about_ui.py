from PyQt5 import QtCore, QtGui, QtWidgets
from images import resource_rc


class About_UI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Form")
        self.resize(450, 470)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/log.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setStyleSheet("#From{\n"
                           "    background-color: rgb(0, 0, 0);\n"
                           "}\n"
                           "\n"
                           "#main_frame{\n"
                           "    background-color: rgb(0, 0, 0);\n"
                           "    border: 2px solid rgb(97, 53, 131);\n"
                           "}")
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.main_frame = QtWidgets.QFrame(self)
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.main_frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.logo_and_title = QtWidgets.QFrame(self.main_frame)
        self.logo_and_title.setStyleSheet("#logo_and_title{\n"
                                          "    border:none;\n"
                                          "    border-bottom:2px solid rgb(97, 53, 131);\n"
                                          "}\n"
                                          "")
        self.logo_and_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logo_and_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo_and_title.setObjectName("logo_and_title")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.logo_and_title)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.logo = QtWidgets.QLabel(self.logo_and_title)
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(":/images/log.png"))
        self.logo.setScaledContents(False)
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName("logo")
        self.horizontalLayout.addWidget(self.logo)
        self.title = QtWidgets.QLabel(self.logo_and_title)
        font = QtGui.QFont()
        font.setFamily("Yrsa")
        font.setPointSize(40)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setStyleSheet("color: rgb(255, 255, 255);")
        self.title.setScaledContents(True)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.horizontalLayout.addWidget(self.title)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)
        self.verticalLayout.addWidget(self.logo_and_title)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.informations = QtWidgets.QFrame(self.main_frame)
        self.informations.setStyleSheet("QLabel{\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "}\n"
                                        "\n"
                                        "#informations{\n"
                                        "    border:none;\n"
                                        "}")
        self.informations.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.informations.setFrameShadow(QtWidgets.QFrame.Raised)
        self.informations.setObjectName("informations")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.informations)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.informations)
        font = QtGui.QFont()
        font.setFamily("Dyuthi")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("margin-left:10px;\n"
                                 "margin-right:10px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_2.addItem(spacerItem1)
        self.info_labels = QtWidgets.QFrame(self.informations)
        self.info_labels.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.info_labels.setStyleSheet("#info_labels{\n"
                                       "border:none;\n"
                                       "}")
        self.info_labels.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.info_labels.setFrameShadow(QtWidgets.QFrame.Raised)
        self.info_labels.setObjectName("info_labels")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.info_labels)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setHorizontalSpacing(20)
        self.gridLayout_2.setVerticalSpacing(10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.info_labels)
        font = QtGui.QFont()
        font.setFamily("Dyuthi")
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setOpenExternalLinks(True)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.info_labels)
        font = QtGui.QFont()
        font.setFamily("Dyuthi")
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setOpenExternalLinks(True)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.info_labels)
        font = QtGui.QFont()
        font.setFamily("Dyuthi")
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 1, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.info_labels)
        spacerItem4 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_2.addItem(spacerItem4)
        self.label_5 = QtWidgets.QLabel(self.informations)
        font = QtGui.QFont()
        font.setFamily("Gargi")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.verticalLayout.addWidget(self.informations)
        spacerItem5 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.bottom_area = QtWidgets.QFrame(self.main_frame)
        self.bottom_area.setStyleSheet("#bottom_area{\n"
                                       "    border:none;\n"
                                       "}")
        self.bottom_area.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bottom_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom_area.setObjectName("bottom_area")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.bottom_area)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem6 = QtWidgets.QSpacerItem(
            155, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.close_btn = QtWidgets.QPushButton(self.bottom_area)
        self.close_btn.setStyleSheet("#close_btn{    \n"
                                     "    background-color: rgb(0, 0, 0);\n"
                                     "    color: rgb(255, 255, 255);\n"
                                     "    border: 1px solid white;\n"
                                     "    border-radius:15px;\n"
                                     "    padding: 8px 20px 8px 20px ;\n"
                                     "\n"
                                     "}\n"
                                     "#close_btn:hover{    \n"
                                     "    border-color: rgb(97, 53, 131);\n"
                                     "}")
        self.close_btn.setObjectName("close_btn")
        self.close_btn.clicked.connect(lambda: self.close())
        self.horizontalLayout_2.addWidget(self.close_btn)
        spacerItem7 = QtWidgets.QSpacerItem(
            155, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.verticalLayout.addWidget(self.bottom_area)
        self.verticalLayout.setStretch(2, 1)
        self.gridLayout.addWidget(self.main_frame, 0, 0, 1, 1)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "About Senaya"))
        self.title.setText(_translate("Form", "Senaya"))
        self.label.setText(_translate(
            "Form", "<html><head/><body><p>Senaya is the first Virtual Assistant developed by a Sri Lankan.</p></body></html>"))
        self.label_3.setText(_translate(
            "Form", "<html><head/><body><p>WebSite:- <a href=\"http://osanaai.000webhostapp.com/\"><span style=\" text-decoration: underline; color:#0000ff;\">senayaai.com</span></a></p></body></html>"))
        self.label_4.setText(_translate(
            "Form", "<html><head/><body><p>Github:- <a href=\"https://github.com/manojdilz/senaya-ai-assistant\"><span style=\" text-decoration: underline; color:#0000ff;\">github.com/manojdilz</span></a></p></body></html>"))
        self.label_2.setText(_translate(
            "Form", "Developed by Manoj Dilshan"))
        self.label_5.setText(_translate(
            "Form", "<html><head/><body><p>Copyright 2023 @Manoj</p></body></html>"))
        self.close_btn.setText(_translate("Form", "Close"))
