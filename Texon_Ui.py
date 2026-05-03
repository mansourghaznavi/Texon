# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Texon_Ui.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QTextEdit, QWidget)

class Ui_page(object):
    def setupUi(self, page):
        if not page.objectName():
            page.setObjectName(u"page")
        page.resize(750, 531)
        page.setAutoFillBackground(False)
        page.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	color:#4d4d4d;\n"
"	border-radius:10px;\n"
"	border:1px solid #ccc;\n"
"	background-color:white;\n"
"	padding: 6px ,8px;\n"
"	font-family:\"Segoe UI \" , \"Tahoma\";\n"
"    font-size:13px;\n"
"	\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(220, 220, 220);\n"
"	border:1px solid #b25a4d;\n"
"\n"
"}\n"
"\n"
"QLabel{\n"
"	background-color:rgba(178,90,77,0.6);\n"
"    min-width: 300px;\n"
"	min-height: 60px;\n"
"	font-size : 14pt;\n"
"	font-family:\"Segeo UI\";\n"
"	qproperty-alignment: 'AlignCenter';\n"
"	border-radius:10px;\n"
"}")
        self.txt_input = QTextEdit(page)
        self.txt_input.setObjectName(u"txt_input")
        self.txt_input.setGeometry(QRect(70, 20, 611, 221))
        self.txt_input.setStyleSheet(u"#page{\n"
"	background-color:f0f0f0;\n"
"\n"
"}\n"
"\n"
"#txt_input{\n"
"	background-color:rgba(178,90,77,0.77);\n"
"       font-size:30px;\n"
"	color:white;\n"
"	border-radius:8px;\n"
"	padding:10px;\n"
"	font-family: 'Segeo Ui',sans-serif;\n"
"	\n"
"}")
        self.txt_upper = QPushButton(page)
        self.txt_upper.setObjectName(u"txt_upper")
        self.txt_upper.setGeometry(QRect(90, 263, 101, 31))
        self.txt_lower = QPushButton(page)
        self.txt_lower.setObjectName(u"txt_lower")
        self.txt_lower.setGeometry(QRect(220, 263, 101, 31))
        self.txt_copitalize = QPushButton(page)
        self.txt_copitalize.setObjectName(u"txt_copitalize")
        self.txt_copitalize.setGeometry(QRect(350, 263, 101, 31))
        self.txt_reverse = QPushButton(page)
        self.txt_reverse.setObjectName(u"txt_reverse")
        self.txt_reverse.setGeometry(QRect(480, 263, 111, 31))
        self.del_additional_space = QPushButton(page)
        self.del_additional_space.setObjectName(u"del_additional_space")
        self.del_additional_space.setGeometry(QRect(250, 300, 161, 31))
        self.count_words = QPushButton(page)
        self.count_words.setObjectName(u"count_words")
        self.count_words.setGeometry(QRect(430, 300, 141, 31))
        self.count_char = QPushButton(page)
        self.count_char.setObjectName(u"count_char")
        self.count_char.setGeometry(QRect(110, 300, 111, 31))
        self.lab_words = QLabel(page)
        self.lab_words.setObjectName(u"lab_words")
        self.lab_words.setGeometry(QRect(60, 370, 300, 101))
        self.lab_words.setStyleSheet(u"")
        self.lab_char = QLabel(page)
        self.lab_char.setObjectName(u"lab_char")
        self.lab_char.setGeometry(QRect(380, 370, 300, 101))
        self.lab_char.setMinimumSize(QSize(300, 60))

        self.retranslateUi(page)

        QMetaObject.connectSlotsByName(page)
    # setupUi

    def retranslateUi(self, page):
        page.setWindowTitle(QCoreApplication.translate("page", u"Dialog", None))
        self.txt_upper.setText(QCoreApplication.translate("page", u"To Upper Case", None))
        self.txt_lower.setText(QCoreApplication.translate("page", u"To Lower Case", None))
        self.txt_copitalize.setText(QCoreApplication.translate("page", u"To Copitalize", None))
        self.txt_reverse.setText(QCoreApplication.translate("page", u"Reverse words", None))
        self.del_additional_space.setText(QCoreApplication.translate("page", u"Delete Additional Space", None))
        self.count_words.setText(QCoreApplication.translate("page", u"Count Words", None))
        self.count_char.setText(QCoreApplication.translate("page", u"Count Charcters", None))
        self.lab_words.setText("")
        self.lab_char.setText("")
    # retranslateUi

