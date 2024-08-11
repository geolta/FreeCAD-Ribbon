# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Settings.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QListView,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QTableWidget, QTableWidgetItem,
    QToolButton, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowModality(Qt.WindowModal)
        Form.resize(579, 724)
        self.gridLayout_7 = QGridLayout(Form)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.GenerateJson = QPushButton(Form)
        self.GenerateJson.setObjectName(u"GenerateJson")

        self.gridLayout_6.addWidget(self.GenerateJson, 0, 3, 1, 1)

        self.ResetJson = QPushButton(Form)
        self.ResetJson.setObjectName(u"ResetJson")

        self.gridLayout_6.addWidget(self.ResetJson, 0, 0, 1, 1)

        self.RestoreJson = QPushButton(Form)
        self.RestoreJson.setObjectName(u"RestoreJson")

        self.gridLayout_6.addWidget(self.RestoreJson, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer, 0, 1, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_6, 1, 0, 1, 1)

        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.QAToolbars = QWidget()
        self.QAToolbars.setObjectName(u"QAToolbars")
        self.layoutWidget = QWidget(self.QAToolbars)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 10, 551, 631))
        self.gridLayout_2 = QGridLayout(self.layoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(6, 0, 0, 0)
        self.CommandesSelected = QListWidget(self.layoutWidget)
        __qlistwidgetitem = QListWidgetItem(self.CommandesSelected)
        __qlistwidgetitem.setCheckState(Qt.Checked);
        self.CommandesSelected.setObjectName(u"CommandesSelected")
        self.CommandesSelected.setDefaultDropAction(Qt.MoveAction)
        self.CommandesSelected.setMovement(QListView.Free)

        self.gridLayout_2.addWidget(self.CommandesSelected, 1, 2, 1, 1)

        self.CommandsAvailable = QListWidget(self.layoutWidget)
        __qlistwidgetitem1 = QListWidgetItem(self.CommandsAvailable)
        __qlistwidgetitem1.setCheckState(Qt.Checked);
        self.CommandsAvailable.setObjectName(u"CommandsAvailable")
        self.CommandsAvailable.setSelectionMode(QAbstractItemView.MultiSelection)

        self.gridLayout_2.addWidget(self.CommandsAvailable, 1, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.MoveUp_Command = QToolButton(self.layoutWidget)
        self.MoveUp_Command.setObjectName(u"MoveUp_Command")
        self.MoveUp_Command.setArrowType(Qt.UpArrow)

        self.gridLayout.addWidget(self.MoveUp_Command, 4, 0, 1, 1)

        self.MoveDown_Command = QToolButton(self.layoutWidget)
        self.MoveDown_Command.setObjectName(u"MoveDown_Command")
        self.MoveDown_Command.setArrowType(Qt.DownArrow)

        self.gridLayout.addWidget(self.MoveDown_Command, 5, 0, 1, 1)

        self.Remove_Command = QToolButton(self.layoutWidget)
        self.Remove_Command.setObjectName(u"Remove_Command")
        self.Remove_Command.setArrowType(Qt.LeftArrow)

        self.gridLayout.addWidget(self.Remove_Command, 2, 0, 1, 1)

        self.Add_Command = QToolButton(self.layoutWidget)
        self.Add_Command.setObjectName(u"Add_Command")
        self.Add_Command.setArrowType(Qt.RightArrow)

        self.gridLayout.addWidget(self.Add_Command, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 6, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_3, 3, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 1, 1)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 3)

        self.tabWidget.addTab(self.QAToolbars, "")
        self.Workbenches = QWidget()
        self.Workbenches.setObjectName(u"Workbenches")
        self.layoutWidget1 = QWidget(self.Workbenches)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 10, 551, 631))
        self.gridLayout_3 = QGridLayout(self.layoutWidget1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(6, 0, 0, 0)
        self.WorkbenchesAvailable = QListWidget(self.layoutWidget1)
        __qlistwidgetitem2 = QListWidgetItem(self.WorkbenchesAvailable)
        __qlistwidgetitem2.setCheckState(Qt.Checked);
        self.WorkbenchesAvailable.setObjectName(u"WorkbenchesAvailable")
        self.WorkbenchesAvailable.setSelectionMode(QAbstractItemView.MultiSelection)

        self.gridLayout_3.addWidget(self.WorkbenchesAvailable, 1, 0, 1, 1)

        self.WorkbenchesSelected = QListWidget(self.layoutWidget1)
        __qlistwidgetitem3 = QListWidgetItem(self.WorkbenchesSelected)
        __qlistwidgetitem3.setCheckState(Qt.Checked);
        self.WorkbenchesSelected.setObjectName(u"WorkbenchesSelected")
        self.WorkbenchesSelected.setDefaultDropAction(Qt.MoveAction)
        self.WorkbenchesSelected.setMovement(QListView.Free)

        self.gridLayout_3.addWidget(self.WorkbenchesSelected, 1, 2, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_4, 0, 0, 1, 1)

        self.MoveUp_Workbench = QToolButton(self.layoutWidget1)
        self.MoveUp_Workbench.setObjectName(u"MoveUp_Workbench")
        self.MoveUp_Workbench.setArrowType(Qt.UpArrow)

        self.gridLayout_4.addWidget(self.MoveUp_Workbench, 4, 0, 1, 1)

        self.MoveDown_Workbench = QToolButton(self.layoutWidget1)
        self.MoveDown_Workbench.setObjectName(u"MoveDown_Workbench")
        self.MoveDown_Workbench.setArrowType(Qt.DownArrow)

        self.gridLayout_4.addWidget(self.MoveDown_Workbench, 5, 0, 1, 1)

        self.Remove_Workbench = QToolButton(self.layoutWidget1)
        self.Remove_Workbench.setObjectName(u"Remove_Workbench")
        self.Remove_Workbench.setArrowType(Qt.LeftArrow)

        self.gridLayout_4.addWidget(self.Remove_Workbench, 2, 0, 1, 1)

        self.Add_Workbench = QToolButton(self.layoutWidget1)
        self.Add_Workbench.setObjectName(u"Add_Workbench")
        self.Add_Workbench.setArrowType(Qt.RightArrow)

        self.gridLayout_4.addWidget(self.Add_Workbench, 1, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_5, 6, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_4.addItem(self.verticalSpacer_6, 3, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_4, 1, 1, 1, 1)

        self.label_6 = QLabel(self.layoutWidget1)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 3)

        self.tabWidget.addTab(self.Workbenches, "")
        self.Toolbars = QWidget()
        self.Toolbars.setObjectName(u"Toolbars")
        self.layoutWidget_6 = QWidget(self.Toolbars)
        self.layoutWidget_6.setObjectName(u"layoutWidget_6")
        self.layoutWidget_6.setGeometry(QRect(0, 10, 551, 631))
        self.gridLayout_17 = QGridLayout(self.layoutWidget_6)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(6, 0, 0, 0)
        self.ToolbarsToExclude = QListWidget(self.layoutWidget_6)
        __qlistwidgetitem4 = QListWidgetItem(self.ToolbarsToExclude)
        __qlistwidgetitem4.setCheckState(Qt.Checked);
        self.ToolbarsToExclude.setObjectName(u"ToolbarsToExclude")
        self.ToolbarsToExclude.setSelectionMode(QAbstractItemView.MultiSelection)

        self.gridLayout_17.addWidget(self.ToolbarsToExclude, 1, 0, 1, 1)

        self.ToolbarsExcluded = QListWidget(self.layoutWidget_6)
        __qlistwidgetitem5 = QListWidgetItem(self.ToolbarsExcluded)
        __qlistwidgetitem5.setCheckState(Qt.Checked);
        self.ToolbarsExcluded.setObjectName(u"ToolbarsExcluded")
        self.ToolbarsExcluded.setDefaultDropAction(Qt.MoveAction)
        self.ToolbarsExcluded.setMovement(QListView.Free)

        self.gridLayout_17.addWidget(self.ToolbarsExcluded, 1, 2, 1, 1)

        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_18.addItem(self.verticalSpacer_15, 0, 0, 1, 1)

        self.MoveUp_Toolbar = QToolButton(self.layoutWidget_6)
        self.MoveUp_Toolbar.setObjectName(u"MoveUp_Toolbar")
        self.MoveUp_Toolbar.setArrowType(Qt.UpArrow)

        self.gridLayout_18.addWidget(self.MoveUp_Toolbar, 4, 0, 1, 1)

        self.MoveDown_Toolbar = QToolButton(self.layoutWidget_6)
        self.MoveDown_Toolbar.setObjectName(u"MoveDown_Toolbar")
        self.MoveDown_Toolbar.setArrowType(Qt.DownArrow)

        self.gridLayout_18.addWidget(self.MoveDown_Toolbar, 5, 0, 1, 1)

        self.Remove_Toolbar = QToolButton(self.layoutWidget_6)
        self.Remove_Toolbar.setObjectName(u"Remove_Toolbar")
        self.Remove_Toolbar.setArrowType(Qt.LeftArrow)

        self.gridLayout_18.addWidget(self.Remove_Toolbar, 2, 0, 1, 1)

        self.Add_Toolbar = QToolButton(self.layoutWidget_6)
        self.Add_Toolbar.setObjectName(u"Add_Toolbar")
        self.Add_Toolbar.setArrowType(Qt.RightArrow)

        self.gridLayout_18.addWidget(self.Add_Toolbar, 1, 0, 1, 1)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_18.addItem(self.verticalSpacer_16, 6, 0, 1, 1)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_18.addItem(self.verticalSpacer_17, 3, 0, 1, 1)


        self.gridLayout_17.addLayout(self.gridLayout_18, 1, 1, 1, 1)

        self.label_13 = QLabel(self.layoutWidget_6)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_17.addWidget(self.label_13, 0, 0, 1, 3)

        self.tabWidget.addTab(self.Toolbars, "")
        self.RibbonDesign = QWidget()
        self.RibbonDesign.setObjectName(u"RibbonDesign")
        self.layoutWidget2 = QWidget(self.RibbonDesign)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 10, 391, 52))
        self.gridLayout_5 = QGridLayout(self.layoutWidget2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_5.addWidget(self.label_2, 1, 0, 1, 1)

        self.WorkbenchList = QComboBox(self.layoutWidget2)
        self.WorkbenchList.setObjectName(u"WorkbenchList")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.WorkbenchList.sizePolicy().hasHeightForWidth())
        self.WorkbenchList.setSizePolicy(sizePolicy)

        self.gridLayout_5.addWidget(self.WorkbenchList, 0, 1, 1, 1)

        self.ToolbarList = QComboBox(self.layoutWidget2)
        self.ToolbarList.setObjectName(u"ToolbarList")

        self.gridLayout_5.addWidget(self.ToolbarList, 1, 1, 1, 1)

        self.label = QLabel(self.layoutWidget2)
        self.label.setObjectName(u"label")

        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)

        self.IconOnly = QCheckBox(self.layoutWidget2)
        self.IconOnly.setObjectName(u"IconOnly")

        self.gridLayout_5.addWidget(self.IconOnly, 1, 2, 1, 1)

        self.widget = QWidget(self.RibbonDesign)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 70, 541, 571))
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_9)

        self.MoveUp_Toolbar_2 = QToolButton(self.widget)
        self.MoveUp_Toolbar_2.setObjectName(u"MoveUp_Toolbar_2")
        self.MoveUp_Toolbar_2.setArrowType(Qt.UpArrow)

        self.verticalLayout.addWidget(self.MoveUp_Toolbar_2)

        self.MoveDown_Toolbar_2 = QToolButton(self.widget)
        self.MoveDown_Toolbar_2.setObjectName(u"MoveDown_Toolbar_2")
        self.MoveDown_Toolbar_2.setArrowType(Qt.DownArrow)

        self.verticalLayout.addWidget(self.MoveDown_Toolbar_2)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_8)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.tableWidget = QTableWidget(self.widget)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 1):
            self.tableWidget.setRowCount(1)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(0, 0, __qtablewidgetitem5)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.NoBrush)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setCheckState(Qt.Checked);
        __qtablewidgetitem6.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem6.setBackground(brush);
        __qtablewidgetitem6.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(0, 1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setCheckState(Qt.Checked);
        __qtablewidgetitem7.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem7.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(0, 2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setCheckState(Qt.Checked);
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem8.setFlags(Qt.ItemIsSelectable|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget.setItem(0, 3, __qtablewidgetitem8)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"border-color: rgb(167, 167rgb(217, 217, 217), 167);")
        self.tableWidget.setFrameShape(QFrame.StyledPanel)
        self.tableWidget.setFrameShadow(QFrame.Plain)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.tableWidget.setIconSize(QSize(16, 16))
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.verticalHeader().setVisible(False)

        self.horizontalLayout_3.addWidget(self.tableWidget)

        self.tabWidget.addTab(self.RibbonDesign, "")
        self.Settings = QWidget()
        self.Settings.setObjectName(u"Settings")
        self.gridLayout_9 = QGridLayout(self.Settings)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.EnableBackup = QCheckBox(self.Settings)
        self.EnableBackup.setObjectName(u"EnableBackup")

        self.gridLayout_8.addWidget(self.EnableBackup, 0, 0, 1, 1)

        self.groupBox = QGroupBox(self.Settings)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setEnabled(False)
        self.groupBox.setMinimumSize(QSize(0, 50))
        self.layoutWidget3 = QWidget(self.groupBox)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(0, 20, 531, 25))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(6, 0, 6, 0)
        self.label_4 = QLabel(self.layoutWidget3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFrameShape(QFrame.Box)

        self.horizontalLayout.addWidget(self.label_4)

        self.BackUpLocation = QPushButton(self.layoutWidget3)
        self.BackUpLocation.setObjectName(u"BackUpLocation")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(20)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.BackUpLocation.sizePolicy().hasHeightForWidth())
        self.BackUpLocation.setSizePolicy(sizePolicy1)
        self.BackUpLocation.setMinimumSize(QSize(20, 0))

        self.horizontalLayout.addWidget(self.BackUpLocation)


        self.gridLayout_8.addWidget(self.groupBox, 1, 0, 1, 1)


        self.gridLayout_9.addLayout(self.gridLayout_8, 0, 0, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_7, 4, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.Settings)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(0, 50))
        self.layoutWidget_2 = QWidget(self.groupBox_2)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(0, 20, 531, 25))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(6, 0, 6, 0)
        self.label_7 = QLabel(self.layoutWidget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFrameShape(QFrame.Box)

        self.horizontalLayout_2.addWidget(self.label_7)

        self.StyleSheetLocation = QPushButton(self.layoutWidget_2)
        self.StyleSheetLocation.setObjectName(u"StyleSheetLocation")
        sizePolicy1.setHeightForWidth(self.StyleSheetLocation.sizePolicy().hasHeightForWidth())
        self.StyleSheetLocation.setSizePolicy(sizePolicy1)
        self.StyleSheetLocation.setMinimumSize(QSize(20, 0))

        self.horizontalLayout_2.addWidget(self.StyleSheetLocation)


        self.gridLayout_9.addWidget(self.groupBox_2, 2, 0, 1, 1)

        self.AutoHide = QCheckBox(self.Settings)
        self.AutoHide.setObjectName(u"AutoHide")

        self.gridLayout_9.addWidget(self.AutoHide, 3, 0, 1, 1)

        self.tabWidget.addTab(self.Settings, "")

        self.gridLayout_7.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.GenerateJson.setText(QCoreApplication.translate("Form", u"Generate", None))
        self.ResetJson.setText(QCoreApplication.translate("Form", u"Reset", None))
        self.RestoreJson.setText(QCoreApplication.translate("Form", u"Restore", None))

        __sortingEnabled = self.CommandesSelected.isSortingEnabled()
        self.CommandesSelected.setSortingEnabled(False)
        ___qlistwidgetitem = self.CommandesSelected.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Form", u"New Item", None));
        self.CommandesSelected.setSortingEnabled(__sortingEnabled)


        __sortingEnabled1 = self.CommandsAvailable.isSortingEnabled()
        self.CommandsAvailable.setSortingEnabled(False)
        ___qlistwidgetitem1 = self.CommandsAvailable.item(0)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Form", u"New Item", None));
        self.CommandsAvailable.setSortingEnabled(__sortingEnabled1)

        self.MoveUp_Command.setText(QCoreApplication.translate("Form", u"...", None))
        self.MoveDown_Command.setText(QCoreApplication.translate("Form", u"...", None))
        self.Remove_Command.setText(QCoreApplication.translate("Form", u"...", None))
        self.Add_Command.setText(QCoreApplication.translate("Form", u"...", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Select commands to add to the quick access toolbar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.QAToolbars), QCoreApplication.translate("Form", u"Quick access toolbar", None))

        __sortingEnabled2 = self.WorkbenchesAvailable.isSortingEnabled()
        self.WorkbenchesAvailable.setSortingEnabled(False)
        ___qlistwidgetitem2 = self.WorkbenchesAvailable.item(0)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Form", u"New Item", None));
        self.WorkbenchesAvailable.setSortingEnabled(__sortingEnabled2)


        __sortingEnabled3 = self.WorkbenchesSelected.isSortingEnabled()
        self.WorkbenchesSelected.setSortingEnabled(False)
        ___qlistwidgetitem3 = self.WorkbenchesSelected.item(0)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("Form", u"New Item", None));
        self.WorkbenchesSelected.setSortingEnabled(__sortingEnabled3)

        self.MoveUp_Workbench.setText(QCoreApplication.translate("Form", u"...", None))
        self.MoveDown_Workbench.setText(QCoreApplication.translate("Form", u"...", None))
        self.Remove_Workbench.setText(QCoreApplication.translate("Form", u"...", None))
        self.Add_Workbench.setText(QCoreApplication.translate("Form", u"...", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Select workbenches to<span style=\" font-weight:600;\"> include</span> in the ribbon.</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Workbenches), QCoreApplication.translate("Form", u"Workbenches", None))

        __sortingEnabled4 = self.ToolbarsToExclude.isSortingEnabled()
        self.ToolbarsToExclude.setSortingEnabled(False)
        ___qlistwidgetitem4 = self.ToolbarsToExclude.item(0)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("Form", u"New Item", None));
        self.ToolbarsToExclude.setSortingEnabled(__sortingEnabled4)


        __sortingEnabled5 = self.ToolbarsExcluded.isSortingEnabled()
        self.ToolbarsExcluded.setSortingEnabled(False)
        ___qlistwidgetitem5 = self.ToolbarsExcluded.item(0)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("Form", u"New Item", None));
        self.ToolbarsExcluded.setSortingEnabled(__sortingEnabled5)

        self.MoveUp_Toolbar.setText(QCoreApplication.translate("Form", u"...", None))
        self.MoveDown_Toolbar.setText(QCoreApplication.translate("Form", u"...", None))
        self.Remove_Toolbar.setText(QCoreApplication.translate("Form", u"...", None))
        self.Add_Toolbar.setText(QCoreApplication.translate("Form", u"...", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Select toolbars to <span style=\" font-weight:600;\">exclude</span> from the ribbon.</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Toolbars), QCoreApplication.translate("Form", u"Toolbars", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Select toolbar:", None))
        self.label.setText(QCoreApplication.translate("Form", u"Select workbench:", None))
        self.IconOnly.setText(QCoreApplication.translate("Form", u"Icon only", None))
        self.MoveUp_Toolbar_2.setText(QCoreApplication.translate("Form", u"...", None))
        self.MoveDown_Toolbar_2.setText(QCoreApplication.translate("Form", u"...", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Command", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Small", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Medium", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Large", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"1", None));

        __sortingEnabled6 = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem5 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Command 1", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled6)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.RibbonDesign), QCoreApplication.translate("Form", u"Ribbon design", None))
        self.EnableBackup.setText(QCoreApplication.translate("Form", u"Create backup", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Backup location", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"...\\", None))
        self.BackUpLocation.setText(QCoreApplication.translate("Form", u"Browse..", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"Select stylesheet", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"...\\", None))
        self.StyleSheetLocation.setText(QCoreApplication.translate("Form", u"Browse..", None))
        self.AutoHide.setText(QCoreApplication.translate("Form", u"Autohide the ribbon", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Settings), QCoreApplication.translate("Form", u"Settings", None))
    # retranslateUi

