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
from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QListWidgetItem, QTableWidgetItem, QListWidget
from PySide6.QtCore import Qt, SIGNAL
import sys
import json
from datetime import datetime
import shutil

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

    # Create lists for the several list in the json file.
    List_IgnoredToolbars = []
    List_IconOnlyToolbars = []
    List_QuickAccessCommands = []
    List_IgnoredWorkbenches = []
    Dict_RibbonCommandPanel = {}
    # create a list for the changed data for the customized buttons.
    # a list is chosen, so the order list is easier to create from the list widgets

    ShowText = False

    def __init__(self):
        # Makes "self.on_CreateBOM_clicked" listen to the changed control values instead initial values
        super(LoadDialog, self).__init__()

        # # this will create a Qt widget from our ui file
        self.form = Gui.PySideUic.loadUi(os.path.join(pathUI, "Settings.ui"))

        # Make sure that the dialog stays on top
        self.form.setWindowFlags(Qt.WindowStaysOnTopHint)

        # region - create the lists ------------------------------------------------------------------
        #
        # Create a list of all workbenches with their icon
        List_Workbenches = Gui.listWorkbenches().copy()
        for key in List_Workbenches:
            if str(key) != "" or key is not None:
                if str(key) != "NoneWorkbench":
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
                    MenuName = command.getInfo()["menuText"].replace("&", "")
                    # Add the command and its icon to the command list
                    self.List_Commands.append([CommandName, Icon, MenuName])
        #
        # endregion ----------------------------------------------------------------------

        # Read the jason file and fill the lists
        self.ReadJson()

        self.form.WorkbenchList.clear()
        self.form.WorkbenchesAvailable.clear()
        self.form.WorkbenchesSelected.clear()
        self.form.ToolbarsToExclude.clear()
        self.form.ToolbarsExcluded.clear()
        self.form.CommandsAvailable.clear()
        self.form.CommandesSelected.clear()

        # region - Load all controls------------------------------------------------------------------
        #
        # -- Ribbon design tab --
        # Add all workbenches to the ListItem Widget. In this case a dropdown list.
        self.addWorkbenches()
        # Add all toolbars of the selected workbench to the toolbar list(dropdown)
        self.on_WorkbenchList__TextChanged()
        # load the commands in the table.
        self.on_ToolbarList__TextChanged()

        # -- Excluded toolbars --
        self.ExcludedToolbars()

        # -- Quick access toolbar tab --
        # Add all commands to the listbox for the quick access toolbar
        self.QuickAccessCommands()
        #
        # endregion-----------------------------------------------------------------------------------

        # region - connect controls with functions----------------------------------------------------
        def LoadWorkbenches():
            self.on_WorkbenchList__TextChanged()

        self.form.WorkbenchList.currentTextChanged.connect(LoadWorkbenches)

        def LoadToolbars():
            self.on_ToolbarList__TextChanged()

        self.form.ToolbarList.currentTextChanged.connect(LoadToolbars)

        def GenerateJson():
            self.on_GenerateJson_clicked(self)

        self.form.GenerateJson.connect(self.form.GenerateJson, SIGNAL("clicked()"), GenerateJson)

        self.form.tableWidget.itemClicked.connect(self.on_tableCell_clicked)

        # endregion

        # region - Modifiy controls-------------------------------------------------------------------
        #
        # -- TabWidget
        # Set the first tab activated
        self.form.tabWidget.setCurrentWidget(self.form.tabWidget.widget(0))
        # -- Ribbon design tab --
        # Settings for the table widget
        self.form.tableWidget.setEnabled(True)
        self.form.tableWidget.horizontalHeader().setVisible(True)
        #
        # endregion

        return

    # region - Control functions----------------------------------------------------------------------
    # Add all toolbars of the selected workbench to the toolbar list(QComboBox)
    # @staticmethod
    def on_WorkbenchList__TextChanged(self):
        WorkBenchName = ""
        for WorkBench in self.List_Workbenches:
            if WorkBench[2] == self.form.WorkbenchList.currentText():
                WorkBenchName = WorkBench[0]

        wbToolbars = Gui.getWorkbench(WorkBenchName).listToolbars()

        self.form.ToolbarList.clear()
        for Toolbar in wbToolbars:
            IsIgnored = False
            for IgnoredToolbar in self.List_IgnoredToolbars:
                if Toolbar == IgnoredToolbar:
                    IsIgnored = True
            if IsIgnored is False:
                self.form.ToolbarList.addItem(Toolbar, "")
        self.on_ToolbarList__TextChanged
        return

    # @staticmethod
    def on_ToolbarList__TextChanged(self):
        # Get the correct workbench name
        WorkBenchName = ""
        for WorkBench in self.List_Workbenches:
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
            Command = Gui.Command.get(ToolbarCommand)
            if Command is None:
                continue
            CommandName = Command.getInfo()["name"]

            # Get the text
            CommandTitle = Command.getInfo()["menuText"].replace("&", "")
            textAddition = ""
            IconName = ""
            # get the icon for this command if there isn't one, leave it None
            Icon = Gui.getIcon("freecad")
            try:
                Icon = Gui.getIcon(Command.getInfo()["pixmap"])
                IconName = Command.getInfo()["pixmap"]
                # If this is a dropdown, get it's first command and get the icon from thant.
                action = Command.getAction()
                if len(action) > 1:
                    command_0 = Gui.Command.get(action[0].data())
                    Icon = Gui.getIcon(command_0.getInfo()["pixmap"])
                    IconName = Command.getInfo()["pixmap"]
                    textAddition = "..."
            except Exception:
                pass

            # Set the default check states
            checked_small = Qt.CheckState.Checked
            checked_medium = Qt.CheckState.Unchecked
            checked_large = Qt.CheckState.Unchecked
            # set the default size
            Size = "small"

            # Go through the toolbars in the Json Ribbon list
            for WorkBenchName in self.Dict_RibbonCommandPanel["workbenches"]:
                try:
                    for i in range(len(self.List_Workbenches)):
                        if self.List_Workbenches[i][0] == WorkBenchName:
                            CommandTitle = self.Dict_RibbonCommandPanel["workbenches"][WorkBenchName]["toolbars"][
                                Toolbar
                            ]["commands"][CommandName]["text"]
                            Size = self.Dict_RibbonCommandPanel["workbenches"][WorkBenchName]["toolbars"][Toolbar][
                                "commands"
                            ][CommandName]["size"]

                            if Size == "medium":
                                checked_small = Qt.CheckState.Unchecked
                                checked_medium = Qt.CheckState.Checked
                                checked_large = Qt.CheckState.Unchecked
                            if Size == "large":
                                checked_small = Qt.CheckState.Unchecked
                                checked_medium = Qt.CheckState.Unchecked
                                checked_large = Qt.CheckState.Checked
                            Icon_Json_Name = self.Dict_RibbonCommandPanel["workbenches"][WorkBenchName]["toolbars"][
                                Toolbar
                            ]["commands"][CommandName]["icon"]
                            Icon = Gui.getIcon(Icon_Json_Name)
                except Exception:
                    continue

            # Create the row in the table
            # if Command.getInfo()["menuText"] != "" or Command.getInfo()["menuText"] != "separator":
            # add a row to the table widget
            self.form.tableWidget.insertRow(self.form.tableWidget.rowCount())
            # Define a table widget item
            TableWidgetItem = QTableWidgetItem()
            TableWidgetItem.setText(CommandTitle + textAddition)
            if Icon is not None:
                TableWidgetItem.setIcon(Icon)

            # Get the last rownumber and set this row with the TableWidgetItem
            RowNumber = self.form.tableWidget.rowCount() - 1
            self.form.tableWidget.setItem(RowNumber, 0, TableWidgetItem)

            Icon_small = QTableWidgetItem()
            Icon_small.setCheckState(checked_small)
            self.form.tableWidget.setItem(RowNumber, 1, Icon_small)

            Icon_medium = QTableWidgetItem()
            Icon_medium.setCheckState(checked_medium)
            self.form.tableWidget.setItem(RowNumber, 2, Icon_medium)

            Icon_large = QTableWidgetItem()
            Icon_large.setCheckState(checked_large)
            self.form.tableWidget.setItem(RowNumber, 3, Icon_large)

            # Set the IconOnlyToolbars control
            Toolbar = self.form.ToolbarList.currentText()

            for item in self.List_IconOnlyToolbars:
                if item == Toolbar:
                    self.form.IconOnly.setChecked(True)

        return

    def on_IconOnly_clicked(self):
        if self.form.IconOnly.checked is True:
            toolbar = self.form.ToolbarList.currentText()

            isInList = False
            for item in self.List_IconOnlyToolbars:
                if item == toolbar:
                    isInList = True

            if isInList is False:
                self.List_IconOnlyToolbars.append(toolbar)

    def on_tableCell_clicked(self, item):
        # Get the row and column of the clicked item (cell)
        row = item.row()
        column = item.column()
        WorkbenchTitle = self.form.WorkbenchList.currentText()
        WorkBenchName = ""
        for item in self.List_Workbenches:
            if item[2] == WorkbenchTitle:
                WorkBenchName = item[0]

        # get the name of the toolbar
        Toolbar = self.form.ToolbarList.currentText()
        # create a empty size string
        Size = "small"
        # Get the command text from the first cell in the row
        CommandTitle = self.form.tableWidget.item(row, 0).text()

        # Get the checkedstate from the clicked cell
        CheckState = self.form.tableWidget.item(row, column).checkState()
        # Go through the cells in the row. If checkstate is checkd, uncheck the other cells in the row
        for i in range(1, self.form.tableWidget.columnCount()):
            if CheckState == Qt.CheckState.Checked:
                if i == column:
                    self.form.tableWidget.item(row, i).setCheckState(Qt.CheckState.Checked)
                    if i == 1:
                        Size = "small"
                    if i == 2:
                        Size = "medium"
                    if i == 3:
                        Size = "large"
                else:
                    self.form.tableWidget.item(row, i).setCheckState(Qt.CheckState.Unchecked)

        # Defien empty strings for the command name and icon name
        CommandName = ""
        IconName = ""

        # Go through the list with all available commands.
        # If the commandText is in this list, get the command name.

        for i in range(len(self.List_Commands)):
            if CommandTitle == self.List_Commands[i][2]:
                CommandName = self.List_Commands[i][0]
                # With the commandname, get the command and then the iconname
                Command = Gui.Command.get(CommandName)
                IconName = Command.getInfo()["pixmap"]

                # try:
                WorkbenchTitle = self.form.WorkbenchList.currentText()
                for item in self.List_Workbenches:
                    if item[2] == WorkbenchTitle:
                        WorkBenchName = item[0]

                Order = []
                for i in range(1, self.form.tableWidget.rowCount()):
                    Order.append(QTableWidgetItem(self.form.tableWidget.item(i, 0)).text())

                self.add_keys_nested_dict(
                    self.Dict_RibbonCommandPanel,
                    ["workbenches", WorkBenchName, "toolbars", Toolbar, "order"],
                )
                self.add_keys_nested_dict(
                    self.Dict_RibbonCommandPanel,
                    ["workbenches", WorkBenchName, "toolbars", Toolbar, "commands", CommandName],
                )

                self.Dict_RibbonCommandPanel["workbenches"][WorkBenchName]["toolbars"][Toolbar]["order"] = Order
                self.Dict_RibbonCommandPanel["workbenches"][WorkBenchName]["toolbars"][Toolbar]["commands"][
                    CommandName
                ] = {"size": Size, "text": CommandTitle, "icon": IconName}

        return

    @staticmethod
    def on_GenerateJson_clicked(self):
        self.WriteJson()

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

        JsonFile.close()
        return

    def WriteJson(self):
        # Create the internal lists
        List_IgnoredToolbars = []
        List_IconOnlyToolbars = []
        List_QuickAccessCommands = []
        List_IgnoredWorkbenches = []

        # IgnoredToolbars
        ExcludedToolbars = self.ListWidgetItems(self.form.ToolbarsExcluded)
        for i1 in range(len(ExcludedToolbars)):
            IgnoredToolbar = QListWidgetItem(ExcludedToolbars[i1]).text()
            List_IgnoredToolbars.append(IgnoredToolbar)

        # IconOnlyToolbars
        List_IconOnlyToolbars = self.List_IconOnlyToolbars

        # QuickAccessCommands
        SelectedCommands = self.ListWidgetItems(self.form.CommandesSelected)
        for i2 in range(len(SelectedCommands)):
            QuickAccessCommand = QListWidgetItem(SelectedCommands[i2]).text()
            List_QuickAccessCommands.append(QuickAccessCommand)

        # IgnoredWorkbences
        AvailableWorkbenches = self.ListWidgetItems(self.form.WorkbenchesAvailable)
        for i3 in range(len(AvailableWorkbenches)):
            IgnoredWorkbench = QListWidgetItem(AvailableWorkbenches[i3]).text()
            List_IgnoredWorkbenches.append(IgnoredWorkbench)

        # Create a resulting dict
        resultingDict = {}
        # add the various lists to the resulting dict.
        resultingDict["ignoredToolbars"] = List_IgnoredToolbars
        resultingDict["iconOnlyToolbars"] = List_IconOnlyToolbars
        resultingDict["quickAccessCommands"] = List_QuickAccessCommands
        resultingDict["ignoredWorkbenches"] = List_IgnoredWorkbenches
        # Add the show text property to the dict
        resultingDict["showText"] = False

        # RibbonTabs
        # Go through the RibbonCommandPanel list.
        # workbenchDict = {}
        # for workbench in range(len(self.Dict_RibbonCommandPanel_new)):
        resultingDict.update(self.Dict_RibbonCommandPanel)

        # get the path for the Json file
        JsonPath = "D:\\OneDrive\\Desktop"
        JsonFile = os.path.join(JsonPath, "test.json")

        # create a copy and rename it as a backup if enabled
        BackupPath = JsonPath  # to change when settings are enabled
        Suffix = datetime.now().strftime("%Y%m%d_%H%M%S")
        BackupName = f"RibbonStructure_{Suffix}.json"
        BackupFile = os.path.join(BackupPath, BackupName)
        # shutil.copy(JsonFile, BackupFile)

        # Writing to sample.json
        with open(JsonFile, "w") as outfile:
            json.dump(resultingDict, outfile, indent=4)

        outfile.close()

    def add_keys_nested_dict(self, dict, keys):
        for key in keys:
            if key not in dict:
                dict[key] = {}
            dict = dict[key]
        try:
            dict.setdefault(keys[-1], 1)
        except Exception:
            pass

    def ListWidgetItems(self, ListWidget: QListWidget) -> list:
        items = []
        for x in range(ListWidget.count()):
            items.append(ListWidget.item(x))

        return items

    # endregion


def main():
    # Get the form
    Dialog = LoadDialog().form
    # Show the form
    Dialog.show()

    return
