from PyQt5 import QtCore, QtGui, QtWidgets
from chat_utils import place_question
from utils import load_about_ui, ask_question, recognize_speech, text_to_speech, open_in_browser, translate_handler
from images import resource_rc


class Chat_UI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.row_index = 2
        self.is_recording_started = False
        self.frame_index = 1
        self.label_index = 1
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Form")
        self.resize(559, 650)
        self.setMinimumSize(QtCore.QSize(550, 0))
        self.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.setStyleSheet("#Form{\n"
                           "    background-color: rgb(0, 0, 0);\n"
                           "}\n"
                           "\n"
                           "#main_frame{    \n"
                           "    background-color: rgb(0, 0, 0);\n"
                           "    margin:0px;\n"
                           "    padding:0px;\n"
                           "}\n"
                           "\n"
                           "#chat_area{\n"
                           "    margin:0px;\n"
                           "    padding:0px;\n"
                           "    border:none;\n"
                           "}")
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.main_frame = QtWidgets.QFrame(self)
        self.main_frame.setMinimumSize(QtCore.QSize(0, 0))
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.main_frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_area = QtWidgets.QFrame(self.main_frame)
        self.top_area.setMaximumSize(QtCore.QSize(16777215, 50))
        self.top_area.setStyleSheet("#top_area{\n"
                                    "    border:2px solid rgb(97, 53, 131);\n"
                                    "    border-radius:15px;\n"
                                    "}")
        self.top_area.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_area.setObjectName("top_area")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.top_area)
        self.horizontalLayout.setContentsMargins(15, 8, 15, 8)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.logo_btn = QtWidgets.QPushButton(self.top_area)
        self.logo_btn.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                    "border:none;")
        self.logo_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/log.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logo_btn.setIcon(icon)
        self.logo_btn.setIconSize(QtCore.QSize(28, 28))
        self.logo_btn.setCheckable(False)
        self.logo_btn.setObjectName("logo_btn")
        self.logo_btn.clicked.connect(load_about_ui)
        self.horizontalLayout.addWidget(self.logo_btn)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.title_label = QtWidgets.QLabel(self.top_area)
        self.title_label.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Dyuthi")
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet("#title_label{\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "}")
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.horizontalLayout.addWidget(self.title_label)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.top_area)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(3, 1)
        self.verticalLayout.addWidget(self.top_area, 0, QtCore.Qt.AlignTop)
        self.chat_area_frame = QtWidgets.QFrame(self.main_frame)
        self.chat_area_frame.setMinimumSize(QtCore.QSize(0, 470))
        self.chat_area_frame.setStyleSheet("#chat_area_frame{\n"
                                           "    border:1px solid rgb(26, 95, 180);\n"
                                           "    border-radius:15px;\n"
                                           "}")
        self.chat_area_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.chat_area_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.chat_area_frame.setObjectName("chat_area_frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.chat_area_frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.chat_area = QtWidgets.QScrollArea(self.chat_area_frame)
        self.chat_area.setStyleSheet("#chat_area{\n"
                                     "    background-color: rgb(0, 0, 0);\n"
                                     "}\n"
                                     "\n"
                                     "\n"
                                     " QScrollBar:vertical {\n"
                                     "    border: none;\n"
                                     "    background: rgb(45, 45, 68);\n"
                                     "    width: 10px;\n"
                                     "    margin: 15px 0 15px 0;\n"
                                     "    border-radius: 2px;\n"
                                     " }\n"
                                     "\n"
                                     "/*  HANDLE BAR VERTICAL */\n"
                                     "QScrollBar::handle:vertical {    \n"
                                     "    background-color: rgb(80, 80, 122);\n"
                                     "    min-height: 30px;\n"
                                     "    border-radius: 7px;\n"
                                     "}\n"
                                     "QScrollBar::handle:vertical:hover{    \n"
                                     "    background-color: rgb(26, 95, 180);\n"
                                     "}\n"
                                     "QScrollBar::handle:vertical:pressed {    \n"
                                     "    background-color: rgb(26, 95, 180);\n"
                                     "}\n"
                                     "\n"
                                     "/* BTN TOP - SCROLLBAR */\n"
                                     "QScrollBar::sub-line:vertical {\n"
                                     "    border: none;\n"
                                     "    background-color: rgb(59, 59, 90);\n"
                                     "    height: 15px;\n"
                                     "    border-top-left-radius: 7px;\n"
                                     "    border-top-right-radius: 7px;\n"
                                     "    subcontrol-position: top;\n"
                                     "    subcontrol-origin: margin;\n"
                                     "}\n"
                                     "QScrollBar::sub-line:vertical:hover {    \n"
                                     "    background-color: rgb(255, 0, 127);\n"
                                     "}\n"
                                     "QScrollBar::sub-line:vertical:pressed {    \n"
                                     "    background-color: rgb(185, 0, 92);\n"
                                     "}\n"
                                     "\n"
                                     "/* BTN BOTTOM - SCROLLBAR */\n"
                                     "QScrollBar::add-line:vertical {\n"
                                     "    border: none;\n"
                                     "    background-color: rgb(59, 59, 90);\n"
                                     "    height: 15px;\n"
                                     "    border-bottom-left-radius: 7px;\n"
                                     "    border-bottom-right-radius: 7px;\n"
                                     "    subcontrol-position: bottom;\n"
                                     "    subcontrol-origin: margin;\n"
                                     "}\n"
                                     "QScrollBar::add-line:vertical:hover {    \n"
                                     "    background-color: rgb(255, 0, 127);\n"
                                     "}\n"
                                     "QScrollBar::add-line:vertical:pressed {    \n"
                                     "    background-color: rgb(185, 0, 92);\n"
                                     "}\n"
                                     "\n"
                                     "/* RESET ARROW */\n"
                                     "QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
                                     "    background: none;\n"
                                     "}\n"
                                     "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
                                     "    background: none;\n"
                                     "}\n"
                                     "")
        self.chat_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.chat_area.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.chat_area.setWidgetResizable(True)
        self.chat_area.setObjectName("chat_area")
        self.chat_area_content = QtWidgets.QWidget()
        self.chat_area_content.setGeometry(QtCore.QRect(0, 0, 499, 448))
        self.chat_area_content.setStyleSheet("#chat_area_content{\n"
                                             "    background-color: rgb(0, 0, 0);\n"
                                             "}\n"
                                             "\n"
                                             "QFrame{\n"
                                             "    border: 1px solid rgb(97, 53, 131);\n"
                                             "    border-radius:25px;\n"
                                             "}\n"
                                             "\n"
                                             "QLabel{\n"
                                             "    border:none;\n"
                                             "    color: rgb(255, 255, 255);\n"
                                             "}")
        self.chat_area_content.setObjectName("chat_area_content")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.chat_area_content)
        self.gridLayout_3.setContentsMargins(5, -1, 5, -1)
        self.gridLayout_3.setHorizontalSpacing(15)
        self.gridLayout_3.setVerticalSpacing(10)
        self.gridLayout_3.setObjectName("gridLayout_3")

        frame_s_1 = QtWidgets.QFrame(self.chat_area_content)
        frame_s_1.setMinimumSize(QtCore.QSize(210, 1))
        frame_s_1.setMaximumSize(QtCore.QSize(16777215, 1))
        frame_s_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        frame_s_1.setFrameShadow(QtWidgets.QFrame.Raised)
        frame_s_1.setObjectName("frame_s_1")
        frame_s_1.setStyleSheet("#frame_s_1{\n"
                                "    border:none;\n"
                                "}")
        verticalLayout_3 = QtWidgets.QVBoxLayout(frame_s_1)
        verticalLayout_3.setObjectName("verticalLayout_3")
        label_s_1 = QtWidgets.QLabel(frame_s_1)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(11)
        label_s_1.setFont(font)
        label_s_1.setStyleSheet("")
        label_s_1.setWordWrap(True)
        label_s_1.setObjectName("label_s_1")
        verticalLayout_3.addWidget(label_s_1)
        self.gridLayout_3.addWidget(frame_s_1, 0, 1, 1, 1)
        frame_s_2 = QtWidgets.QFrame(self.chat_area_content)
        frame_s_2.setMinimumSize(QtCore.QSize(210, 1))
        frame_s_2.setMaximumSize(QtCore.QSize(16777215, 1))
        frame_s_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        frame_s_2.setFrameShadow(QtWidgets.QFrame.Raised)
        frame_s_2.setObjectName("frame_s_2")
        frame_s_2.setStyleSheet("#frame_s_2{\n"
                                "    border:none;\n"
                                "}")
        verticalLayout_4 = QtWidgets.QVBoxLayout(frame_s_2)
        verticalLayout_4.setObjectName("verticalLayout_4")
        label_s_2 = QtWidgets.QLabel(frame_s_2)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(11)
        label_s_2.setFont(font)
        label_s_2.setStyleSheet("")
        label_s_2.setWordWrap(True)
        label_s_2.setObjectName("label_s_2")
        verticalLayout_4.addWidget(label_s_2)
        self.gridLayout_3.addWidget(frame_s_2, 1, 0, 1, 1)
        self.chat_spacer_1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(
            self.chat_spacer_1, 2, 0, 1, 1)
        self.chat_spacer_2 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(
            self.chat_spacer_2, 2, 1, 1, 1)
        self.chat_area.setWidget(self.chat_area_content)
        self.gridLayout_2.addWidget(self.chat_area, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.chat_area_frame)
        self.bottom_area = QtWidgets.QFrame(self.main_frame)
        self.bottom_area.setMinimumSize(QtCore.QSize(0, 80))
        self.bottom_area.setMaximumSize(QtCore.QSize(16777215, 80))
        self.bottom_area.setStyleSheet("#bottom_area{\n"
                                       "    border:2px solid rgb(97, 53, 131);\n"
                                       "    border-radius:15px;\n"
                                       "}")
        self.bottom_area.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bottom_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom_area.setObjectName("bottom_area")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.bottom_area)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.user_input = QtWidgets.QTextEdit(self.bottom_area)
        self.user_input.setMinimumSize(QtCore.QSize(350, 50))
        self.user_input.setStyleSheet("#user_input{\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "    background-color: rgb(0, 0, 0);\n"
                                      "    border:1px solid rgb(255,255,255);\n"
                                      "    border-radius:15px;\n"
                                      "    padding-top:5px;\n"
                                      "    padding-left:7px;\n"
                                      "    padding-bottom:5px;    \n"
                                      "    padding-right:7px;\n"
                                      "    font-family:MS Shell Dlg 2;\n"
                                      "    font-size:15px;\n"
                                      "}\n"
                                      "\n"
                                      "#user_input:focus{\n"
                                      "    \n"
                                      "    border-color: rgb(73, 168, 53);\n"
                                      "}")
        self.user_input.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.user_input.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.user_input.setObjectName("user_input")
        self.horizontalLayout_2.addWidget(self.user_input)
        self.buttons_frame = QtWidgets.QFrame(self.bottom_area)
        self.buttons_frame.setStyleSheet("#buttons_frame{\n"
                                         "border:none;\n"
                                         "}")
        self.buttons_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttons_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttons_frame.setObjectName("buttons_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.buttons_frame)
        self.horizontalLayout_3.setContentsMargins(-1, 4, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.mic_btn = QtWidgets.QPushButton(self.buttons_frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.mic_btn.sizePolicy().hasHeightForWidth())
        self.mic_btn.setSizePolicy(sizePolicy)
        self.mic_btn.setMinimumSize(QtCore.QSize(50, 50))
        self.mic_btn.setMaximumSize(QtCore.QSize(80, 80))
        self.mic_btn.setStyleSheet("#mic_btn{    \n"
                                   "    color: rgb(255, 255, 255);\n"
                                   "    background-color: rgb(0, 0, 0);\n"
                                   "    border:1px solid rgb(255,255,255);\n"
                                   "    border-radius:25px;\n"
                                   "}\n"
                                   "\n"
                                   "#mic_btn:hover{\n"
                                   "    border-color: rgb(97, 53, 131);\n"
                                   "}")
        self.mic_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/mic.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mic_btn.setIcon(icon1)
        self.mic_btn.setIconSize(QtCore.QSize(25, 25))
        self.mic_btn.setObjectName("mic_btn")
        self.mic_btn.clicked.connect(self.mic_btn_action)
        self.horizontalLayout_3.addWidget(self.mic_btn)
        self.send_btn = QtWidgets.QPushButton(self.buttons_frame)
        self.send_btn.clicked.connect(self.send_btn_action)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.send_btn.sizePolicy().hasHeightForWidth())
        self.send_btn.setSizePolicy(sizePolicy)
        self.send_btn.setMinimumSize(QtCore.QSize(50, 50))
        self.send_btn.setMaximumSize(QtCore.QSize(80, 80))
        self.send_btn.setStyleSheet("#send_btn{    \n"
                                    "    color: rgb(255, 255, 255);\n"
                                    "    background-color: rgb(0, 0, 0);\n"
                                    "    border:1px solid rgb(255,255,255);\n"
                                    "    border-radius:25px;\n"
                                    "}\n"
                                    "#send_btn:hover{\n"
                                    "    border-color: rgb(97, 53, 131);\n"
                                    "}")
        self.send_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/send.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.send_btn.setIcon(icon2)
        self.send_btn.setIconSize(QtCore.QSize(25, 25))
        self.send_btn.setObjectName("send_btn")
        self.horizontalLayout_3.addWidget(self.send_btn)
        self.horizontalLayout_2.addWidget(self.buttons_frame)
        self.horizontalLayout_2.setStretch(0, 1)
        self.verticalLayout.addWidget(
            self.bottom_area, 0, QtCore.Qt.AlignBottom)
        self.gridLayout.addWidget(self.main_frame, 0, 0, 1, 1)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Osana - Virtual Assistant"))
        self.logo_btn.setToolTip(_translate(
            "Form", "<html><head/><body><p><span style=\" color:#ffffff;\">Click to check App\'s Info</span></p></body></html>"))
        self.logo_btn.setShortcut(_translate("Form", "Ctrl+S"))
        self.title_label.setText(_translate("Form", "Osana"))
        self.label.setToolTip(_translate(
            "Form", "<html><head/><body><p><span style=\" color:#000000;\">You are offline</span></p></body></html>"))
        self.label.setText(_translate("Form", "offline"))
        self.user_input.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.mic_btn.setShortcut(_translate("Form", "M"))
        self.send_btn.setShortcut(_translate("Form", "Return"))

    def send_btn_action(self):
        question = self.user_input.toPlainText()
        only_spaces = True
        for i in question:
            if ord(i) != ord(' '):
                only_spaces = False
        if not only_spaces:
            self.send_btn.setDisabled(True)
            self.mic_btn.setDisabled(True)
            place_question(self)
            ask_question(self, question)

    def mic_btn_action(self):
        if not self.is_recording_started:
            self.is_recording_started = True
            self.send_btn.setEnabled(False)
            recognize_speech(self)
        else:
            self.is_recording_started = False
            self.mic_btn.setEnabled(False)
            self.mic_btn.setStyleSheet("#mic_btn{    \n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    background-color: rgb(0, 0, 0);\n"
                                       "    border:1px solid rgb(255,255,255);\n"
                                       "    border-radius:25px;\n"
                                       "}\n"
                                       "\n"
                                       "#mic_btn:hover{\n"
                                       "    border-color: rgb(97, 53, 131);\n"
                                       "}")

    def eventFilter(self, source, event):
        if (event.type() == QtCore.QEvent.ContextMenu) and (type(source) == QtWidgets.QLabel):
            menu = QtWidgets.QMenu()
            translate_action = QtWidgets.QAction("Translate")
            translate_action.triggered.connect(
                lambda: translate_handler(source, source.text()))
            speech_action = QtWidgets.QAction("Speech")
            speech_action.triggered.connect(
                lambda: text_to_speech(self, source.text()))
            open_browser_action = QtWidgets.QAction("Open in browser")
            open_browser_action.triggered.connect(
                lambda: open_in_browser(source.text()))
            menu.addAction(translate_action)
            menu.addAction(speech_action)
            menu.addAction(open_browser_action)
            menu.setStyleSheet("""
                                QMenu {
                                    background-color: black;
                                    border: 2px solid purple;
                                    border-radius: 15px;
                                    color: white;
                                }
                                """)
            menu.exec(event.globalPos())
        return super().eventFilter(source, event)
