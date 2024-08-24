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

from PySide6.QtWidgets import (
    QListWidgetItem,
    QTableWidgetItem,
    QListWidget,
    QTableWidget,
    QSpinBox,
    QWidget,
    QToolBar,
    QComboBox,
    QPushButton,
    QToolButton,
    QTabWidget,
)

# Set the path where you want to save this new Json file
# JsonPath = os.path.dirname(__file__)
JsonPath = "D:\\OneDrive\\Desktop\\"


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
List_IconOnlyToolbars = ["Structure", "Individual views"]
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
Dict_CustomToolbars = {}

List_IgnoredToolbars_internal = []

ShowText_Small = False
ShowText_Medium = False
ShowText_Large = False

# Add workbenches here that you want to exclude from this script.
skipWorkbenchList = []
# skipWorkbenchList = ["PartDesignWorkbench", "AssemblyWorkbench", "SketcherWorkbench"]

# Add toolbars which must have only small icons:
smallOnlyToolbars = ["Structure", "Individual views"]

# Add here your customized panels (toolbars)
Dict_CustomToolbars = {
    "customToolbars": {
        "Loads & boundary conditions": {
            "commands": {
                "Electromagnetic boundary conditions": "Electromagnetic boundary conditions",
                "Initial flow velocity condition": "Fluid boundary conditions",
                "Initial pressure condition": "Fluid boundary conditions",
                "Flow velocity boundary condition": "Fluid boundary conditions",
                "Fixed boundary condition": "Mechanical boundary conditions and loads",
                "Rigid body constraint": "Mechanical boundary conditions and loads",
                "Displacement boundary condition": "Mechanical boundary conditions and loads",
                "Contact constraint": "Mechanical boundary conditions and loads",
                "Tie constraint": "Mechanical boundary conditions and loads",
                "Spring": "Mechanical boundary conditions and loads",
                "Force load": "Mechanical boundary conditions and loads",
                "Pressure load": "Mechanical boundary conditions and loads",
                "Centrifugal load": "Mechanical boundary conditions and loads",
                "Gravity load": "Mechanical boundary conditions and loads",
                "Initial temperature": "Thermal boundary conditions and loads",
                "Heat flux load": "Thermal boundary conditions and loads",
                "Temperature boundary condition": "Thermal boundary conditions and loads",
                "Body heat source": "Thermal boundary conditions and loads",
            },
            "workbench": "FemWorkbench",
        }
    },
}

# Add here your customized workbenches to include.
CustomJson_Workbenches = {
    "workbenches": {
        "PartDesignWorkbench": {
            "toolbars": {
                "Part Design Helper": {
                    "order": [
                        "Create sketch",
                        "Create body",
                        "Validate sketch",
                        "Check Geometry",
                        "Create a sub-object(s) shape binder",
                        "Create a clone",
                        "Create datum",
                    ],
                    "commands": {
                        "PartDesign_CompSketches": {
                            "size": "large",
                            "text": "Create sketch",
                            "icon": "",
                        },
                        "PartDesign_Body": {
                            "size": "small",
                            "text": "Create body",
                            "icon": "PartDesign_Body",
                        },
                        "Sketcher_ValidateSketch": {
                            "size": "small",
                            "text": "Validate sketch...",
                            "icon": "Sketcher_ValidateSketch",
                        },
                        "Part_CheckGeometry": {
                            "size": "small",
                            "text": "Check Geometry",
                            "icon": "Part_CheckGeometry",
                        },
                        "PartDesign_SubShapeBinder": {
                            "size": "small",
                            "text": "Create a sub-object(s) shape binder",
                            "icon": "PartDesign_SubShapeBinder",
                        },
                        "PartDesign_Clone": {
                            "size": "small",
                            "text": "Create a clone",
                            "icon": "PartDesign_Clone",
                        },
                        "PartDesign_CompDatums": {
                            "size": "large",
                            "text": "Create datum",
                            "icon": "",
                        },
                    },
                },
                "Part Design Modeling": {
                    "order": [
                        "Pad",
                        "Create an additive primitive",
                        "Create a subtractive primitive",
                        "Revolution",
                        "Additive loft",
                        "Additive pipe",
                        "Additive helix",
                        "Pocket",
                        "Hole",
                        "Groove",
                        "Subtractive loft",
                        "Subtractive pipe",
                        "Subtractive helix",
                        "Boolean operation",
                    ],
                    "commands": {
                        "PartDesign_Pad": {
                            "size": "large",
                            "text": "Pad",
                            "icon": "PartDesign_Pad",
                        },
                        "PartDesign_Revolution": {
                            "size": "small",
                            "text": "Revolution",
                            "icon": "PartDesign_Revolution",
                        },
                        "PartDesign_AdditiveLoft": {
                            "size": "small",
                            "text": "Additive loft",
                            "icon": "PartDesign_AdditiveLoft",
                        },
                        "PartDesign_AdditivePipe": {
                            "size": "small",
                            "text": "Additive pipe",
                            "icon": "PartDesign_AdditivePipe",
                        },
                        "PartDesign_AdditiveHelix": {
                            "size": "small",
                            "text": "Additive helix",
                            "icon": "PartDesign_AdditiveHelix",
                        },
                        "PartDesign_CompPrimitiveAdditive": {
                            "size": "large",
                            "text": "Create an additive primitive",
                            "icon": "",
                        },
                        "PartDesign_Pocket": {
                            "size": "small",
                            "text": "Pocket",
                            "icon": "PartDesign_Pocket",
                        },
                        "PartDesign_Hole": {
                            "size": "small",
                            "text": "Hole",
                            "icon": "PartDesign_Hole",
                        },
                        "PartDesign_Groove": {
                            "size": "small",
                            "text": "Groove",
                            "icon": "PartDesign_Groove",
                        },
                        "PartDesign_SubtractiveLoft": {
                            "size": "small",
                            "text": "Subtractive loft",
                            "icon": "PartDesign_SubtractiveLoft",
                        },
                        "PartDesign_SubtractivePipe": {
                            "size": "small",
                            "text": "Subtractive pipe",
                            "icon": "PartDesign_SubtractivePipe",
                        },
                        "PartDesign_SubtractiveHelix": {
                            "size": "small",
                            "text": "Subtractive helix",
                            "icon": "PartDesign_SubtractiveHelix",
                        },
                        "PartDesign_CompPrimitiveSubtractive": {
                            "size": "large",
                            "text": "Create a subtractive primitive",
                            "icon": "",
                        },
                        "PartDesign_Boolean": {
                            "size": "small",
                            "text": "Boolean operation",
                            "icon": "PartDesign_Boolean",
                        },
                    },
                },
                "Individual views": {
                    "order": [
                        "Isometric",
                        "Front",
                        "Top",
                        "Right",
                        "Rear",
                        "Bottom",
                        "Left",
                    ],
                    "commands": {
                        "Std_ViewIsometric": {
                            "size": "small",
                            "text": "Isometric",
                            "icon": "view-axonometric",
                        },
                        "Std_ViewFront": {
                            "size": "small",
                            "text": "Front",
                            "icon": "view-front",
                        },
                        "Std_ViewTop": {
                            "size": "small",
                            "text": "Top",
                            "icon": "view-top",
                        },
                        "Std_ViewRight": {
                            "size": "small",
                            "text": "Right",
                            "icon": "view-right",
                        },
                        "Std_ViewRear": {
                            "size": "small",
                            "text": "Rear",
                            "icon": "view-rear",
                        },
                        "Std_ViewBottom": {
                            "size": "small",
                            "text": "Bottom",
                            "icon": "view-bottom",
                        },
                        "Std_ViewLeft": {
                            "size": "small",
                            "text": "Left",
                            "icon": "view-left",
                        },
                    },
                },
            }
        },
    }
}


def main():
    CreateLists()
    CreateJson()
    WriteJson()


def CreateJson():
    # Add your custom workbenches
    if CustomJson_Workbenches != "" or CustomJson_Workbenches is not None:
        for Workbench in CustomJson_Workbenches["workbenches"]:
            skipWorkbenchList.append(Workbench)
        Dict_RibbonCommandPanel.update(CustomJson_Workbenches)

    # Go throug the workbenches
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
            wbToolbars = Gui.getWorkbench(WorkBenchName).getToolbarItems()
            CustomCommands = Dict_ReturnCustomToolbars(WorkBenchName)
            wbToolbars.update(CustomCommands)
            CustomPanelCommands = Dict_AddCustomToolbarsToWorkbench(WorkBenchName)
            wbToolbars.update(CustomPanelCommands)

            # Go through the toolbars
            for key, value in wbToolbars.items():
                Toolbar = key

                # Exclude the toolbars that will be ignored in the RibbonBar
                ToolbarToBeSkipped = False
                for ignoredToolbar in List_IgnoredToolbars:
                    if ignoredToolbar == key:
                        ToolbarToBeSkipped = True
                # Exclude the toolbars that must have only small icons
                for ToolbarToSkip in smallOnlyToolbars:
                    if ToolbarToSkip == key:
                        ToolbarToBeSkipped = True

                if ToolbarToBeSkipped is False:
                    # create a empty size string
                    Size = "small"
                    # Defien empty strings for the command name and icon name
                    CommandName = ""
                    IconName = ""

                    for i2 in range(len(value)):
                        CommandName = value[i2]
                        Command = Gui.Command.get(CommandName)
                        if Command is not None:
                            IconName = Command.getInfo()["pixmap"]
                            MenuName = Command.getInfo()["menuText"].replace("&", "")

                            # Create an empty list for orders
                            Order = []
                            for i3 in range(len(value)):
                                CommandOrder = Gui.Command.get(value[i3])
                                if CommandOrder is not None:
                                    MenuNameOrder = CommandOrder.getInfo()["menuText"].replace("&", "")
                                    Order.append(MenuNameOrder)

                            # Set the first command to large
                            if i2 == 0:
                                Size = "large"

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

                                Dict_RibbonCommandPanel["workbenches"][WorkBenchName]["toolbars"][Toolbar][
                                    "order"
                                ] = Order
                                Dict_RibbonCommandPanel["workbenches"][WorkBenchName]["toolbars"][Toolbar]["commands"][
                                    CommandName
                                ] = {
                                    "size": Size,
                                    "text": MenuName,
                                    "icon": IconName,
                                }
                            if i2 > 0:
                                Size = "small"

                            i2 = i2 + 1
    return


def CreateLists():
    # Create a list of all workbenches with their icon
    List_Workbenches.clear()
    Workbenches = Gui.listWorkbenches()
    for WorkBenchName in Workbenches:
        if str(WorkBenchName) != "":
            if str(WorkBenchName) != "NoneWorkbench" or WorkBenchName is not None:
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
    CustomToolbars = List_ReturnCustomToolbars()
    for Customtoolbar in CustomToolbars:
        StringList_Toolbars.append(Customtoolbar)
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
    # add also custom commands
    Toolbars = List_ReturnCustomToolbars()
    for Toolbar in Toolbars:
        WorkbenchTitle = Toolbar[1]
        for WorkBench in List_Workbenches:
            if WorkbenchTitle == WorkBench[2]:
                WorkBenchName = WorkBench[0]
                for CustomCommand in Toolbar[2]:
                    command = Gui.Command.get(CustomCommand)
                    if command.getInfo()["pixmap"] != "":
                        Icon = Gui.getIcon(command.getInfo()["pixmap"])
                    else:
                        Icon = None
                    MenuName = command.getInfo()["menuText"].replace("&", "")
                    List_Commands.append([CustomCommand, Icon, MenuName, WorkBenchName])
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
    resultingDict.update(Dict_CustomToolbars)
    # Add the show text property to the dict
    resultingDict["showTextSmall"] = ShowText_Small
    resultingDict["showTextMedium"] = ShowText_Medium
    resultingDict["showTextLarge"] = ShowText_Large

    # RibbonTabs
    # Get the Ribbon dictionary
    resultingDict.update(Dict_RibbonCommandPanel)

    # get the path for the Json file
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


def List_ReturnCustomToolbars():
    # Get the main window of FreeCAD
    mw = Gui.getMainWindow()
    Toolbars = []

    List_Workbenches = Gui.listWorkbenches().copy()
    for WorkBenchName in List_Workbenches:
        WorkbenchTitle = Gui.getWorkbench(WorkBenchName).MenuText
        if str(WorkBenchName) != "" or WorkBenchName is not None:
            if str(WorkBenchName) != "NoneWorkbench":
                CustomToolbars: list = App.ParamGet(
                    "User parameter:BaseApp/Workbench/" + WorkBenchName + "/Toolbar"
                ).GetGroups()

                for Group in CustomToolbars:
                    Parameter = App.ParamGet("User parameter:BaseApp/Workbench/" + WorkBenchName + "/Toolbar/" + Group)
                    Name = Parameter.GetString("Name")

                    ListCommands = []
                    # get list of all buttons in toolbar
                    TB = mw.findChildren(QToolBar, Name)
                    allButtons: list = TB[0].findChildren(QToolButton)
                    for button in allButtons:
                        if button.text() == "":
                            continue

                        action = button.defaultAction()
                        if action is not None:
                            Command = action.objectName()
                            ListCommands.append(Command)

                    Toolbars.append([Name, WorkbenchTitle, ListCommands])

    return Toolbars


def Dict_ReturnCustomToolbars(WorkBenchName):
    # Get the main window of FreeCAD
    mw = Gui.getMainWindow()
    Toolbars = {}

    if str(WorkBenchName) != "" or WorkBenchName is not None:
        if str(WorkBenchName) != "NoneWorkbench":
            CustomToolbars: list = App.ParamGet(
                "User parameter:BaseApp/Workbench/" + WorkBenchName + "/Toolbar"
            ).GetGroups()

            for Group in CustomToolbars:
                Parameter = App.ParamGet("User parameter:BaseApp/Workbench/" + WorkBenchName + "/Toolbar/" + Group)
                Name = Parameter.GetString("Name")

                if Name != "":
                    ListCommands = []
                    # get list of all buttons in toolbar
                    TB = mw.findChildren(QToolBar, Name)
                    allButtons: list = TB[0].findChildren(QToolButton)
                    for button in allButtons:
                        if button.text() == "":
                            continue
                        action = button.defaultAction()
                        Command = action.objectName()
                        ListCommands.append(Command)

                        Toolbars[Name] = ListCommands

    return Toolbars


def Dict_AddCustomToolbarsToWorkbench(WorkBenchName):
    Toolbars = {}

    try:
        for CustomToolbar in Dict_CustomToolbars["customToolbars"]:
            ListCommands = []
            Commands = Dict_CustomToolbars["customToolbars"][CustomToolbar]["commands"]
            Workbench = Dict_CustomToolbars["customToolbars"][CustomToolbar]["workbench"]

            if Workbench == WorkBenchName:
                for key, value in Commands.items():
                    for i in range(len(self.List_Commands)):
                        if self.List_Commands[i][2] == key:
                            Command = self.List_Commands[i][0]
                            ListCommands.append(Command)

                    if List_IgnoredToolbars_internal.__contains__(value) is False:
                        List_IgnoredToolbars_internal.append(value)

                Toolbars[CustomToolbar] = ListCommands
    except Exception:
        pass

    return Toolbars


main()
