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
from inspect import getsourcefile
from PySide6.QtGui import QPalette, QIcon
from PySide6.QtWidgets import (
    QListWidgetItem,
    QDialogButtonBox,
    QTableWidgetItem,
    QTableWidget,
)
from PySide6.QtCore import SIGNAL, Qt
import sys

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

    def __init__(self):
        # Makes "self.on_CreateBOM_clicked" listen to the changed control values instead initial values
        super(LoadDialog, self).__init__()

        # # this will create a Qt widget from our ui file
        self.form = Gui.PySideUic.loadUi(os.path.join(pathUI, "Settings.ui"))

        # Make sure that the dialog stays on top
        self.form.setWindowFlags(Qt.WindowStaysOnTopHint)

        # region - create the lists ------------------------------------------------------------------

        # Create a list of all workbenches with their icon
        List_Workbenches = Gui.listWorkbenches().copy()
        for key in List_Workbenches:
            if key != "NoneWorkbench" or key != "" or key is not None:
                Icon = None
                IconName = str(Gui.getWorkbench(key).Icon)
                if IconName != "":
                    Icon = Gui.getIcon(IconName)
                self.List_Workbenches.append([str(key), Icon])

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
                Icon = Gui.getIcon(command.getInfo()["pixmap"])
                # Add the command and its icon to the command list
                self.List_Commands.append([CommandName, Icon])
        # endregion ----------------------------------------------------------------------

        # region - Load all controls------------------------------------------------------------------
        # Add all workbenches to the ListItem Widget. In this case a dropdown list.
        self.addWorkbenches()

        # Add all toolbars of the selected workbench to the toolbar list(dropdown)
        self.on_WorkbenchList__TextChanged()

        self.on_ToolbarList__TextChanged()

        # Add all commands to the listbox for available commands
        self.AddCommands()
        # endregion----------------------------------------------------------------------------------

        # region - connect controls with functions----------------------------------------------------
        self.form.WorkbenchList.currentTextChanged.connect(
            self.on_WorkbenchList__TextChanged
        )

        self.form.ToolbarList.currentTextChanged.connect(
            self.on_ToolbarList__TextChanged
        )
        # endregion

        self.form.tableWidget.setEnabled(True)
        # test = QTableWidget
        # test.setEnabled(test, True)
        return

    # region - Control functions----------------------------------------------------------------------
    # Add all toolbars of the selected workbench to the toolbar list(QComboBox)
    def on_WorkbenchList__TextChanged(self):
        wbToolbars = Gui.getWorkbench(
            self.form.WorkbenchList.currentText()
        ).listToolbars()
        self.form.ToolbarList.clear()
        for Toolbar in wbToolbars:
            self.form.ToolbarList.addItem(Toolbar, "")
        self.on_ToolbarList__TextChanged
        return

    def on_ToolbarList__TextChanged(self):
        Workbench = Gui.getWorkbench(self.form.WorkbenchList.currentText())
        Toolbar = self.form.ToolbarList.currentText()
        Commands = Workbench.getToolbarItems().copy()

        self.form.tableWidget.clearContents()

        ToolbarCommands = []
        for key in Commands:
            if key == Toolbar:
                ToolbarCommands = Commands[key]

        for ToolbarCommand in ToolbarCommands:
            # Get the command
            command = Gui.Command.get(ToolbarCommand)
            # get the icon for this command
            Icon = Gui.getIcon(command.getInfo()["pixmap"])

            self.form.tableWidget.insertRow(self.form.tableWidget.rowCount())
            CommandName = QTableWidgetItem()
            CommandName.setFlags(Qt.ItemFlag.ItemIsEnabled)
            CommandName.setFlags(Qt.ItemFlag.ItemIsSelectable)
            CommandName.setText(command.getInfo()["menuText"].replace("&", ""))
            if Icon is not None:
                CommandName.setIcon(Icon)
            self.form.tableWidget.setItem(
                self.form.tableWidget.rowCount() - 1, 0, CommandName
            )

            Icon_small = QTableWidgetItem()
            Icon_small.setFlags(Qt.ItemFlag.ItemIsEnabled)
            Icon_small.setFlags(Qt.ItemFlag.ItemIsSelectable)
            Icon_small.setFlags(Qt.ItemFlag.ItemIsUserCheckable)
            Icon_small.setCheckState(Qt.CheckState.Checked)
            self.form.tableWidget.setItem(
                self.form.tableWidget.rowCount() - 1, 1, Icon_small
            )

            Icon_medium = QTableWidgetItem()
            Icon_medium.setFlags(Qt.ItemFlag.ItemIsEnabled)
            Icon_medium.setFlags(Qt.ItemFlag.ItemIsSelectable)
            Icon_medium.setFlags(Qt.ItemFlag.ItemIsUserCheckable)
            Icon_medium.setCheckState(Qt.CheckState.Unchecked)
            self.form.tableWidget.setItem(
                self.form.tableWidget.rowCount() - 1, 2, Icon_medium
            )

            Icon_large = QTableWidgetItem()
            Icon_large.setFlags(Qt.ItemFlag.ItemIsEnabled)
            Icon_medium.setFlags(Qt.ItemFlag.ItemIsSelectable)
            Icon_large.setFlags(Qt.ItemFlag.ItemIsUserCheckable)
            Icon_large.setCheckState(Qt.CheckState.Unchecked)
            self.form.tableWidget.setItem(
                self.form.tableWidget.rowCount() - 1, 3, Icon_large
            )

        return

    # endregion---------------------------------------------------------------------------------------

    # region - Functions------------------------------------------------------------------------------
    def addWorkbenches(self):
        for workbench in self.List_Workbenches:
            # Define a new ListWidgetItem.
            ListWidgetItem = QListWidgetItem()
            ListWidgetItem.setText(workbench[0])
            icon = QIcon(workbench[1])
            ListWidgetItem.setIcon(icon)
            # Add the ListWidgetItem to the ListItem Widget
            self.form.WorkbenchList.addItem(icon, workbench[0])
        self.form.WorkbenchList.setCurrentText(Gui.activeWorkbench().name())
        return

    def AddCommands(self):
        for command in self.List_Commands:
            ListWidgetItem = QListWidgetItem()
            ListWidgetItem.setText(command[0])
            icon = QIcon(command[1])
            ListWidgetItem.setIcon(icon)
            self.form.CommandsAvailable.addItem(ListWidgetItem)
        return

    # endregion


def main():
    # Get the form
    Dialog = LoadDialog().form
    # Show the form
    Dialog.show()

    return
