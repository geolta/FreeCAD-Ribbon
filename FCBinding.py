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

from PySide6.QtGui import QIcon, QAction, QPixmap
from PySide6.QtWidgets import (
    QToolButton,
    QToolBar,
    QPushButton,
    QLayout,
    QSizePolicy,
    QMenu,
)
from PySide6.QtCore import Qt, QTimer, Signal, QObject, QSize

import json
import os
import sys
import traceback
import logging
import webbrowser

import pyqtribbon
from pyqtribbon import RibbonBar
import LoadDesign_Ribbon
import Parameters_Ribbon
import LoadSettings_Ribbon

# Get the main window of FreeCAD
mw = Gui.getMainWindow()

# Get the resources
pathIcons = Parameters_Ribbon.ICON_LOCATION
pathStylSheets = Parameters_Ribbon.STYLESHEET_LOCATION
pathUI = Parameters_Ribbon.UI_LOCATION
sys.path.append(pathIcons)
sys.path.append(pathStylSheets)
sys.path.append(pathUI)

# Get the main window of FreeCAD
mw = Gui.getMainWindow()

# Define a timer
timer = QTimer()


class ModernMenu(RibbonBar):
    """
    Create ModernMenu QWidget.
    """

    ribbonStructure = None

    wbNameMapping = {}
    isWbLoaded = {}

    # use icon size from FreeCAD preferences
    iconSize: int = App.ParamGet("User parameter:BaseApp/Preferences/General").GetInt("ToolbarIconSize", 24)

    def __init__(self):
        """
        Constructor
        """
        super().__init__(title="", iconSize=self.iconSize)

        self.connectSignals()

        # read ribbon structure from JSON file
        with open(os.path.join(os.path.dirname(__file__), "RibbonStructure.json"), "r") as file:
            ModernMenu.ribbonStructure = json.load(file)

        # Create the ribbon
        self.createModernMenu()
        self.onUserChangedWorkbench()

        # Set the custom stylesheet
        self.setStyleSheet(Parameters_Ribbon.STYLESHEET)
        return

    def connectSignals(self):
        self.tabBar().currentChanged.connect(self.onUserChangedWorkbench)
        mw.workbenchActivated.connect(self.onWbActivated)
        return

    def disconnectSignals(self):
        self.tabBar().currentChanged.disconnect(self.onUserChangedWorkbench)
        mw.workbenchActivated.disconnect(self.onWbActivated)
        return

    def createModernMenu(self):
        """
        Create menu tabs.
        """

        # add quick access buttons
        i = 0  # Start value for button count. Used for width of quixkaccess toolbar
        for commandName in ModernMenu.ribbonStructure["quickAccessCommands"]:
            i = i + 1
            button = QToolButton()
            action = Gui.Command.get(commandName).getAction()
            # XXX for debugging purposes
            if len(action) == 0:
                print(f"{commandName} has no action")
            elif len(action) > 1:
                print(f"{commandName} has more than one action")

            button.setDefaultAction(action[0])
            self.addQuickAccessButton(button)

        # Set the height of the quickaccess toolbar
        self.quickAccessToolBar().setFixedHeight(self.iconSize * 1.5)
        # Set the width of the quickaccess toolbar.
        self.quickAccessToolBar().setMinimumWidth(self.iconSize * i * 3.7795275591 * 0.5)

        # Get the order of workbenches from Parameters
        WorkbenchOrderParam = "User parameter:BaseApp/Preferences/Workbenches/"
        WorkbenchOrderedList = App.ParamGet(WorkbenchOrderParam).GetString("Ordered").split(",")
        # add category for each workbench
        for i in range(len(WorkbenchOrderedList)):
            for workbenchName, workbench in Gui.listWorkbenches().items():
                if workbenchName == WorkbenchOrderedList[i]:
                    if workbenchName == "" or workbench.MenuText in ModernMenu.ribbonStructure["ignoredWorkbenches"]:
                        continue

                    name = workbench.MenuText
                    self.wbNameMapping[name] = workbenchName
                    self.isWbLoaded[name] = False

                    self.addCategory(name)
                    # set tab icon
                    self.tabBar().setTabIcon(len(self.categories()) - 1, QIcon(workbench.Icon))

        # Set the font size of the ribbon tab titles
        self.tabBar().font().setPointSizeF(10)

        # Set the size of the collpseRibbonButton
        self.collapseRibbonButton().setFixedSize(16, 16)

        # Set the helpbutton
        self.helpRibbonButton().setEnabled(True)
        self.helpRibbonButton().setFixedHeight(24)
        # Set the widht of the right toolbar
        self.rightToolBar().setMinimumWidth(self.iconSize * 2 * 1.5)
        # Define an action for the help button
        action = QAction()
        # action.setIcon(Gui.getIcon("help"))
        helpIcon = QIcon()
        pixmap = QPixmap(os.path.join(pathIcons, "Help-browser.svg"))
        helpIcon.addPixmap(pixmap)
        action.setIcon(helpIcon)
        action.triggered.connect(self.onHelpClicked)
        self.helpRibbonButton().setDefaultAction(action)

        # Set the application button
        self.applicationOptionButton().setFixedHeight(self.iconSize)
        self.setApplicationIcon(Gui.getIcon("freecad"))
        Menu = self.addFileMenu()
        DesignButton = Menu.addAction("Ribbon design")
        DesignButton.triggered.connect(self.loadDesignMenu)
        SettingsButton = Menu.addAction("Preferences")
        SettingsButton.triggered.connect(self.loadSettingsMenu)

        # Set the autohide behavior
        self.setAutoHideRibbon(Parameters_Ribbon.AUTOHIDE_RIBBON)

        self.setAcceptDrops(True)
        return

    def loadDesignMenu(self):
        LoadDesign_Ribbon.main()
        return

    def loadSettingsMenu(self):
        LoadSettings_Ribbon.main()
        return

    def onHelpClicked(self):
        HelpParam = "User parameter:BaseApp/Preferences/Mod/Help"
        HelpAdress = App.ParamGet(HelpParam).GetString("Location")
        if HelpAdress == "":
            HelpAdress = Parameters_Ribbon.HELP_ADRESS
        webbrowser.open(HelpAdress, new=2, autoraise=True)
        return

    def onUserChangedWorkbench(self):
        """
        Import selected workbench toolbars to ModernMenu section.
        """

        index = self.tabBar().currentIndex()
        tabName = self.tabBar().tabText(index)
        # category = self.currentCategory()

        # activate selected workbench
        tabName = tabName.replace("&", "")
        Gui.activateWorkbench(self.wbNameMapping[tabName])
        self.onWbActivated()
        return

    def onWbActivated(self):
        # switch tab if necessary
        self.updateCurrentTab()

        # hide normal toolbars
        self.hideClassicToolbars()

        # ensure that workbench is already loaded
        workbench = Gui.activeWorkbench()
        if not hasattr(workbench, "__Workbench__"):
            # XXX for debugging purposes
            print(f"wb {workbench.MenuText} not loaded")

            # wait for 0.1s hoping that after that time the workbench is loaded
            timer.timeout.connect(self.onWbActivated)
            timer.setSingleShot(True)
            timer.start(100)

            return

        # create panels
        self.buildPanels()
        return

    def buildPanels(self):
        # Get the active workbench and get tis name
        workbench = Gui.activeWorkbench()
        workbenchName = workbench.name()

        # check if the panel is already loaded. If so exit this function
        tabName = self.tabBar().tabText(self.tabBar().currentIndex()).replace("&", "")
        if self.isWbLoaded[tabName]:
            return

        # Get the list of toolbars from the active workbench
        ListToolbars: list = workbench.listToolbars()
        # Get custom toolbars that are created in the toolbar enviroment and add them to the list of toolbars
        CustomToolbars = self.List_ReturnCustomToolbars()
        for CustomToolbar in CustomToolbars:
            if CustomToolbar[1] == workbenchName:
                ListToolbars.append(CustomToolbar[0])

        # Get the custom panels and add them to the list of toolbars
        try:
            for CustomPanel in ModernMenu.ribbonStructure["customToolbars"]:
                if ModernMenu.ribbonStructure["customToolbars"][CustomPanel]["workbench"] == workbenchName:
                    ListToolbars.append(CustomPanel)

                    # remove the original toolbars from the list
                    Commands = ModernMenu.ribbonStructure["customToolbars"][CustomPanel]["commands"]
                    for Command in Commands:
                        OriginalToolbar = ModernMenu.ribbonStructure["customToolbars"][CustomPanel]["commands"][Command]
                        ListToolbars.remove(OriginalToolbar)
        except Exception as e:
            print(e)
            pass

        try:
            # Get the order of toolbars
            ToolbarOrder: list = ModernMenu.ribbonStructure["workbenches"][workbenchName]["toolbars"]["order"]

            # Sort the list of toolbars according the toolbar order
            def SortToolbars(toolbar):
                if toolbar == "":
                    return -1

                position = None
                try:
                    position = ToolbarOrder.index(toolbar)
                except ValueError:
                    position = 999999
                return position

            ListToolbars.sort(key=SortToolbars)
        except Exception:
            pass

        # If the toolbar must be ignored, skip it
        for toolbar in ListToolbars:
            if toolbar in ModernMenu.ribbonStructure["ignoredToolbars"]:
                continue

            # Create the panel, use the toolbar name as title
            panel = self.currentCategory().addPanel(
                title=toolbar,
                showPanelOptionButton=False,
            )

            # get list of all buttons in toolbar
            allButtons: list = []
            try:
                TB = mw.findChildren(QToolBar, toolbar)
                allButtons = TB[0].findChildren(QToolButton)
            except Exception:
                pass
            customList = self.List_AddCustomToolbarsToWorkbench(workbenchName, toolbar)
            allButtons.extend(customList)

            if workbenchName in ModernMenu.ribbonStructure["workbenches"]:
                # order buttons like defined in ribbonStructure
                if (
                    toolbar in ModernMenu.ribbonStructure["workbenches"][workbenchName]["toolbars"]
                    and "order" in ModernMenu.ribbonStructure["workbenches"][workbenchName]["toolbars"][toolbar]
                ):
                    positionsList: list = ModernMenu.ribbonStructure["workbenches"][workbenchName]["toolbars"][toolbar][
                        "order"
                    ]

                    # XXX check that positionsList consists of strings only
                    def sortButtons(button: QToolButton):
                        if button.text() == "":
                            return -1

                        position = None
                        try:
                            position = positionsList.index(button.defaultAction().text())
                        except ValueError:
                            position = 999999

                        return position

                    allButtons.sort(key=sortButtons)

            # add buttons to panel
            shadowList = (
                []
            )  # if buttons are used in multiple workbenches, they can show up double. (Sketcher_NewSketch)
            for button in allButtons:
                if button.text() == "":
                    continue
                # If the command is already there, skipp it.
                if shadowList.__contains__(button.text()) is True:
                    continue

                try:
                    action = button.defaultAction()

                    # whether to show text of the button
                    showText = (
                        ModernMenu.ribbonStructure["showText"]
                        and toolbar not in ModernMenu.ribbonStructure["iconOnlyToolbars"]
                    )

                    # try to get alternative text from ribbonStructure
                    try:
                        text = ModernMenu.ribbonStructure["workbenches"][workbenchName]["toolbars"][toolbar][
                            "commands"
                        ][action.data()]["text"]
                        # the text would be overwritten again when the state of the action changes
                        # (e.g. when getting enabled / disabled), therefore the action itself
                        # is manipulated.
                        action.setText(text)
                    except KeyError:
                        text = action.text()

                    # try to get alternative icon from ribbonStructure
                    try:
                        icon_Json = ModernMenu.ribbonStructure["workbenches"][workbenchName]["toolbars"][toolbar][
                            "commands"
                        ][action.data()]["icon"]
                        # action.setIcon(QIcon(os.path.join(pathIcons, icon)))
                        if icon_Json != "":
                            action.setIcon(Gui.getIcon(icon_Json))
                    except KeyError:
                        icon_Json = action.icon()

                    # get button size from ribbonStructure
                    try:
                        buttonSize = ModernMenu.ribbonStructure["workbenches"][workbenchName]["toolbars"][toolbar][
                            "commands"
                        ][action.data()]["size"]
                    except KeyError:
                        buttonSize = "small"  # small as default

                    if buttonSize == "small":
                        btn = panel.addSmallButton(
                            action.text(),
                            action.icon(),
                            alignment=Qt.AlignmentFlag.AlignLeft,
                            showText=showText,
                            fixedHeight=Parameters_Ribbon.ICON_SIZE_SMALL,
                        )
                    elif buttonSize == "medium":
                        btn = panel.addMediumButton(
                            action.text(),
                            action.icon(),
                            alignment=Qt.AlignmentFlag.AlignLeft,
                            showText=showText,
                            fixedHeight=Parameters_Ribbon.ICON_SIZE_MEDIUM,
                        )
                    elif buttonSize == "large":
                        btn = panel.addLargeButton(
                            action.text(),
                            action.icon(),
                            alignment=Qt.AlignmentFlag.AlignLeft,
                            showText=showText,
                            fixedHeight=False,
                        )
                    else:
                        raise NotImplementedError(
                            "Given button size not implemented, only small, medium and large are available."
                        )
                    btn.setDefaultAction(action)
                    # add dropdown menu if necessary
                    if button.menu() is not None:
                        btn.setMenu(button.menu())
                        btn.setPopupMode(QToolButton.InstantPopup)

                except Exception:
                    continue

                # add the button text to the shadowList for checking if buttons are already there.
                shadowList.append(button.text())

        self.isWbLoaded[tabName] = True

        return

    def updateCurrentTab(self):
        currentWbIndex = self.tabBar().indexOf(Gui.activeWorkbench().MenuText)
        currentTabIndex = self.tabBar().currentIndex()

        if currentWbIndex != currentTabIndex:
            self.disconnectSignals()
            self.tabBar().setCurrentIndex(currentWbIndex)
            self.connectSignals()
        return

    def hideClassicToolbars(self):
        for toolbar in mw.findChildren(QToolBar):
            if toolbar.objectName() not in [
                "",
                "draft_status_scale_widget",
                "draft_snap_widget",
            ]:
                toolbar.hide()
        return

    def List_ReturnCustomToolbars(self):
        Toolbars = []

        List_Workbenches = Gui.listWorkbenches().copy()
        for WorkBenchName in List_Workbenches:
            if str(WorkBenchName) != "" or WorkBenchName is not None:
                if str(WorkBenchName) != "NoneWorkbench":
                    CustomToolbars: list = App.ParamGet(
                        "User parameter:BaseApp/Workbench/" + WorkBenchName + "/Toolbar"
                    ).GetGroups()

                    for Group in CustomToolbars:
                        Parameter = App.ParamGet(
                            "User parameter:BaseApp/Workbench/" + WorkBenchName + "/Toolbar/" + Group
                        )
                        Name = Parameter.GetString("Name")

                        Toolbars.append([Name, WorkBenchName])

        return Toolbars

    def List_AddCustomToolbarsToWorkbench(self, WorkBenchName, CustomToolbar):
        ButtonList = []

        try:
            Commands = ModernMenu.ribbonStructure["customToolbars"][CustomToolbar]["commands"]
            Workbench = ModernMenu.ribbonStructure["customToolbars"][CustomToolbar]["workbench"]

            if Workbench == WorkBenchName:
                for key, value in Commands.items():
                    for CommandName in Gui.listCommands():
                        Command = Gui.Command.get(CommandName)
                        MenuText = Command.getInfo()["menuText"]

                        if MenuText == key:
                            action = Command.getAction()[0]
                            action.setData(CommandName)
                            action.setText(CommandName)

                            Button = QToolButton()
                            Button.setDefaultAction(action)
                            Button.setText(MenuText)
                            Button.setObjectName(Command.getInfo()["name"])

                            ButtonList.append(Button)
        except Exception:
            pass

        return ButtonList


class run:
    """
    Activate Modern UI.
    """

    def __init__(self, name):
        """
        Constructor
        """
        disable = 0
        if name != "NoneWorkbench":
            # Disable connection after activation
            mw = Gui.getMainWindow()
            mw.workbenchActivated.disconnect(run)
            if disable:
                return

            ribbon = ModernMenu()
            # Give an offset otherwise the ribbon will go through the menu bar
            ribbon.setContentsMargins(0, 20, 0, 0)
            # Create the ribbon
            mw.setMenuBar(ribbon)
        return


# region - Exception handler--------------------------------------------------------------
#
#
# https://pyqribbon.readthedocs.io/en/stable/apidoc/pyqtribbon.logger.html
# https: // timlehr.com/2018/01/python-exception-hooks-with-qt-message-box/index.html
class UncaughtHook(QObject):
    _exception_caught = Signal(object)

    def __init__(self, *args, **kwargs):
        super(UncaughtHook, self).__init__(*args, **kwargs)

        # this registers the exception_hook() function as hook with the Python interpreter
        sys.excepthook = self.exception_hook

        # connect signal to execute the message box function always on main thread
        # self._exception_caught.connect(show_exception_box)

    def exception_hook(self, exc_type, exc_value, exc_traceback):
        """Function handling uncaught exceptions.
        It is triggered each time an uncaught exception occurs.
        """
        if issubclass(exc_type, KeyboardInterrupt):
            # ignore keyboard interrupt to support console applications
            sys.__excepthook__(exc_type, exc_value, exc_traceback)
        else:
            # ----------Suppressed original handling---------------------------------------
            exc_info = (exc_type, exc_value, exc_traceback)
            # log_msg = '\n'.join([''.join(traceback.format_tb(exc_traceback)),
            #                      '{0}: {1}'.format(exc_type.__name__, exc_value)])
            # log.critical("Uncaught exception:\n {0}".format(log_msg), exc_info=exc_info)

            # trigger message box show
            # self._exception_caught.emit(log_msg)

            App.Console.PrintWarning(
                "RibbonUI: There was an error. This is probally caused by an incompatible FreeCAD plugin!"
            )
            App.Console.PrintWarning(exc_info)
        return


# create a global instance of our exception class to register the hook
# qt_exception_hook = UncaughtHook()
#
#
# endregion=========================================================================================
