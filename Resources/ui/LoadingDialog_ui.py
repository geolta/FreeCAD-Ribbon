# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoadingDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QProgressBar, QSizePolicy,
    QWidget)

class Ui_LoadingwokrbenchesLoadingDialog(object):
    def setupUi(self, LoadingwokrbenchesLoadingDialog):
        if not LoadingwokrbenchesLoadingDialog.objectName():
            LoadingwokrbenchesLoadingDialog.setObjectName(u"LoadingwokrbenchesLoadingDialog")
        LoadingwokrbenchesLoadingDialog.resize(400, 42)
        self.gridLayout = QGridLayout(LoadingwokrbenchesLoadingDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.progressBar = QProgressBar(LoadingwokrbenchesLoadingDialog)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)
        self.progressBar.setInvertedAppearance(False)

        self.gridLayout.addWidget(self.progressBar, 0, 0, 1, 1)


        self.retranslateUi(LoadingwokrbenchesLoadingDialog)

        QMetaObject.connectSlotsByName(LoadingwokrbenchesLoadingDialog)
    # setupUi

    def retranslateUi(self, LoadingwokrbenchesLoadingDialog):
        LoadingwokrbenchesLoadingDialog.setWindowTitle(QCoreApplication.translate("LoadingwokrbenchesLoadingDialog", u"Loading workbenches", None))
    # retranslateUi

