# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Settings.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide.QtWidgets import (
    QAbstractItemView,
    QAbstractScrollArea,
    QApplication,
    QComboBox,
    QFrame,
    QGridLayout,
    QHeaderView,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QTabWidget,
    QTableWidget,
    QTableWidgetItem,
    QToolButton,
    QWidget,
)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(593, 724)
        self.gridLayout_7 = QGridLayout(Form)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.GenerateJson = QPushButton(Form)
        self.GenerateJson.setObjectName("GenerateJson")

        self.gridLayout_6.addWidget(self.GenerateJson, 0, 3, 1, 1)

        self.ResetJson = QPushButton(Form)
        self.ResetJson.setObjectName("ResetJson")

        self.gridLayout_6.addWidget(self.ResetJson, 0, 0, 1, 1)

        self.RestoreJson = QPushButton(Form)
        self.RestoreJson.setObjectName("RestoreJson")

        self.gridLayout_6.addWidget(self.RestoreJson, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.gridLayout_7.addLayout(self.gridLayout_6, 1, 0, 1, 1)

        self.tabToolbar = QTabWidget(Form)
        self.tabToolbar.setObjectName("tabToolbar")
        self.QAToolbars = QWidget()
        self.QAToolbars.setObjectName("QAToolbars")
        self.layoutWidget = QWidget(self.QAToolbars)
        self.layoutWidget.setObjectName("layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 10, 551, 631))
        self.gridLayout_2 = QGridLayout(self.layoutWidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_2.setContentsMargins(6, 0, 0, 0)
        self.CommandsAvailable = QListWidget(self.layoutWidget)
        __qlistwidgetitem = QListWidgetItem(self.CommandsAvailable)
        __qlistwidgetitem.setCheckState(Qt.Checked)
        self.CommandsAvailable.setObjectName("CommandsAvailable")

        self.gridLayout_2.addWidget(self.CommandsAvailable, 0, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.toolButton_3 = QToolButton(self.layoutWidget)
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolButton_3.setArrowType(Qt.UpArrow)

        self.gridLayout.addWidget(self.toolButton_3, 4, 0, 1, 1)

        self.toolButton_4 = QToolButton(self.layoutWidget)
        self.toolButton_4.setObjectName("toolButton_4")
        self.toolButton_4.setArrowType(Qt.DownArrow)

        self.gridLayout.addWidget(self.toolButton_4, 5, 0, 1, 1)

        self.toolButton_2 = QToolButton(self.layoutWidget)
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_2.setArrowType(Qt.LeftArrow)

        self.gridLayout.addWidget(self.toolButton_2, 2, 0, 1, 1)

        self.toolButton = QToolButton(self.layoutWidget)
        self.toolButton.setObjectName("toolButton")
        self.toolButton.setArrowType(Qt.RightArrow)

        self.gridLayout.addWidget(self.toolButton, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 6, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_3, 3, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 0, 1, 1)

        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)

        self.CommandesSelected = QListWidget(self.layoutWidget)
        __qlistwidgetitem1 = QListWidgetItem(self.CommandesSelected)
        __qlistwidgetitem1.setCheckState(Qt.Checked)
        self.CommandesSelected.setObjectName("CommandesSelected")

        self.gridLayout_2.addWidget(self.CommandesSelected, 0, 2, 1, 1)

        self.tabToolbar.addTab(self.QAToolbars, "")
        self.Workbenches = QWidget()
        self.Workbenches.setObjectName("Workbenches")
        self.layoutWidget1 = QWidget(self.Workbenches)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 10, 551, 631))
        self.gridLayout_3 = QGridLayout(self.layoutWidget1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_3.setContentsMargins(6, 0, 0, 0)
        self.WorkbenchesAvailable = QListWidget(self.layoutWidget1)
        __qlistwidgetitem2 = QListWidgetItem(self.WorkbenchesAvailable)
        __qlistwidgetitem2.setCheckState(Qt.Checked)
        self.WorkbenchesAvailable.setObjectName("WorkbenchesAvailable")

        self.gridLayout_3.addWidget(self.WorkbenchesAvailable, 0, 0, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_4, 0, 0, 1, 1)

        self.toolButton_5 = QToolButton(self.layoutWidget1)
        self.toolButton_5.setObjectName("toolButton_5")
        self.toolButton_5.setArrowType(Qt.UpArrow)

        self.gridLayout_4.addWidget(self.toolButton_5, 4, 0, 1, 1)

        self.toolButton_6 = QToolButton(self.layoutWidget1)
        self.toolButton_6.setObjectName("toolButton_6")
        self.toolButton_6.setArrowType(Qt.DownArrow)

        self.gridLayout_4.addWidget(self.toolButton_6, 5, 0, 1, 1)

        self.toolButton_7 = QToolButton(self.layoutWidget1)
        self.toolButton_7.setObjectName("toolButton_7")
        self.toolButton_7.setArrowType(Qt.LeftArrow)

        self.gridLayout_4.addWidget(self.toolButton_7, 2, 0, 1, 1)

        self.toolButton_8 = QToolButton(self.layoutWidget1)
        self.toolButton_8.setObjectName("toolButton_8")
        self.toolButton_8.setArrowType(Qt.RightArrow)

        self.gridLayout_4.addWidget(self.toolButton_8, 1, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_5, 6, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_4.addItem(self.verticalSpacer_6, 3, 0, 1, 1)

        self.gridLayout_3.addLayout(self.gridLayout_4, 0, 1, 1, 1)

        self.WorkbenchesSelected = QListWidget(self.layoutWidget1)
        __qlistwidgetitem3 = QListWidgetItem(self.WorkbenchesSelected)
        __qlistwidgetitem3.setCheckState(Qt.Checked)
        self.WorkbenchesSelected.setObjectName("WorkbenchesSelected")

        self.gridLayout_3.addWidget(self.WorkbenchesSelected, 0, 2, 1, 1)

        self.tabToolbar.addTab(self.Workbenches, "")
        self.RibbonDesign = QWidget()
        self.RibbonDesign.setObjectName("RibbonDesign")
        self.tableWidget = QTableWidget(self.RibbonDesign)
        if self.tableWidget.columnCount() < 5:
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        if self.tableWidget.rowCount() < 1:
            self.tableWidget.setRowCount(1)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem6)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.NoBrush)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setCheckState(Qt.Checked)
        __qtablewidgetitem7.setTextAlignment(Qt.AlignCenter)
        __qtablewidgetitem7.setBackground(brush)
        __qtablewidgetitem7.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
        self.tableWidget.setItem(0, 1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setCheckState(Qt.Checked)
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter)
        __qtablewidgetitem8.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
        self.tableWidget.setItem(0, 2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setCheckState(Qt.Checked)
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter)
        __qtablewidgetitem9.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
        self.tableWidget.setItem(0, 3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setCheckState(Qt.Checked)
        __qtablewidgetitem10.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
        self.tableWidget.setItem(0, 4, __qtablewidgetitem10)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setGeometry(QRect(10, 70, 521, 561))
        self.tableWidget.setStyleSheet("border-color: rgb(167, 167rgb(217, 217, 217), 167);")
        self.tableWidget.setFrameShape(QFrame.StyledPanel)
        self.tableWidget.setFrameShadow(QFrame.Plain)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.layoutWidget2 = QWidget(self.RibbonDesign)
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 10, 391, 52))
        self.gridLayout_5 = QGridLayout(self.layoutWidget2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget2)
        self.label.setObjectName("label")

        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)

        self.WorkbenchList = QComboBox(self.layoutWidget2)
        self.WorkbenchList.setObjectName("WorkbenchList")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.WorkbenchList.sizePolicy().hasHeightForWidth())
        self.WorkbenchList.setSizePolicy(sizePolicy)

        self.gridLayout_5.addWidget(self.WorkbenchList, 0, 1, 1, 1)

        self.label_2 = QLabel(self.layoutWidget2)
        self.label_2.setObjectName("label_2")

        self.gridLayout_5.addWidget(self.label_2, 1, 0, 1, 1)

        self.ToolbarList = QComboBox(self.layoutWidget2)
        self.ToolbarList.setObjectName("ToolbarList")

        self.gridLayout_5.addWidget(self.ToolbarList, 1, 1, 1, 1)

        self.tabToolbar.addTab(self.RibbonDesign, "")

        self.gridLayout_7.addWidget(self.tabToolbar, 0, 0, 1, 1)

        self.retranslateUi(Form)

        self.tabToolbar.setCurrentIndex(2)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form", None))
        self.GenerateJson.setText(QCoreApplication.translate("Form", "Generate", None))
        self.ResetJson.setText(QCoreApplication.translate("Form", "Reset", None))
        self.RestoreJson.setText(QCoreApplication.translate("Form", "Restore", None))

        __sortingEnabled = self.CommandsAvailable.isSortingEnabled()
        self.CommandsAvailable.setSortingEnabled(False)
        ___qlistwidgetitem = self.CommandsAvailable.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Form", "New Item", None))
        self.CommandsAvailable.setSortingEnabled(__sortingEnabled)

        self.toolButton_3.setText(QCoreApplication.translate("Form", "...", None))
        self.toolButton_4.setText(QCoreApplication.translate("Form", "...", None))
        self.toolButton_2.setText(QCoreApplication.translate("Form", "...", None))
        self.toolButton.setText(QCoreApplication.translate("Form", "...", None))

        __sortingEnabled1 = self.CommandesSelected.isSortingEnabled()
        self.CommandesSelected.setSortingEnabled(False)
        ___qlistwidgetitem1 = self.CommandesSelected.item(0)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Form", "New Item", None))
        self.CommandesSelected.setSortingEnabled(__sortingEnabled1)

        self.tabToolbar.setTabText(
            self.tabToolbar.indexOf(self.QAToolbars), QCoreApplication.translate("Form", "Quick access toolbar", None)
        )

        __sortingEnabled2 = self.WorkbenchesAvailable.isSortingEnabled()
        self.WorkbenchesAvailable.setSortingEnabled(False)
        ___qlistwidgetitem2 = self.WorkbenchesAvailable.item(0)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Form", "New Item", None))
        self.WorkbenchesAvailable.setSortingEnabled(__sortingEnabled2)

        self.toolButton_5.setText(QCoreApplication.translate("Form", "...", None))
        self.toolButton_6.setText(QCoreApplication.translate("Form", "...", None))
        self.toolButton_7.setText(QCoreApplication.translate("Form", "...", None))
        self.toolButton_8.setText(QCoreApplication.translate("Form", "...", None))

        __sortingEnabled3 = self.WorkbenchesSelected.isSortingEnabled()
        self.WorkbenchesSelected.setSortingEnabled(False)
        ___qlistwidgetitem3 = self.WorkbenchesSelected.item(0)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("Form", "New Item", None))
        self.WorkbenchesSelected.setSortingEnabled(__sortingEnabled3)

        self.tabToolbar.setTabText(
            self.tabToolbar.indexOf(self.Workbenches), QCoreApplication.translate("Form", "Workbenches", None)
        )
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", "Command", None))
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", "Small", None))
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", "Medium", None))
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", "Large", None))
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", "Icon only", None))
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", "1", None))

        __sortingEnabled4 = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem6 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", "Command 1", None))
        self.tableWidget.setSortingEnabled(__sortingEnabled4)

        self.label.setText(QCoreApplication.translate("Form", "Select workbench:", None))
        self.label_2.setText(QCoreApplication.translate("Form", "Select toolbar:", None))
        self.tabToolbar.setTabText(
            self.tabToolbar.indexOf(self.RibbonDesign), QCoreApplication.translate("Form", "Ribbon design", None)
        )

    # retranslateUi
