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

import json


# Define list of the workbenches, toolbars and commands on class level
List_Workbenches = []
StringList_Toolbars = []
List_Commands = []

# Create lists for the several list in the json file.
List_IgnoredToolbars = [
    "Clipboard",
    "Edit",
    "File",
    "Help",
    "Macro",
    "View",
    "Workbench",
]
List_IconOnlyToolbars = [
    "Structure",
]
List_QuickAccessCommands = [
    "Std_New",
    "Std_Save",
    "Std_Undo",
    "Std_Redo",
    "Std_Refresh",
    "Std_Cut",
    "Std_Copy",
    "Std_Paste",
]
List_IgnoredWorkbenches = [
    "Inspection",
    "OpenSCAD",
    "Points",
    "Reverse Engineering",
    "Robot",
    "Test Framework",
]
Dict_RibbonCommandPanel = {}
List_SortedCommands = []
showText = False

# Add workbenches here that you want to exclude from this script.
skipWorkbenchList = []
# skipWorkbenchList = ["PartDesignWorkbench", "AssemblyWorkbench", "SketcherWorkbench"]


def main():
    CreateLists()

    for WorkbenchItem in List_Workbenches:
        WorkBenchName = WorkbenchItem[0]

        # Exclude the workbenches that you want to exclude
        WorkbenchToBeSkipped = False
        for WorkbenchToSkip in skipWorkbenchList:
            if WorkbenchToSkip == WorkBenchName:
                WorkbenchToBeSkipped = True
        # Exclude the workbenches that will be ignored in the RibbonBar
        for WorkbenchToSkip in List_IgnoredWorkbenches:
            if WorkbenchToSkip == WorkBenchName:
                WorkbenchToBeSkipped = True

        if WorkbenchToBeSkipped is False:
            # Activate the workbench. Otherwise, .listToolbars() returns empty
            Gui.activateWorkbench(WorkBenchName)
            # Get the toolbars of this workbench
            wbToolbars = Gui.getWorkbench(WorkBenchName).listToolbars()
            # Go through the toolbars
            for Toolbar in wbToolbars:
                # Exclude the toolbars that will be ignored in the RibbonBar
                ToolbarToBeSkipped = False
                for Toolbar in List_IgnoredToolbars:
                    if Toolbar == WorkBenchName:
                        ToolbarToBeSkipped = True

                if ToolbarToBeSkipped is False:
                    # create a empty size string
                    Size = "small"
                    # Defien empty strings for the command name and icon name
                    CommandName = ""
                    IconName = ""

                    # Go through the list with all available commands.
                    # If the commandText is in this list, get the command name.
                    for i2 in range(len(List_Commands)):
                        CommandName = List_Commands[i2][0]
                        Command = Gui.Command.get(CommandName)
                        IconName = Command.getInfo()["pixmap"]
                        MenuName = List_Commands[i2][2]

                        # Set the first command to large
                        if i2 == 0:
                            Size = "Large"

                            # Create an empty list for orders
                            Order = []

                            add_keys_nested_dict(
                                Dict_RibbonCommandPanel,
                                [
                                    "workbenches",
                                    WorkBenchName,
                                    "toolbars",
                                    Toolbar,
                                    "order",
                                ],
                            )
                            add_keys_nested_dict(
                                Dict_RibbonCommandPanel,
                                [
                                    "workbenches",
                                    WorkBenchName,
                                    "toolbars",
                                    Toolbar,
                                    "commands",
                                    CommandName,
                                ],
                            )

                            Dict_RibbonCommandPanel["workbenches"][WorkBenchName]["toolbars"][Toolbar]["order"] = Order
                            Dict_RibbonCommandPanel["workbenches"][WorkBenchName]["toolbars"][Toolbar]["commands"][
                                CommandName
                            ] = {
                                "size": Size,
                                "text": MenuName,
                                "icon": IconName,
                            }
                        if i2 > 0:
                            Size = "small"

    WriteJson()
    return


def CreateLists():
    # Create a list of all workbenches with their icon
    Workbenches = Gui.listWorkbenches().copy()
    for WorkBenchName in Workbenches:
        if str(WorkBenchName) != "" or WorkBenchName is not None:
            if str(WorkBenchName) != "NoneWorkbench":
                Icon = None
                IconName = str(Gui.getWorkbench(WorkBenchName).Icon)
                if IconName != "":
                    Icon = Gui.getIcon(IconName)
                WorkbenchTitle = Gui.getWorkbench(WorkBenchName).MenuText
                List_Workbenches.append([str(WorkBenchName), Icon, WorkbenchTitle])

    # Create a list of all toolbars
    StringList_Toolbars.clear()
    # Store the current active workbench
    ActiveWB = Gui.activeWorkbench().name()
    # Go through the list of workbenches
    for workbench in List_Workbenches:
        # Activate the workbench. Otherwise, .listToolbars() returns empty
        Gui.activateWorkbench(workbench[0])
        # Get the toolbars of this workbench
        wbToolbars = Gui.getWorkbench(workbench[0]).listToolbars()
        # Go through the toolbars
        for Toolbar in wbToolbars:
            # Go through the list of toolbars. If already present, skip it.
            # Otherwise add it the the list.
            IsInList = False
            for i in range(len(StringList_Toolbars)):
                if Toolbar == StringList_Toolbars[i][0]:
                    IsInList = True

            if IsInList is False:
                StringList_Toolbars.append([Toolbar, workbench[2]])
    # re-activate the workbench that was stored.
    Gui.activateWorkbench(ActiveWB)

    # Create a list of all commands with their icon
    List_Commands.clear()
    # Create a list of command names
    CommandNames = []
    for i in range(len(List_Workbenches)):
        WorkBench = Gui.getWorkbench(List_Workbenches[i][0])
        ToolbarItems = WorkBench.getToolbarItems()
        for key, value in ToolbarItems.items():
            for j in range(len(value)):
                Item = [value[j], List_Workbenches[i][0]]
                # if CommandNames.__contains__(Item) is False:
                IsInList = False
                for k in range(len(CommandNames)):
                    if CommandNames[k][0] == value[j]:
                        IsInList = True
                if IsInList is False:
                    CommandNames.append(Item)

    # Go through the list
    for CommandName in CommandNames:
        # get the command with this name
        command = Gui.Command.get(CommandName[0])
        WorkBenchName = CommandName[1]
        if command is not None:
            # get the icon for this command
            if command.getInfo()["pixmap"] != "":
                Icon = Gui.getIcon(command.getInfo()["pixmap"])
            else:
                Icon = None
            MenuName = command.getInfo()["menuText"].replace("&", "")
            List_Commands.append([CommandName[0], Icon, MenuName, WorkBenchName])
    # endregion ----------------------------------------------------------------------

    return


def WriteJson():
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
    # Get the Ribbon dictionary
    resultingDict.update(Dict_RibbonCommandPanel)

    # get the path for the Json file
    # JsonPath = os.path.dirname(__file__)
    JsonPath = "D:\\OneDrive\\Desktop\\"
    JsonFile = os.path.join(JsonPath, "RibbonStructure_test.json")

    # Writing to sample.json
    with open(JsonFile, "w") as outfile:
        json.dump(resultingDict, outfile, indent=4)

    outfile.close()
    return


def add_keys_nested_dict(dict, keys):
    for key in keys:
        if key not in dict:
            dict[key] = {}
        dict = dict[key]
    try:
        dict.setdefault(keys[-1], 1)
    except Exception:
        pass
    return


main()
