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

from PySide6.QtGui import QIcon, QAction, QPixmap, QScrollEvent, QKeyEvent
from PySide6.QtWidgets import QToolButton, QToolBar, QSizePolicy, QDockWidget, QWidget, QMenuBar, QMenu, QMainWindow
from PySide6.QtCore import Qt, QTimer, Signal, QObject, QMetaMethod, SIGNAL, QEvent

import json
import os
import sys
import webbrowser
import LoadDesign_Ribbon
import Parameters_Ribbon
import LoadSettings_Ribbon
import Standard_Functions_RIbbon as StandardFunctions
import platform
import time


# import modules for keypress detection based on OS
if platform.system() == "Windows" or platform.system() == "Darwin":
    import keyboard


# Get the resources
pathIcons = Parameters_Ribbon.ICON_LOCATION
pathStylSheets = Parameters_Ribbon.STYLESHEET_LOCATION
pathUI = Parameters_Ribbon.UI_LOCATION
pathScripts = os.path.join(os.path.dirname(__file__), "Scripts")
pathPackages = os.path.join(os.path.dirname(__file__), "Resources", "packages")
sys.path.append(pathIcons)
sys.path.append(pathStylSheets)
sys.path.append(pathUI)
sys.path.append(pathPackages)

try:
    from pyqtribbon.ribbonbar import RibbonMenu, RibbonBar, RibbonStyle
except ImportError:
    from pyqtribbon_local.ribbonbar import RibbonMenu, RibbonBar, RibbonStyle

    print("pyqtribbon used local")


# Get the main window of FreeCAD
mw = Gui.getMainWindow()

# Define a timer
timer = QTimer()


class ModernMenu(RibbonBar):
    """
    Create ModernMenu QWidget.
    """

    ribbonStructure = {}

    wbNameMapping = {}
    isWbLoaded = {}

    MainWindowLoaded = False

    UseQtKeyPress = False

    # use icon size from FreeCAD preferences
    iconSize = Parameters_Ribbon.ICON_SIZE_SMALL

    sizeFactor = 1.2

    def __init__(self):
        """
        Constructor
        """
        super().__init__(title="", iconSize=self.iconSize)
        self.setObjectName("Ribbon")

        # connect the signals
        self.connectSignals()

        # Set the icon size if parameters has none
        # Define the icon sizes
        if (
            Parameters_Ribbon.Settings.GetIntSetting("IconSize_Small") is None
            or Parameters_Ribbon.Settings.GetIntSetting("IconSize_Small") == 0
        ):
            Parameters_Ribbon.Settings.SetIntSetting("IconSize_Small", 30)

        if (
            Parameters_Ribbon.Settings.GetIntSetting("IconSize_Medium") is None
            or Parameters_Ribbon.Settings.GetIntSetting("IconSize_Medium") == 0
        ):
            Parameters_Ribbon.Settings.SetIntSetting("IconSize_Medium", 40)

        # read ribbon structure from JSON file
        with open(os.path.join(os.path.dirname(__file__), "RibbonStructure.json"), "r") as file:
            self.ribbonStructure.update(json.load(file))
        file.close()

        # Create the ribbon
        self.createModernMenu()
        self.onUserChangedWorkbench()

        # Set the custom stylesheet
        self.setStyleSheet(Parameters_Ribbon.STYLESHEET)

        # get the state of the mainwindow
        self.MainWindowLoaded = True

        # Set these settings and connections at init
        # Set the autohide behavior of the ribbon
        self.setAutoHideRibbon(Parameters_Ribbon.AUTOHIDE_RIBBON)
        # connect the collapsbutton with our own function
        self.collapseRibbonButton().connect(
            self.collapseRibbonButton(),
            SIGNAL("clicked()"),
            self.onCollapseRibbonButton_clicked,
        )

        # Set the menuBar hidden as standard
        mw.menuBar().hide()
        if self.isEnabled() is False:
            mw.menuBar().show()

        # Get the keypress when on linux
        if platform.system() == "Linux" or platform.system() == "Darwin":
            self.UseQtKeyPress = True

        # Get the keypress when on windows or mac
        if platform.system() == "Windows" or platform.system() == "Darwin":
            try:
                # connect the alt key to the menuBar
                keyboard.on_press_key("alt", lambda _: self.ToggleMenuBar())
            except Exception:  # Use Qt incase of an error
                self.UseQtKeyPress = True
        return

    # The backup keypress event
    def keyPressEvent(self, event):
        if self.UseQtKeyPress is True:
            if event.key() == Qt.Key.Key_Alt or event.key() == Qt.Key.Key_AltGr:
                self.ToggleMenuBar()

    # implentation to add actions to the Filemenu. Needed for the accessiores menu
    def addAction(self, action: QAction):
        menu = self.findChild(RibbonMenu, "")
        if menu is None:
            menu = self.addFileMenu()
        menu.addAction(action)
        return

    # used to scroll a ribbon horizontal, when it's wider than the screen
    def wheelEvent(self, event):
        x = 0
        # Get the scroll value (1 or -1)
        delta = event.angleDelta().y()
        x += delta and delta // abs(delta)

        # go back or forward based on x.
        if x == 1:
            self.currentCategory()._previousButton.click()
        if x == -1:
            self.currentCategory()._nextButton.click()

        return

    def getkey():
        old_settings = termios.tcgetattr(sys.stdin)
        tty.setcbreak(sys.stdin.fileno())
        try:
            while True:
                b = os.read(sys.stdin.fileno(), 3).decode()
                if len(b) == 3:
                    k = ord(b[2])
                else:
                    k = ord(b)
                key_mapping = {
                    127: "backspace",
                    10: "return",
                    32: "space",
                    9: "tab",
                    27: "esc",
                    65: "up",
                    66: "down",
                    67: "right",
                    68: "left",
                }
                return key_mapping.get(k, chr(k))
        finally:
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

    # region - Hover function needed for handling the autohide function of the ribbon
    def enterEvent(self, QEvent):
        TB = mw.findChildren(QDockWidget, "Ribbon")[0]

        if self.ribbonVisible() is False:
            TB.setMaximumHeight(200)
            self.setRibbonVisible(True)
        pass

    def leaveEvent(self, QEvent):
        TB = mw.findChildren(QDockWidget, "Ribbon")[0]

        if self._autoHideRibbon is True:
            TB.setMaximumHeight(45)
            self.setRibbonVisible(False)
        pass

    # endregion

    def connectSignals(self):
        self.tabBar().currentChanged.connect(self.onUserChangedWorkbench)
        mw.workbenchActivated.connect(self.onWbActivated)
        return

    def disconnectSignals(self):
        self.tabBar().currentChanged.disconnect(self.onUserChangedWorkbench)
        mw.workbenchActivated.disconnect(self.onWbActivated)
        return

    def ToggleMenuBar(self):
        mw = Gui.getMainWindow()
        menuBar = mw.menuBar()
        if menuBar.isVisible() is True:
            menuBar.hide()
            return
        if menuBar.isVisible() is False:
            menuBar.show()
            return

    def createModernMenu(self):
        """
        Create menu tabs.
        """
        # add quick access buttons
        i = 2  # Start value for button count. Used for width of quixkaccess toolbar
        for commandName in self.ribbonStructure["quickAccessCommands"]:
            i = i + 1
            button = QToolButton()
            QuickAction = Gui.Command.get(commandName).getAction()
            # XXX for debugging purposes
            if len(QuickAction) == 0:
                print(f"{commandName} has no action")
            elif len(QuickAction) > 1:
                print(f"{commandName} has more than one action")

            button.setDefaultAction(QuickAction[0])
            button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            self.addQuickAccessButton(button)

        # Set the height of the quickaccess toolbar
        self.quickAccessToolBar().setMaximumHeight(self.iconSize * self.sizeFactor)
        # Set the width of the quickaccess toolbar.
        self.quickAccessToolBar().setMinimumWidth(self.iconSize * i * self.sizeFactor)
        self.quickAccessToolBar().setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        # Get the order of workbenches from Parameters
        WorkbenchOrderParam = "User parameter:BaseApp/Preferences/Workbenches/"
        WorkbenchOrderedList = App.ParamGet(WorkbenchOrderParam).GetString("Ordered").split(",")
        # add category for each workbench
        for i in range(len(WorkbenchOrderedList)):
            for workbenchName, workbench in Gui.listWorkbenches().items():
                if workbenchName == WorkbenchOrderedList[i]:
                    if workbenchName == "" or workbench.MenuText in self.ribbonStructure["ignoredWorkbenches"]:
                        continue

                    name = workbench.MenuText
                    self.wbNameMapping[name] = workbenchName
                    self.isWbLoaded[name] = False

                    self.addCategory(name)
                    # set tab icon
                    self.tabBar().setTabIcon(len(self.categories()) - 1, QIcon(workbench.Icon))

        # Set the font size of the ribbon tab titles
        self.tabBar().font().setPointSizeF(10)
        self.tabBar().setFixedHeight(self.iconSize * self.sizeFactor)

        # Set the size of the collpseRibbonButton
        self.collapseRibbonButton().setFixedSize(self.iconSize, self.iconSize)

        # Set the helpbutton
        self.helpRibbonButton().setEnabled(True)
        self.helpRibbonButton().setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.helpRibbonButton().setMaximumWidth(self.iconSize * self.sizeFactor)
        # Define an action for the help button
        helpAction = QAction()
        helpIcon = QIcon()
        pixmap = QPixmap(os.path.join(pathIcons, "Help-browser.svg"))
        helpIcon.addPixmap(pixmap)
        helpAction.setIcon(helpIcon)
        helpAction.triggered.connect(self.onHelpClicked)
        self.helpRibbonButton().setDefaultAction(helpAction)

        # Add a button the enable or disable AutoHide
        pixmap = QPixmap(os.path.join(pathIcons, "pin-icon-open.svg"))
        pinIcon = QIcon()
        pinIcon.addPixmap(pixmap)
        pinButton = QToolButton()
        pinButton.setCheckable(True)
        pinButton.setIcon(pinIcon)
        pinButton.setText("Pin Ribbon")
        pinButton.setToolTip("Click to toggle the autohide function on or off")
        pinButton.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        pinButton.setMaximumWidth(self.iconSize * self.sizeFactor)
        if Parameters_Ribbon.AUTOHIDE_RIBBON is True:
            pinButton.setChecked(False)
        if Parameters_Ribbon.AUTOHIDE_RIBBON is False:
            pinButton.setChecked(True)
        pinButton.clicked.connect(self.onPinClicked)
        self.rightToolBar().addWidget(pinButton)

        # Set the widht of the right toolbar
        i = len(self.rightToolBar().actions())
        self.rightToolBar().setMinimumWidth(self.iconSize * self.sizeFactor * i)
        self.rightToolBar().setMaximumHeight(self.iconSize * self.sizeFactor)
        self.rightToolBar().setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        # Set the application button
        self.applicationOptionButton().setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.setApplicationIcon(Gui.getIcon("freecad"))
        Menu = self.addFileMenu()

        # add the menus from the menubar to the application button
        MenuBar = mw.menuBar()
        Menu.addActions(MenuBar.actions())

        # Add the ribbon design button
        Menu.addSeparator()
        DesignMenu = Menu.addMenu("Customize...")
        DesignButton = DesignMenu.addAction("Ribbon Design")
        DesignButton.triggered.connect(self.loadDesignMenu)
        # Add the preference button
        PreferenceButton = DesignMenu.addAction("Ribbon Preferences")
        PreferenceButton.triggered.connect(self.loadSettingsMenu)
        # Add the script submenu with items
        ScriptDir = os.path.join(os.path.dirname(__file__), "Scripts")
        if os.path.exists(ScriptDir) is True:
            ListScripts = os.listdir(ScriptDir)
            if len(ListScripts) > 0:
                ScriptButtonMenu = DesignMenu.addMenu("Scripts")
                for i in range(len(ListScripts)):
                    ScriptButtonMenu.addAction(
                        ListScripts[i],
                        lambda i=i + 1: self.LoadMarcoFreeCAD(ListScripts[i - 1]),
                    )

        return

    def loadDesignMenu(self):
        message = "All workbenches need to be loaded.\nThis can take a couple of minutes.\nDo you want to proceed?"
        result = StandardFunctions.Mbox(message, "", 1, IconType="Question")
        if result == "yes":
            LoadDesign_Ribbon.main()
        # LoadingDialog.main()
        return

    def loadSettingsMenu(self):
        LoadSettings_Ribbon.main()
        return

    def onCollapseRibbonButton_clicked(self):
        TB = mw.findChildren(QDockWidget, "Ribbon")[0]

        if self.ribbonVisible() is False:
            TB.setMaximumHeight(45)
        else:
            TB.setMaximumHeight(200)

        return

    def onPinClicked(self):
        if self._autoHideRibbon is True:
            self.setAutoHideRibbon(False)
            Parameters_Ribbon.Settings.SetBoolSetting("AutoHideRibbon", False)
            self.onCollapseRibbonButton_clicked()
            return
        if self._autoHideRibbon is False:
            self.setAutoHideRibbon(True)
            Parameters_Ribbon.Settings.SetBoolSetting("AutoHideRibbon", True)
            self.onCollapseRibbonButton_clicked()
            return

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
            for CustomPanel in self.ribbonStructure["customToolbars"][workbenchName]:
                ListToolbars.append(CustomPanel)

                # remove the original toolbars from the list
                Commands = self.ribbonStructure["customToolbars"][workbenchName][CustomPanel]["commands"]
                for Command in Commands:
                    try:
                        OriginalToolbar = self.ribbonStructure["customToolbars"][workbenchName][CustomPanel][
                            "commands"
                        ][Command]
                        ListToolbars.remove(OriginalToolbar)
                    except Exception:
                        continue
        except Exception as e:
            print(e)
            pass

        try:
            # Get the order of toolbars
            ToolbarOrder: list = self.ribbonStructure["workbenches"][workbenchName]["toolbars"]["order"]

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
            if toolbar in self.ribbonStructure["ignoredToolbars"]:
                continue
            if toolbar == "":
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

            if workbenchName in self.ribbonStructure["workbenches"]:
                # order buttons like defined in ribbonStructure
                if (
                    toolbar in self.ribbonStructure["workbenches"][workbenchName]["toolbars"]
                    and "order" in self.ribbonStructure["workbenches"][workbenchName]["toolbars"][toolbar]
                ):
                    positionsList: list = self.ribbonStructure["workbenches"][workbenchName]["toolbars"][toolbar][
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
                # if the button has not text, skipp it.
                if button.text() == "":
                    continue
                # add a separator instead of a button if the text is "separator"
                if (
                    workbenchName in self.ribbonStructure["workbenches"]
                    and toolbar in self.ribbonStructure["workbenches"][workbenchName]["toolbars"]
                    and "order" in self.ribbonStructure["workbenches"][workbenchName]["toolbars"][toolbar]
                ):
                    for i in range(
                        1,
                        len(self.ribbonStructure["workbenches"][workbenchName]["toolbars"][toolbar]["order"]),
                    ):
                        command = self.ribbonStructure["workbenches"][workbenchName]["toolbars"][toolbar]["order"][i]
                        commandPrevious = self.ribbonStructure["workbenches"][workbenchName]["toolbars"][toolbar][
                            "order"
                        ][i - 1]

                        if command == button.text() and commandPrevious.lower() == "separator":
                            panel.addSeparator()
                            continue
                # If the command is already there, skipp it.
                if shadowList.__contains__(button.text()) is True:
                    continue

                try:
                    action = button.defaultAction()

                    # try to get alternative text from ribbonStructure
                    try:
                        text = self.ribbonStructure["workbenches"][workbenchName]["toolbars"][toolbar]["commands"][
                            action.data()
                        ]["text"]
                        # the text would be overwritten again when the state of the action changes
                        # (e.g. when getting enabled / disabled), therefore the action itself
                        # is manipulated.
                        action.setText(text)
                    except KeyError:
                        text = action.text()

                    if action.icon() is None:
                        commandName = self.ribbonStructure["workbenches"][workbenchName]["toolbars"][toolbar][
                            "commands"
                        ][action.data()]
                        command = Gui.Command.get(commandName)
                        action.setIcon(Gui.getIcon(command.getInfo()["pixmap"]))

                    # try to get alternative icon from ribbonStructure
                    try:
                        icon_Json = self.ribbonStructure["workbenches"][workbenchName]["toolbars"][toolbar]["commands"][
                            action.data()
                        ]["icon"]
                        if icon_Json != "":
                            action.setIcon(Gui.getIcon(icon_Json))
                    except KeyError:
                        icon_Json = action.icon()

                    # get button size from ribbonStructure
                    try:
                        buttonSize = self.ribbonStructure["workbenches"][workbenchName]["toolbars"][toolbar][
                            "commands"
                        ][action.data()]["size"]
                    except KeyError:
                        buttonSize = "small"  # small as default

                    # Check if this is an icon only toolbar
                    IconOnly = False
                    for iconToolbar in self.ribbonStructure["iconOnlyToolbars"]:
                        if iconToolbar == toolbar:
                            IconOnly = True

                    if buttonSize == "small":
                        showText = Parameters_Ribbon.SHOW_ICON_TEXT_SMALL
                        if IconOnly is True:
                            showText = False

                        btn = panel.addSmallButton(
                            action.text(),
                            action.icon(),
                            alignment=Qt.AlignmentFlag.AlignLeft,
                            showText=showText,
                            fixedHeight=Parameters_Ribbon.ICON_SIZE_SMALL,
                        )
                        if Parameters_Ribbon.SHOW_ICON_TEXT_SMALL is False:
                            btn.setMinimumWidth(Parameters_Ribbon.ICON_SIZE_SMALL + self.iconSize)
                    elif buttonSize == "medium":
                        showText = Parameters_Ribbon.SHOW_ICON_TEXT_MEDIUM
                        if IconOnly is True:
                            showText = False

                        btn = panel.addMediumButton(
                            action.text(),
                            action.icon(),
                            alignment=Qt.AlignmentFlag.AlignLeft,
                            showText=showText,
                            fixedHeight=Parameters_Ribbon.ICON_SIZE_MEDIUM,
                        )
                        if Parameters_Ribbon.SHOW_ICON_TEXT_MEDIUM is False:
                            btn.setMinimumWidth(Parameters_Ribbon.ICON_SIZE_MEDIUM + self.iconSize)
                    elif buttonSize == "large":
                        showText = Parameters_Ribbon.SHOW_ICON_TEXT_LARGE
                        if IconOnly is True:
                            showText = False

                        btn = panel.addLargeButton(
                            action.text(),
                            action.icon(),
                            alignment=Qt.AlignmentFlag.AlignLeft,
                            showText=showText,
                            fixedHeight=False,
                        )
                        if Parameters_Ribbon.SHOW_ICON_TEXT_LARGE is False:
                            btn.setMinimumWidth(btn.maximumHeight())
                    else:
                        raise NotImplementedError(
                            "Given button size not implemented, only small, medium and large are available."
                        )

                    # add dropdown menu if necessary
                    if button.menu() is not None:
                        btn.setMenu(button.menu())
                        btn.setPopupMode(QToolButton.ToolButtonPopupMode.MenuButtonPopup)
                        # btn.setStyleSheet("QToolButton::menu-button {width: 16px")
                    btn.setDefaultAction(action)

                except Exception:
                    continue

                # add the button text to the shadowList for checking if buttons are already there.
                shadowList.append(button.text())

            if panel.title().endswith("_custom"):
                panel.setTitle(panel.title().replace("_custom", ""))

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

        List_Workbenches = Gui.listWorkbenches()
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
            # Get the commands from the custom panel
            Commands = self.ribbonStructure["customToolbars"][WorkBenchName][CustomToolbar]["commands"]

            # Get the command and its original toolbar
            for key, value in Commands.items():
                # get the menu text from the command list
                for CommandName in Gui.listCommands():
                    Command = Gui.Command.get(CommandName)
                    MenuText = Command.getInfo()["menuText"]

                    if MenuText == key:
                        try:
                            # Get the original toolbar as QToolbar
                            OriginalToolBar = mw.findChild(QToolBar, value)
                            # Go through all it's QtoolButtons
                            for Child in OriginalToolBar.findChildren(QToolButton):
                                # If the text of the QToolButton matches the menu text
                                # Add it to the button list.
                                if Child.text() == MenuText:
                                    ButtonList.append(Child)
                        except Exception as e:
                            print(e)
                            continue
        except Exception:
            pass

        return ButtonList

    def LoadMarcoFreeCAD(self, scriptName):
        if self.MainWindowLoaded is True:
            script = os.path.join(pathScripts, scriptName)
            if script.endswith(".py"):
                App.loadFile(script)
        return


class MainWindow(QMainWindow):
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Alt or event.key() == Qt.Key.Key_AltGr:
            self.ToggleMenuBar()

    def ToggleMenuBar(self):
        mw = self
        menuBar = mw.menuBar()
        if menuBar.isVisible() is True:
            menuBar.hide()
            return
        if menuBar.isVisible() is False:
            menuBar.show()
            return


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
            mw.workbenchActivated.disconnect(run)
            if disable:
                return

            ribbon = ModernMenu()
            ribbonDock = QDockWidget()
            # set the name of the object and the window title
            ribbonDock.setObjectName("Ribbon")
            ribbonDock.setWindowTitle("Ribbon")
            # Set the titlebar to an empty widget (effectivly hide it)
            ribbonDock.setTitleBarWidget(QWidget())
            # attach the ribbon to the dockwidget
            ribbonDock.setWidget(ribbon)

            if Parameters_Ribbon.AUTOHIDE_RIBBON is True:
                ribbonDock.setMaximumHeight(45)

            # Add the dockwidget to the main window
            mw.addDockWidget(Qt.DockWidgetArea.TopDockWidgetArea, ribbonDock)

    def on_hovered(self, ribbonDock: QDockWidget):
        ribbonDock.setMaximumHeight(200)
