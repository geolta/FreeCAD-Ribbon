# ***********************************************************************
# *                                                                     *
# * Copyright (c) 2019 Hakan Seven <hakanseven12@gmail.com>             *
# *                                                                     *
# * This program is free software; you can redistribute it and/or modify*
# * it under the terms of the GNU Lesser General Public License (LGPL)  *
# * as published by the Free Software Foundation; either version 3 of   *
# * the License, or (at your option) any later version.                 *
# * for detail see the LICENCE text file.                               *
# *                                                                     *
# * This program is distributed in the hope that it will be useful,     *
# * but WITHOUT ANY WARRANTY; without even the implied warranty of      *
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the       *
# * GNU Library General Public License for more details.                *
# *                                                                     *
# * You should have received a copy of the GNU Library General Public   *
# * License along with this program; if not, write to the Free Software *
# * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307*
# * USA                                                                 *
# *                                                                     *
# ***********************************************************************
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

    # Define list of the workbenches, toolbars and commands on class level
    List_Workbenches = []
    StringList_Toolbars = []
    List_Commands = []

    # Create lists for the several list in the json file.
    List_IgnoredToolbars = []
    List_IconOnlyToolbars = []
    List_QuickAccessCommands = []
    List_IgnoredWorkbenches = []
    Dict_RibbonCommandPanel = {}
    List_SortedCommands = []
    List_SortedToolbars = []
    Dict_CustomToolbars = {}

    ShowText = False

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

        # Read the jason file and fill the lists
        self.ReadJson()

        # load all settings
        self.form.EnableBackup.setChecked(Parameters_Ribbon.ENABLE_BACKUP)
        self.form.label_4.setText(Parameters_Ribbon.BACKUP_LOCATION)
        if Parameters_Ribbon.AUTOHIDE_RIBBON is True:
            self.form.AutoHide.setCheckState(Qt.CheckState.Checked)
        else:
            self.form.AutoHide.setCheckState(Qt.CheckState.Unchecked)
        self.form.IconSize_Small.setValue(Parameters_Ribbon.ICON_SIZE_SMALL)
        self.form.IconSize_Medium.setValue(Parameters_Ribbon.ICON_SIZE_MEDIUM)
        # self.form.IconSize_Large.setValue(Parameters_Ribbon.ICON_SIZE_LARGE)
        self.form.label_7.setText(Parameters_Ribbon.STYLESHEET)
        if Parameters_Ribbon.SHOW_ICON_TEXT is True:
            self.form.ShowText.setCheckState(Qt.CheckState.Checked)
        else:
            self.form.ShowText.setCheckState(Qt.CheckState.Unchecked)

        # region - connect controls with functions----------------------------------------------------
        #
        # Connect the button GenerateJson with the function on_GenerateJson_clicked
        def GenerateJson():
            self.on_GenerateJson_clicked(self)

        self.form.GenerateJson.connect(self.form.GenerateJson, SIGNAL("clicked()"), GenerateJson)

        # Connect the button GenerateJsonExit with the function on_GenerateJsonExit_clicked
        def GenerateJsonExit():
            self.on_GenerateJsonExit_clicked(self)

        self.form.GenerateJsonExit.connect(self.form.GenerateJsonExit, SIGNAL("clicked()"), GenerateJsonExit)

        self.form.RestoreJson.connect(self.form.RestoreJson, SIGNAL("clicked()"), self.on_RestoreJson_clicked)
        self.form.ResetJson.connect(self.form.ResetJson, SIGNAL("clicked()"), self.on_ResetJson_clicked)
        self.form.EnableBackup.clicked.connect(self.on_EnableBackup_clicked)
        self.form.BackUpLocation.clicked.connect(self.on_BackUpLocation_clicked)
        self.form.AutoHide.clicked.connect(self.on_AutoHide_clicked)
        self.form.IconSize_Small.textChanged.connect(self.on_IconSize_Small_TextChanged)
        self.form.IconSize_Medium.textChanged.connect(self.on_IconSize_Medium_TextChanged)
        # self.form.IconSize_Large.textChanged.connect(self.on_IconSize_Large_TextChanged)
        self.form.StyleSheetLocation.clicked.connect(self.on_StyleSheetLocation_clicked)
        self.form.ShowText.clicked.connect(self.on_ShowText_clicked)

        # endregion

        return

    # region - Control functions----------------------------------------------------------------------

    def on_RestoreJson_clicked(self):
        self.form.setWindowFlags(Qt.WindowType.WindowStaysOnBottomHint)
        # get the path for the Json file
        JsonPath = os.path.dirname(__file__)
        JsonFile = os.path.join(JsonPath, "RibbonStructure.json")

        BackupFiles = []
        # returns a list of names (with extension, without full path) of all files
        # in backup path
        for name in os.listdir(pathBackup):
            if os.path.isfile(os.path.join(pathBackup, name)):
                if name.lower().endswith("json"):
                    BackupFiles.append(name)

        if len(BackupFiles) > 0:
            SelectedDile = StandardFunctions.Mbox("Select backup file", "", 21, "NoIcon", BackupFiles[0], BackupFiles)
            BackupFile = os.path.join(pathBackup, SelectedDile)
            result = shutil.copy(BackupFile, JsonFile)
            StandardFunctions.Print(f"Ribbonbar set back to settings from: {result}!", "Warning")
            StandardFunctions.Mbox(f"Settings reset to {SelectedDile}!")

        self.form.close()
        return

    def on_ResetJson_clicked(self):
        self.form.setWindowFlags(Qt.WindowType.WindowStaysOnBottomHint)
        # get the path for the Json file
        JsonPath = os.path.dirname(__file__)
        JsonFile = os.path.join(JsonPath, "RibbonStructure.json")

        BackupFile = [os.path.join(JsonPath, "RibbonStructure_default.json")]

        result = shutil.copy(BackupFile, JsonFile)
        StandardFunctions.Print(f"Ribbonbar reset from {result}!", "Warning")
        StandardFunctions.Mbox("Settings reset to default!")

        self.form.close()
        return

    @staticmethod
    def on_GenerateJson_clicked(self):
        self.WriteJson()
        # Set the button disabled
        self.form.GenerateJson.setDisabled(True)
        return

    @staticmethod
    def on_GenerateJsonExit_clicked(self):
        self.WriteJson()
        # Close the form
        self.form.close()
        return

    def on_EnableBackup_clicked(self):
        if self.form.EnableBackup.isChecked() is True:
            Parameters_Ribbon.ENABLE_BACKUP = True
            Parameters_Ribbon.Settings.SetBoolSetting("BackupEnabled", True)
        if self.form.EnableBackup.isChecked() is False:
            Parameters_Ribbon.ENABLE_BACKUP = False
            Parameters_Ribbon.Settings.SetBoolSetting("BackupEnabled", False)

        # Enable the apply button
        self.form.GenerateJson.setEnabled(True)

        return

    def on_BackUpLocation_clicked(self):
        BackupFolder = ""
        BackupFolder = StandardFunctions.GetFolder(parent=None, DefaultPath=Parameters_Ribbon.BACKUP_LOCATION)
        if BackupFolder != "":
            self.pathBackup = BackupFolder
            self.form.label_4.setText(BackupFolder)
            Parameters_Ribbon.BACKUP_LOCATION = BackupFolder
            Parameters_Ribbon.Settings.SetStringSetting("BackupFolder", BackupFolder)

        # Enable the apply button
        self.form.GenerateJson.setEnabled(True)

        return

    def on_AutoHide_clicked(self):
        if self.form.AutoHide.isChecked() is True:
            Parameters_Ribbon.AUTOHIDE_RIBBON = True
            Parameters_Ribbon.Settings.SetBoolSetting("AutoHideRibbon", True)
        if self.form.AutoHide.isChecked() is False:
            Parameters_Ribbon.AUTOHIDE_RIBBON = False
            Parameters_Ribbon.Settings.SetBoolSetting("AutoHideRibbon", False)

        # Enable the apply button
        self.form.GenerateJson.setEnabled(True)

        return

    def on_IconSize_Small_TextChanged(self):
        Parameters_Ribbon.ICON_SIZE_SMALL = int(self.form.IconSize_Small.text())
        Parameters_Ribbon.Settings.SetIntSetting("IconSize_Small", int(self.form.IconSize_Small.text()))

        # Enable the apply button
        self.form.GenerateJson.setEnabled(True)

        return

    def on_IconSize_Medium_TextChanged(self):
        Parameters_Ribbon.ICON_SIZE_MEDIUM = int(self.form.IconSize_Medium.text())
        Parameters_Ribbon.Settings.SetIntSetting("IconSize_Medium", int(self.form.IconSize_Medium.text()))

        # Enable the apply button
        self.form.GenerateJson.setEnabled(True)

        return

    # def on_IconSize_Large_TextChanged(self):
    #     Parameters_Ribbon.ICON_SIZE_LARGE = int(self.form.IconSize_Large.text())
    #     Parameters_Ribbon.Settings.SetIntSetting("IconSize_Large", int(self.form.IconSize_Large.text()))

    #     # Enable the apply button
    #     self.form.GenerateJson.setEnabled(True)

    #     return

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

        # Enable the apply button
        self.form.GenerateJson.setEnabled(True)

        return

    def on_ShowText_clicked(self):
        if self.form.ShowText.isChecked() is True:
            Parameters_Ribbon.SHOW_ICON_TEXT = True
            Parameters_Ribbon.Settings.SetBoolSetting("ShowIconText", True)
            self.ShowText = True
        if self.form.ShowText.isChecked() is False:
            Parameters_Ribbon.SHOW_ICON_TEXT = False
            Parameters_Ribbon.Settings.SetBoolSetting("ShowIconText", False)
            self.ShowText = False

        # Enable the apply button
        self.form.GenerateJson.setEnabled(True)

        return

    # endregion---------------------------------------------------------------------------------------

    # region - Functions------------------------------------------------------------------------------
    def ReadJson(self):
        """Read the Json file and fill the lists and set settings"""
        # OPen the JsonFile and load the data
        JsonFile = open(os.path.join(os.path.dirname(__file__), "RibbonStructure.json"))
        data = json.load(JsonFile)

        # Get all the ignored toolbars
        for IgnoredToolbar in data["ignoredToolbars"]:
            self.List_IgnoredToolbars.append(IgnoredToolbar)

        # Get all the icon only toolbars
        for IconOnlyToolbar in data["iconOnlyToolbars"]:
            self.List_IconOnlyToolbars.append(IconOnlyToolbar)

        # Get all the quick access command
        for QuickAccessCommand in data["quickAccessCommands"]:
            self.List_QuickAccessCommands.append(QuickAccessCommand)

        # Get all the ignored workbenches
        for IgnoredWorkbench in data["ignoredWorkbenches"]:
            self.List_IgnoredWorkbenches.append(IgnoredWorkbench)

        # Get the showtext value
        self.ShowText = bool(data["showText"])

        # Get the dict with the customized date for the buttons
        self.Dict_RibbonCommandPanel["workbenches"] = data["workbenches"]

        try:
            for Workbench in self.Dict_RibbonCommandPanel["workbenches"]:
                for toolbar in self.Dict_RibbonCommandPanel["workbenches"][Workbench]["toolbars"]:
                    for orderItem in self.Dict_RibbonCommandPanel["workbenches"][Workbench]["toolbars"]["order"]:
                        self.List_SortedToolbars.append(orderItem)
        except Exception:
            pass

        try:
            for Workbench in self.Dict_RibbonCommandPanel["workbenches"]:
                for toolbar in self.Dict_RibbonCommandPanel["workbenches"][Workbench]["toolbars"]:
                    for orderItem in self.Dict_RibbonCommandPanel["workbenches"][Workbench]["toolbars"][toolbar][
                        "order"
                    ]:
                        self.List_SortedCommands.append(orderItem)
        except Exception:
            pass

        JsonFile.close()
        return

    def WriteJson(self):
        # Create a resulting dict
        resultingDict = {}
        # add the various lists to the resulting dict.
        resultingDict["ignoredToolbars"] = self.List_IgnoredToolbars
        resultingDict["iconOnlyToolbars"] = self.List_IconOnlyToolbars
        resultingDict["quickAccessCommands"] = self.List_QuickAccessCommands
        resultingDict["ignoredWorkbenches"] = self.List_IgnoredWorkbenches
        # Add the show text property to the dict
        resultingDict["showText"] = self.ShowText

        # RibbonTabs
        # Get the Ribbon dictionary
        resultingDict.update(self.Dict_RibbonCommandPanel)

        # get the path for the Json file
        JsonPath = os.path.dirname(__file__)
        JsonFile = os.path.join(JsonPath, "RibbonStructure.json")

        # create a copy and rename it as a backup if enabled
        if Parameters_Ribbon.ENABLE_BACKUP is True:
            Suffix = datetime.now().strftime("%Y%m%d_%H%M%S")
            BackupName = f"RibbonStructure_{Suffix}.json"
            BackupFile = os.path.join(pathBackup, BackupName)
            shutil.copy(JsonFile, BackupFile)

        # Writing to sample.json
        with open(JsonFile, "w") as outfile:
            json.dump(resultingDict, outfile, indent=4)

        outfile.close()
        return

    def add_keys_nested_dict(self, dict, keys):
        for key in keys:
            if key not in dict:
                dict[key] = {}
            dict = dict[key]
        try:
            dict.setdefault(keys[-1], 1)
        except Exception:
            pass
        return

    # endregion


def main():
    # Get the form
    Dialog = LoadDialog().form
    # Show the form
    Dialog.show()

    return
