# *************************************************************************************
# *   MIT License                                                                     *
# *                                                                                   *
# *   Copyright (c) 2024 Paul Ebbers                                                  *
# *                                                                                   *
# *   Permission is hereby granted, free of charge, to any person obtaining a copy    *
# *   of this software and associated documentation files (the "Software"), to deal   *
# *   in the Software without restriction, including without limitation the rights    *
# *   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell       *
# *   copies of the Software, and to permit persons to whom the Software is           *
# *   furnished to do so, subject to the following conditions:                        *
# *                                                                                   *
# *   The above copyright notice and this permission notice shall be included in all  *
# *   copies or substantial portions of the Software.                                 *
# *                                                                                   *
# *   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR      *
# *   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,        *
# *   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE     *
# *   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER          *
# *   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,   *
# *   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE   *
# *   SOFTWARE.                                                                       *
# *                                                                                   *
# *************************************************************************************/
import FreeCAD as App
import FreeCADGui as Gui
import os
from PySide.QtGui import QIcon, QAction, QPalette, QColor
from PySide.QtWidgets import (
    QListWidgetItem,
    QTableWidgetItem,
    QListWidget,
    QTableWidget,
    QSpinBox,
)
from PySide.QtCore import Qt, SIGNAL, QTimer
import sys
import json
from datetime import datetime
import shutil
import Standard_Functions_RIbbon as StandardFunctions
import Parameters_Ribbon

# Get the resources
pathIcons = Parameters_Ribbon.ICON_LOCATION
pathStylSheets = Parameters_Ribbon.STYLESHEET_LOCATION
pathUI = Parameters_Ribbon.UI_LOCATION
pathBackup = Parameters_Ribbon.BACKUP_LOCATION
sys.path.append(pathIcons)
sys.path.append(pathStylSheets)
sys.path.append(pathUI)
sys.path.append(pathBackup)

# import graphical created Ui. (With QtDesigner or QtCreator)
import Settings_ui as Settings_ui

# Define the translation
translate = App.Qt.translate


class LoadDialog(Settings_ui.Ui_Form):
    ShowText_Small = False
    ShowText_Medium = False
    ShowText_Large = False

    def __init__(self):
        # Makes "self.on_CreateBOM_clicked" listen to the changed control values instead initial values
        super(LoadDialog, self).__init__()

        # # this will create a Qt widget from our ui file
        self.form = Gui.PySideUic.loadUi(os.path.join(pathUI, "Settings.ui"))

        # Make sure that the dialog stays on top
        self.form.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

        # Get the style from the main window and use it for this form
        mw = Gui.getMainWindow()
        palette = mw.palette()
        self.form.setPalette(palette)
        Style = mw.style()
        self.form.setStyle(Style)

        # load all settings
        self.form.EnableBackup.setChecked(Parameters_Ribbon.ENABLE_BACKUP)
        self.form.label_4.setText(Parameters_Ribbon.BACKUP_LOCATION)
        self.form.IconSize_Small.setValue(Parameters_Ribbon.ICON_SIZE_SMALL)
        self.form.IconSize_Medium.setValue(Parameters_Ribbon.ICON_SIZE_MEDIUM)
        # self.form.IconSize_Large.setValue(Parameters_Ribbon.ICON_SIZE_LARGE)
        self.form.label_7.setText(Parameters_Ribbon.STYLESHEET)
        if Parameters_Ribbon.SHOW_ICON_TEXT_SMALL is True:
            self.form.ShowText_Small.setCheckState(Qt.CheckState.Checked)
        else:
            self.form.ShowText_Small.setCheckState(Qt.CheckState.Unchecked)
        if Parameters_Ribbon.SHOW_ICON_TEXT_MEDIUM is True:
            self.form.ShowText_Medium.setCheckState(Qt.CheckState.Checked)
        else:
            self.form.ShowText_Medium.setCheckState(Qt.CheckState.Unchecked)
        if Parameters_Ribbon.SHOW_ICON_TEXT_LARGE is True:
            self.form.ShowText_Large.setCheckState(Qt.CheckState.Checked)
        else:
            self.form.ShowText_Large.setCheckState(Qt.CheckState.Unchecked)

        # region - connect controls with functions----------------------------------------------------
        #
        self.form.EnableBackup.clicked.connect(self.on_EnableBackup_clicked)
        self.form.BackUpLocation.clicked.connect(self.on_BackUpLocation_clicked)
        self.form.IconSize_Small.textChanged.connect(self.on_IconSize_Small_TextChanged)
        self.form.IconSize_Medium.textChanged.connect(
            self.on_IconSize_Medium_TextChanged
        )
        self.form.StyleSheetLocation.clicked.connect(self.on_StyleSheetLocation_clicked)

        self.form.ShowText_Small.clicked.connect(self.on_ShowTextSmall_clicked)
        self.form.ShowText_Medium.clicked.connect(self.on_ShowTextMedium_clicked)
        self.form.ShowText_Large.clicked.connect(self.on_ShowTextLarge_clicked)

        # Connect the cancel button
        def Cancel():
            self.on_Cancel_clicked(self)

        self.form.Cancel.connect(self.form.Cancel, SIGNAL("clicked()"), Cancel)

        # Connect the button GenerateJsonExit with the function on_GenerateJsonExit_clicked
        def GenerateJsonExit():
            self.on_GenerateJsonExit_clicked(self)

        self.form.GenerateJsonExit.connect(
            self.form.GenerateJsonExit, SIGNAL("clicked()"), GenerateJsonExit
        )
        # endregion

        return

    # region - Control functions----------------------------------------------------------------------

    def on_EnableBackup_clicked(self):
        if self.form.EnableBackup.isChecked() is True:
            Parameters_Ribbon.ENABLE_BACKUP = True
            Parameters_Ribbon.Settings.SetBoolSetting("BackupEnabled", True)
        if self.form.EnableBackup.isChecked() is False:
            Parameters_Ribbon.ENABLE_BACKUP = False
            Parameters_Ribbon.Settings.SetBoolSetting("BackupEnabled", False)

        return

    def on_BackUpLocation_clicked(self):
        BackupFolder = ""
        BackupFolder = StandardFunctions.GetFolder(
            parent=None, DefaultPath=Parameters_Ribbon.BACKUP_LOCATION
        )
        if BackupFolder != "":
            self.pathBackup = BackupFolder
            self.form.label_4.setText(BackupFolder)
            Parameters_Ribbon.BACKUP_LOCATION = BackupFolder
            Parameters_Ribbon.Settings.SetStringSetting("BackupFolder", BackupFolder)

        return

    def on_IconSize_Small_TextChanged(self):
        Parameters_Ribbon.ICON_SIZE_SMALL = int(self.form.IconSize_Small.text())
        Parameters_Ribbon.Settings.SetIntSetting(
            "IconSize_Small", int(self.form.IconSize_Small.text())
        )

        return

    def on_IconSize_Medium_TextChanged(self):
        Parameters_Ribbon.ICON_SIZE_MEDIUM = int(self.form.IconSize_Medium.text())
        Parameters_Ribbon.Settings.SetIntSetting(
            "IconSize_Medium", int(self.form.IconSize_Medium.text())
        )

        return

    def on_StyleSheetLocation_clicked(self):
        StyleSheet = ""
        StyleSheet = StandardFunctions.GetFileDialog(
            Filter="Stylesheet (*.qss)",
            parent=None,
            DefaultPath=os.path.dirname(Parameters_Ribbon.STYLESHEET),
            SaveAs=False,
        )
        if StyleSheet != "":
            self.form.label_7.setText(StyleSheet)
            Parameters_Ribbon.STYLESHEET = StyleSheet
            Parameters_Ribbon.Settings.SetStringSetting("Stylesheet", StyleSheet)

        return

    def on_ShowTextSmall_clicked(self):
        if self.form.ShowText_Small.isChecked() is True:
            Parameters_Ribbon.SHOW_ICON_TEXT_SMALL = True
            Parameters_Ribbon.Settings.SetBoolSetting("ShowIconText_Small", True)
            self.ShowText_Small = True
        if self.form.ShowText_Small.isChecked() is False:
            Parameters_Ribbon.SHOW_ICON_TEXT_SMALL = False
            Parameters_Ribbon.Settings.SetBoolSetting("ShowIconText_Small", False)
            self.ShowText_Small = False

    def on_ShowTextMedium_clicked(self):
        if self.form.ShowText_Medium.isChecked() is True:
            Parameters_Ribbon.SHOW_ICON_TEXT_MEDIUM = True
            Parameters_Ribbon.Settings.SetBoolSetting("ShowIconText_Medium", True)
            self.ShowText_Medium = True
        if self.form.ShowText_Medium.isChecked() is False:
            Parameters_Ribbon.SHOW_ICON_TEXT_MEDIUM = False
            Parameters_Ribbon.Settings.SetBoolSetting("ShowIconText_Medium", False)
            self.ShowText_Medium = False

    def on_ShowTextLarge_clicked(self):
        if self.form.ShowText_Large.isChecked() is True:
            Parameters_Ribbon.SHOW_ICON_TEXT_LARGE = True
            Parameters_Ribbon.Settings.SetBoolSetting("ShowIconText_Large", True)
            self.ShowText_Large = True
        if self.form.ShowText_Large.isChecked() is False:
            Parameters_Ribbon.SHOW_ICON_TEXT_LARGE = False
            Parameters_Ribbon.Settings.SetBoolSetting("ShowIconText_Large", False)
            self.ShowText_Large = False

        return

    @staticmethod
    def on_Cancel_clicked(self):
        # Close the form
        self.form.close()
        return

    @staticmethod
    def on_GenerateJsonExit_clicked(self):
        # Close the form
        self.form.close()
        return

    # endregion---------------------------------------------------------------------------------------


def main():
    # Get the form
    Dialog = LoadDialog().form
    # Show the form
    Dialog.show()

    return
