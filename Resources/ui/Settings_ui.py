# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SettingsjNXhnW.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowModality(Qt.WindowModal)
        Form.resize(580, 724)
        Form.setAutoFillBackground(False)
        self.gridLayout_7 = QGridLayout(Form)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.GenerateJson = QPushButton(Form)
        self.GenerateJson.setObjectName(u"GenerateJson")

        self.gridLayout_6.addWidget(self.GenerateJson, 0, 4, 1, 1)

        self.GenerateJsonExit = QPushButton(Form)
        self.GenerateJsonExit.setObjectName(u"GenerateJsonExit")

        self.gridLayout_6.addWidget(self.GenerateJsonExit, 0, 5, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_2, 0, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.RestoreJson = QPushButton(Form)
        self.RestoreJson.setObjectName(u"RestoreJson")
        self.RestoreJson.setEnabled(True)

        self.gridLayout_6.addWidget(self.RestoreJson, 0, 2, 1, 1)

        self.ResetJson = QPushButton(Form)
        self.ResetJson.setObjectName(u"ResetJson")
        self.ResetJson.setEnabled(True)

        self.gridLayout_6.addWidget(self.ResetJson, 0, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_6, 1, 0, 1, 1)

        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(u"")
        self.tabWidget.setElideMode(Qt.ElideRight)
        self.General = QWidget()
        self.General.setObjectName(u"General")
        self.General.setEnabled(True)
        self.General.setAutoFillBackground(True)
        self.gridLayout_9 = QGridLayout(self.General)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.groupBox = QGroupBox(self.General)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 120))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.gridLayout_8 = QGridLayout(self.groupBox)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(6, 6, 6, 6)
        self.EnableBackup = QCheckBox(self.groupBox)
        self.EnableBackup.setObjectName(u"EnableBackup")
        font1 = QFont()
        font1.setBold(False)
        font1.setWeight(50)
        self.EnableBackup.setFont(font1)

        self.gridLayout_8.addWidget(self.EnableBackup, 0, 0, 1, 1)

        self.groupBox_Backup = QGroupBox(self.groupBox)
        self.groupBox_Backup.setObjectName(u"groupBox_Backup")
        self.groupBox_Backup.setEnabled(False)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_Backup.sizePolicy().hasHeightForWidth())
        self.groupBox_Backup.setSizePolicy(sizePolicy)
        self.groupBox_Backup.setMinimumSize(QSize(0, 50))
        self.groupBox_Backup.setFont(font1)
        self.gridLayout_13 = QGridLayout(self.groupBox_Backup)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.label_4 = QLabel(self.groupBox_Backup)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFrameShape(QFrame.Box)
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_13.addWidget(self.label_4, 0, 0, 1, 1)

        self.BackUpLocation = QPushButton(self.groupBox_Backup)
        self.BackUpLocation.setObjectName(u"BackUpLocation")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(20)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.BackUpLocation.sizePolicy().hasHeightForWidth())
        self.BackUpLocation.setSizePolicy(sizePolicy1)
        self.BackUpLocation.setMinimumSize(QSize(20, 0))

        self.gridLayout_13.addWidget(self.BackUpLocation, 0, 1, 1, 1)


        self.gridLayout_8.addWidget(self.groupBox_Backup, 1, 0, 1, 1)


        self.gridLayout_9.addWidget(self.groupBox, 0, 0, 2, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_7, 3, 0, 1, 1)

        self.groupBox1 = QGroupBox(self.General)
        self.groupBox1.setObjectName(u"groupBox1")
        self.groupBox1.setMinimumSize(QSize(0, 200))
        self.groupBox1.setFont(font)
        self.groupBox_2 = QGroupBox(self.groupBox1)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(7, 130, 521, 60))
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy2)
        self.groupBox_2.setMinimumSize(QSize(0, 60))
        self.groupBox_2.setFont(font1)
        self.gridLayout_12 = QGridLayout(self.groupBox_2)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(-1, 9, -1, -1)
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFrameShape(QFrame.Box)
        self.label_7.setScaledContents(True)
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.label_7, 0, 0, 1, 1)

        self.StyleSheetLocation = QPushButton(self.groupBox_2)
        self.StyleSheetLocation.setObjectName(u"StyleSheetLocation")
        sizePolicy1.setHeightForWidth(self.StyleSheetLocation.sizePolicy().hasHeightForWidth())
        self.StyleSheetLocation.setSizePolicy(sizePolicy1)
        self.StyleSheetLocation.setMinimumSize(QSize(20, 0))

        self.gridLayout_12.addWidget(self.StyleSheetLocation, 0, 1, 1, 1)

        self.layoutWidget = QWidget(self.groupBox1)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 20, 181, 101))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.AutoHide = QCheckBox(self.layoutWidget)
        self.AutoHide.setObjectName(u"AutoHide")
        self.AutoHide.setFont(font1)

        self.verticalLayout_2.addWidget(self.AutoHide)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy3)
        self.label_10.setMinimumSize(QSize(120, 0))
        self.label_10.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label_10)

        self.IconSize_Small = QSpinBox(self.layoutWidget)
        self.IconSize_Small.setObjectName(u"IconSize_Small")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.IconSize_Small.sizePolicy().hasHeightForWidth())
        self.IconSize_Small.setSizePolicy(sizePolicy4)
        self.IconSize_Small.setMinimumSize(QSize(30, 0))
        self.IconSize_Small.setSizeIncrement(QSize(0, 0))
        self.IconSize_Small.setBaseSize(QSize(0, 0))
        self.IconSize_Small.setFont(font1)
        self.IconSize_Small.setFrame(True)
        self.IconSize_Small.setAlignment(Qt.AlignCenter)
        self.IconSize_Small.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.IconSize_Small.setProperty("showGroupSeparator", False)
        self.IconSize_Small.setMinimum(0)
        self.IconSize_Small.setValue(24)

        self.horizontalLayout_5.addWidget(self.IconSize_Small)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_11 = QLabel(self.layoutWidget)
        self.label_11.setObjectName(u"label_11")
        sizePolicy3.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy3)
        self.label_11.setMinimumSize(QSize(120, 0))
        self.label_11.setFont(font1)

        self.horizontalLayout_6.addWidget(self.label_11)

        self.IconSize_Medium = QSpinBox(self.layoutWidget)
        self.IconSize_Medium.setObjectName(u"IconSize_Medium")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(20)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.IconSize_Medium.sizePolicy().hasHeightForWidth())
        self.IconSize_Medium.setSizePolicy(sizePolicy5)
        self.IconSize_Medium.setMinimumSize(QSize(20, 0))
        self.IconSize_Medium.setFont(font1)
        self.IconSize_Medium.setAlignment(Qt.AlignCenter)
        self.IconSize_Medium.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.IconSize_Medium.setValue(44)

        self.horizontalLayout_6.addWidget(self.IconSize_Medium)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.ShowText = QCheckBox(self.layoutWidget)
        self.ShowText.setObjectName(u"ShowText")
        self.ShowText.setFont(font1)

        self.verticalLayout_2.addWidget(self.ShowText)


        self.gridLayout_9.addWidget(self.groupBox1, 2, 0, 1, 1)

        self.tabWidget.addTab(self.General, "")

        self.gridLayout_7.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.retranslateUi(Form)
        self.EnableBackup.toggled.connect(self.groupBox_Backup.setEnabled)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.GenerateJson.setText(QCoreApplication.translate("Form", u"Update", None))
        self.GenerateJsonExit.setText(QCoreApplication.translate("Form", u"Close", None))
#if QT_CONFIG(shortcut)
        self.GenerateJsonExit.setShortcut(QCoreApplication.translate("Form", u"Esc", None))
#endif // QT_CONFIG(shortcut)
        self.RestoreJson.setText(QCoreApplication.translate("Form", u"Restore", None))
        self.ResetJson.setText(QCoreApplication.translate("Form", u"Reset", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Backup settings", None))
        self.EnableBackup.setText(QCoreApplication.translate("Form", u"Create backup", None))
        self.groupBox_Backup.setTitle(QCoreApplication.translate("Form", u"Backup location", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"...\\", None))
        self.BackUpLocation.setText(QCoreApplication.translate("Form", u"Browse..", None))
        self.groupBox1.setTitle(QCoreApplication.translate("Form", u"Ribbon settings", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"Select stylesheet", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"...\\", None))
        self.StyleSheetLocation.setText(QCoreApplication.translate("Form", u"Browse..", None))
        self.AutoHide.setText(QCoreApplication.translate("Form", u"Autohide the ribbon", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Size of small icons:", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Size of medium icons:", None))
        self.ShowText.setText(QCoreApplication.translate("Form", u"Show icon text", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.General), QCoreApplication.translate("Form", u"General", None))
    # retranslateUi

