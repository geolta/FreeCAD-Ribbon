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
from PySide.QtGui import QIcon
from PySide.QtWidgets import QListWidgetItem, QTableWidgetItem
from PySide.QtCore import Qt, SIGNAL
import sys
import json

# Get the resources
pathIcons = os.path.dirname(__file__) + "/Resources/icons/"
pathStylSheets = os.path.dirname(__file__) + "/Resources/stylesheets/"
pathUI = os.path.dirname(__file__) + "/Resources/ui/"
sys.path.append(pathIcons)
sys.path.append(pathStylSheets)
sys.path.append(pathUI)

# import graphical created Ui. (With QtDesigner or QtCreator)
import Settings_ui as Settings_ui

# Define the translation
translate = App.Qt.translate


class LoadDialog(Settings_ui.Ui_Form):

    # Define list of the workbenches, toolbars and commands on class level
    List_Workbenches = []
    StringList_Toolbars = []
    List_Commands = []

    List_IgnoredToolbars = []
    List_IconOnlyToolbars = []
    List_QuickAccessCommands = []
    List_IgnoredWorkbenches = []
    List_RibbonCommandSettings = []

    ShowText = False

    def __init__(self):
        # Makes "self.on_CreateBOM_clicked" listen to the changed control values instead initial values
        super(LoadDialog, self).__init__()

        # # this will create a Qt widget from our ui file
        self.form = Gui.PySideUic.loadUi(os.path.join(pathUI, "Settings.ui"))

        # Make sure that the dialog stays on top
        self.form.setWindowFlags(Qt.WindowStaysOnTopHint)

        # Read the jason file and fill the lists
        self.ReadJson()

        # region - create the lists ------------------------------------------------------------------
        #
        # Create a list of all workbenches with their icon
        List_Workbenches = Gui.listWorkbenches().copy()
        for key in List_Workbenches:
            if key != "NoneWorkbench" or key != "" or key is not None:
                Icon = None
                IconName = str(Gui.getWorkbench(key).Icon)
                if IconName != "":
                    Icon = Gui.getIcon(IconName)
                WorkbenchName = Gui.getWorkbench(key).MenuText
                self.List_Workbenches.append([str(key), Icon, WorkbenchName])

        # Create a list of all toolbars
        # Store the current active workbench
        ActiveWB = Gui.activeWorkbench().name()
        # Go through the list of workbenches
        for workbench in self.List_Workbenches:
            # Activate the workbench. Otherwise, .listToolbars() returns empty
            Gui.activateWorkbench(workbench[0])
            # Get the toolbars of this workbench
            wbToolbars = Gui.getWorkbench(workbench[0]).listToolbars()
            # Go through the toolbars
            for Toolbar in wbToolbars:
                # Go through the list of toolbars. If already present, skip it.
                # Otherwise add it the the list.
                IsInList = False
                for i in range(len(self.StringList_Toolbars)):
                    if Toolbar == self.StringList_Toolbars[i]:
                        IsInList = True

                if IsInList is False:
                    self.StringList_Toolbars.append(Toolbar)
        # re-activate the workbench that was stored.
        Gui.activateWorkbench(ActiveWB)

        # Create a list of all commands with their icon
        # Create a copy of the list of command names
        CommandNames = Gui.listCommands().copy()
        # Go through the list
        for CommandName in CommandNames:
            # get the command with this name
            command = Gui.Command.get(CommandName)
            if command is not None:
                # get the icon for this command
                if command.getInfo()["pixmap"] != "":
                    Icon = Gui.getIcon(command.getInfo()["pixmap"])
                    # Add the command and its icon to the command list
                    self.List_Commands.append([CommandName, Icon])
        #
        # endregion ----------------------------------------------------------------------

        # region - Load all controls------------------------------------------------------------------
        #
        # -- Ribbon design tab --
        # Add all workbenches to the ListItem Widget. In this case a dropdown list.
        self.addWorkbenches()
        # Add all toolbars of the selected workbench to the toolbar list(dropdown)
        self.on_WorkbenchList__TextChanged(self, self.List_Workbenches, self.List_IgnoredToolbars)
        # load the commands in the table.
        self.on_ToolbarList__TextChanged(self, self.List_Workbenches)

        # -- Excluded toolbars --
        self.ExcludedToolbars()

        # -- Quick access toolbar tab --
        # Add all commands to the listbox for the quick access toolbar
        self.QuickAccessCommands()
        #
        # endregion-----------------------------------------------------------------------------------

        # region - connect controls with functions----------------------------------------------------
        def LoadWorkbenches():
            self.on_WorkbenchList__TextChanged(self, self.List_Workbenches, self.List_IgnoredToolbars)

        self.form.WorkbenchList.currentTextChanged.connect(LoadWorkbenches)

        def LoadToolbars():
            self.on_ToolbarList__TextChanged(self, self.List_Workbenches)

        self.form.ToolbarList.currentTextChanged.connect(LoadToolbars)
        # endregion

        # region - Modifiy controls-------------------------------------------------------------------
        #
        # -- Ribbon design tab --
        # Settings for the table widget
        self.form.tableWidget.setEnabled(True)
        self.form.tableWidget.horizontalHeader().setVisible(True)
        #
        # endregion

        return

    # region - Control functions----------------------------------------------------------------------
    # Add all toolbars of the selected workbench to the toolbar list(QComboBox)
    @staticmethod
    def on_WorkbenchList__TextChanged(self, WorkBenchList, IgnoredToolbarsList):
        WorkBenchName = ""
        for WorkBench in WorkBenchList:
            if WorkBench[2] == self.form.WorkbenchList.currentText():
                WorkBenchName = WorkBench[0]

        wbToolbars = Gui.getWorkbench(WorkBenchName).listToolbars()

        self.form.ToolbarList.clear()
        for Toolbar in wbToolbars:
            IsIgnored = False
            for IgnoredToolbar in IgnoredToolbarsList:
                if Toolbar == IgnoredToolbar:
                    IsIgnored = True
            if IsIgnored is False:
                self.form.ToolbarList.addItem(Toolbar, "")
        self.on_ToolbarList__TextChanged
        return

    @staticmethod
    def on_ToolbarList__TextChanged(self, WorkBenchList):
        # Get the correct workbench name
        WorkBenchName = ""
        for WorkBench in WorkBenchList:
            if WorkBench[2] == self.form.WorkbenchList.currentText():
                WorkBenchName = WorkBench[0]

        # Get the workbench object
        Workbench = Gui.getWorkbench(WorkBenchName)
        # Get the toolbar name
        Toolbar = self.form.ToolbarList.currentText()
        # Copy the workbench commands
        Commands = Workbench.getToolbarItems().copy()

        # Clear the table
        self.form.tableWidget.setRowCount(0)

        # Get the commands in this toolbar
        ToolbarCommands = []
        for key in Commands:
            if key == Toolbar:
                ToolbarCommands = Commands[key]

        # Go through the list of toolbar commands
        for ToolbarCommand in ToolbarCommands:
            # Get the command
            command = Gui.Command.get(ToolbarCommand)
            # get the icon for this command if there isn't one, leave it None
            Icon = None
            try:
                Icon = Gui.getIcon(command.getInfo()["pixmap"])
            except Exception:
                pass

            # Create the row in the table
            try:
                if command.getInfo()["menuText"] != "" or command.getInfo()["menuText"] != "separator":
                    CommandName = QTableWidgetItem()
                    CommandName.setText(command.getInfo()["menuText"].replace("&", ""))
                    if Icon is not None:
                        self.form.tableWidget.insertRow(self.form.tableWidget.rowCount())
                        CommandName.setIcon(Icon)
                        RowNumber = self.form.tableWidget.rowCount() - 1
                        self.form.tableWidget.setItem(RowNumber, 0, CommandName)

                        Icon_small = QTableWidgetItem()
                        Icon_small.setCheckState(Qt.CheckState.Checked)
                        self.form.tableWidget.setItem(RowNumber, 1, Icon_small)

                        Icon_medium = QTableWidgetItem()
                        Icon_medium.setCheckState(Qt.CheckState.Unchecked)
                        self.form.tableWidget.setItem(RowNumber, 2, Icon_medium)

                        Icon_large = QTableWidgetItem()
                        Icon_large.setCheckState(Qt.CheckState.Unchecked)
                        self.form.tableWidget.setItem(RowNumber, 3, Icon_large)
            except Exception:
                pass

        return

    # endregion---------------------------------------------------------------------------------------

    # region - Functions------------------------------------------------------------------------------
    def addWorkbenches(self):
        """Fill the Workbenches available, selected and workbench list"""
        self.form.WorkbenchList.clear()
        self.form.WorkbenchesAvailable.clear()
        self.form.WorkbenchesSelected.clear()

        for workbench in self.List_Workbenches:
            # Default a workbench is selected
            # if in List_IgnoredWorkbenches, set IsSelected to false
            IsSelected = True
            for IgnoredWorkbench in self.List_IgnoredWorkbenches:
                if workbench[2] == IgnoredWorkbench:
                    IsSelected = False

            # Define a new ListWidgetItem.
            ListWidgetItem = QListWidgetItem()
            ListWidgetItem.setText(workbench[2])
            icon = QIcon(workbench[1])
            ListWidgetItem.setIcon(icon)

            # Add the ListWidgetItem to the correct ListWidget
            if IsSelected is False:
                self.form.WorkbenchesAvailable.addItem(ListWidgetItem)
            if IsSelected is True:
                self.form.WorkbenchesSelected.addItem(ListWidgetItem)
                self.form.WorkbenchList.addItem(icon, workbench[2])

        # Set the text in the combobox to the name of the active workbench
        self.form.WorkbenchList.setCurrentText(Gui.activeWorkbench().name())
        return

    def ExcludedToolbars(self):
        self.form.ToolbarsToExclude.clear()
        self.form.ToolbarsExcluded.clear()

        for Toolbar in self.StringList_Toolbars:
            IsSelected = False
            for IgnoredToolbar in self.List_IgnoredToolbars:
                print(f"{Toolbar}, {IgnoredToolbar}")
                if Toolbar == IgnoredToolbar:
                    IsSelected = True

            ListWidgetItem = QListWidgetItem()
            ListWidgetItem.setText(Toolbar)
            if IsSelected is False:
                self.form.ToolbarsToExclude.addItem(ListWidgetItem)
            if IsSelected is True:
                self.form.ToolbarsExcluded.addItem(ListWidgetItem)
        return

    def QuickAccessCommands(self):
        """Fill the Quick Commands Available and Selected"""
        self.form.CommandsAvailable.clear()
        self.form.CommandesSelected.clear()

        for command in self.List_Commands:
            # Default a command is not selected
            # If in List_QuickAccessCommands set IsSelected to True
            IsSelected = False
            for QuickCommand in self.List_QuickAccessCommands:
                if command[0] == QuickCommand:
                    IsSelected = True

            # Define a new ListWidgetItem.
            ListWidgetItem = QListWidgetItem()
            ListWidgetItem.setText(command[0])
            icon = QIcon(command[1])
            ListWidgetItem.setIcon(icon)

            # Add the ListWidgetItem to the correct ListWidget
            if icon is not None:
                if IsSelected is False:
                    self.form.CommandsAvailable.addItem(ListWidgetItem)
                if IsSelected is True:
                    self.form.CommandesSelected.addItem(ListWidgetItem)
        return

    def ReadJson(self):
        """Read the Json file and fill the lists and set settings"""
        JsonFile = open(os.path.join(os.path.dirname(__file__), "RibbonStructure.json"))
        data = json.load(JsonFile)

        for IgnoredToolbar in data["ignoredToolbars"]:
            self.List_IgnoredToolbars.append(IgnoredToolbar)

        for IconOnlyToolbar in data["iconOnlyToolbars"]:
            self.List_IconOnlyToolbars.append(IconOnlyToolbar)

        for QuickAccessCommand in data["quickAccessCommands"]:
            self.List_QuickAccessCommands.append(QuickAccessCommand)

        for IgnoredWorkbench in data["ignoredWorkbenches"]:
            self.List_IgnoredWorkbenches.append(IgnoredWorkbench)

        self.ShowText = bool(data["showText"])

        for RibbonPanel in data["toolbars"]:
            self.List_IconOnlyToolbars.append(RibbonPanel)

        JsonFile.close()
        return

    # endregion


def main():
    # Get the form
    Dialog = LoadDialog().form
    # Show the form
    Dialog.show()

    return
